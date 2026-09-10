# -*- coding: utf-8 -*-
"""Derives everything on the press page from the source files under press/assets.

    python3 build/build.py            # rebuild framed screenshots, thumbnails, icons, OG image, zip
    python3 build/build.py --import /path/to/safeshot-ios
                                      # first copy the sources out of the app repo's .build

Sources (committed): press/assets/icon/*-1024*.png, press/assets/screenshots/app-store/*.png,
press/assets/screenshots/raw/*.png, press/assets/video/SafeShot-Demo.mp4, build/frame-17promax.png.
Derived (also committed, so GitHub Pages can serve them): framed screenshots, the .webp
thumbnails under press/assets/web, the smaller icon sizes, favicon and touch icon, the OG
image, SafeShot-Press-Kit.zip, and the file sizes printed beside every download link.

Needs Pillow (with WebP) and, for the OG image, Google Chrome at its usual path. The import
step also needs ffmpeg for the demo clip.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
PRESS = os.path.join(ROOT, "press")
ASSETS = os.path.join(PRESS, "assets")
WEB = os.path.join(ASSETS, "web")
FRAME = os.path.join(HERE, "frame-17promax.png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# The iPhone 17 Pro Max frame: the screen sits at (75, 66), 1320 x 2868, corner radius 110.
SCREEN_ORIGIN = (75, 66)
SCREEN_SIZE = (1320, 2868)
SCREEN_RADIUS = 110

RAW = [
    ("SafeShot-1-Home", "Home"),
    ("SafeShot-2-Editor", "Editor"),
    ("SafeShot-3-Review", "Review"),
    ("SafeShot-4-Mask-Styles", "Mask styles"),
    ("SafeShot-5-Dark-Mode", "Dark Mode"),
]

ICONS = {
    "Default.png": "SafeShot-Icon-1024.png",
    "Dark.png": "SafeShot-Icon-1024-Dark.png",
    "ClearLight.png": "SafeShot-Icon-1024-Clear-Light.png",
    "ClearDark.png": "SafeShot-Icon-1024-Clear-Dark.png",
    "TintedLight.png": "SafeShot-Icon-1024-Tinted-Light.png",
    "TintedDark.png": "SafeShot-Icon-1024-Tinted-Dark.png",
}

SLIDES = {"01-share.png": "SafeShot-AppStore-1.png",
          "02-iphone.png": "SafeShot-AppStore-2.png",
          "03-finds.png": "SafeShot-AppStore-3.png"}

CAPTURES = {"home.png": "SafeShot-1-Home.png",
            "receipt-3covered.png": "SafeShot-2-Editor.png",
            "receipt-uncovered.png": "SafeShot-3-Review.png",
            "receipt-stylemenu.png": "SafeShot-4-Mask-Styles.png",
            "chat-6covered.png": "SafeShot-5-Dark-Mode.png"}


def import_sources(app_repo):
    """Copy the icon renders, the en-US App Store set, the raw captures and the onboarding
    clip out of the app repository. `make icon` and the screenshot scripts there produce the
    first three; the clip is re-encoded to square pixels on the way."""
    build = os.path.join(app_repo, ".build")
    for src, dst in ICONS.items():
        shutil.copy(os.path.join(build, "icon", src), os.path.join(ASSETS, "icon", dst))
    for src, dst in SLIDES.items():
        shutil.copy(os.path.join(build, "screenshots", "en-US", src),
                    os.path.join(ASSETS, "screenshots", "app-store", dst))
    for src, dst in CAPTURES.items():
        shutil.copy(os.path.join(build, "screenshots", "captures", src),
                    os.path.join(ASSETS, "screenshots", "raw", dst))
    shutil.copy(os.path.join(app_repo, "Tools", "screenshots", "frame-17promax.png"), FRAME)
    clip = os.path.join(app_repo, "SafeShot", "Onboarding", "onboarding.mp4")
    out = os.path.join(ASSETS, "video", "SafeShot-Demo.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", clip,
                    "-vf", "scale=524:1080:flags=lanczos,setsar=1",
                    "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", "-an", out], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "6.5", "-i", out, "-frames:v", "1", "-q:v", "3",
                    os.path.join(ASSETS, "video", "SafeShot-Demo-Poster.jpg")], check=True)
    print("imported from", app_repo)


def rounded(im, radius):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=radius, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def framed(raw_png, out_png):
    """The capture inside the iPhone frame on a transparent ground, at the frame's own size."""
    frame = Image.open(FRAME).convert("RGBA")
    shot = Image.open(raw_png).convert("RGB").resize(SCREEN_SIZE, Image.LANCZOS)
    canvas = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    canvas.paste(rounded(shot, SCREEN_RADIUS), SCREEN_ORIGIN)
    canvas.alpha_composite(frame)
    canvas.save(out_png, optimize=True)
    return canvas


def thumb(im, width, out, quality=82):
    """A WebP for the page. Transparent sources keep their alpha."""
    im = im.convert("RGBA") if im.mode in ("RGBA", "LA", "P") else im.convert("RGB")
    h = round(im.height * width / im.width)
    im.resize((width, h), Image.LANCZOS).save(out, "WEBP", quality=quality, method=6)


def icons():
    src = os.path.join(ASSETS, "icon", "SafeShot-Icon-1024.png")
    im = Image.open(src).convert("RGBA")
    for size in (512, 256, 180):
        im.resize((size, size), Image.LANCZOS).save(
            os.path.join(ASSETS, "icon", "SafeShot-Icon-%d.png" % size), optimize=True)
    for name in sorted(glob.glob(os.path.join(ASSETS, "icon", "*-1024*.png"))):
        base = os.path.basename(name)[:-4]
        thumb(Image.open(name), 256, os.path.join(WEB, base + ".webp"))
    # The site's own favicon and touch icon, and the icon the root page shows.
    im.resize((64, 64), Image.LANCZOS).save(os.path.join(ROOT, "favicon.png"), optimize=True)
    im.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, "apple-touch-icon.png"), optimize=True)
    shutil.copy(os.path.join(ASSETS, "icon", "SafeShot-Icon-512.png"), os.path.join(ROOT, "assets", "icon-512.png"))


def screenshots():
    for base, _ in RAW:
        raw = os.path.join(ASSETS, "screenshots", "raw", base + ".png")
        fr = framed(raw, os.path.join(ASSETS, "screenshots", "framed", base + "-Framed.png"))
        thumb(Image.open(raw), 600, os.path.join(WEB, base + ".webp"))
        thumb(fr, 720, os.path.join(WEB, base + "-Framed.webp"))
    for n in (1, 2, 3):
        slide = os.path.join(ASSETS, "screenshots", "app-store", "SafeShot-AppStore-%d.png" % n)
        thumb(Image.open(slide), 660, os.path.join(WEB, "SafeShot-AppStore-%d.webp" % n))
    poster = os.path.join(ASSETS, "video", "SafeShot-Demo-Poster.jpg")
    if os.path.exists(poster):
        thumb(Image.open(poster), 524, os.path.join(WEB, "SafeShot-Demo-Poster.webp"))


def og_image():
    """1200 x 630 for link previews, rendered by Chrome from build/og.html."""
    if not os.path.exists(CHROME):
        print("no Chrome, keeping the existing OG image")
        return
    page = os.path.join(HERE, "og.html")
    out = os.path.join(ROOT, "assets", "og.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--force-device-scale-factor=1",
                    "--hide-scrollbars", "--window-size=1200,630", "--screenshot=" + out,
                    "file://" + page], check=True, capture_output=True)
    Image.open(out).convert("RGB").save(os.path.join(ROOT, "assets", "og.jpg"), quality=88, optimize=True)
    os.remove(out)


def kit_zip():
    """Everything a writer needs in one download, with the text beside the images."""
    out = os.path.join(PRESS, "SafeShot-Press-Kit.zip")
    folders = [("icon", "Icon"), ("screenshots/app-store", "Screenshots/App Store"),
               ("screenshots/raw", "Screenshots/Raw"), ("screenshots/framed", "Screenshots/Framed"),
               ("video", "Video")]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(PRESS, "SafeShot-Press-Kit.md"), "SafeShot Press Kit/SafeShot Press Kit.md")
        for src, dst in folders:
            for path in sorted(glob.glob(os.path.join(ASSETS, src, "*"))):
                z.write(path, "SafeShot Press Kit/%s/%s" % (dst, os.path.basename(path)))
    return out


def human(n):
    return "%.1f MB" % (n / 1048576) if n >= 1048576 else "%d KB" % round(n / 1024)


def fill_sizes():
    """Every <span data-size="path"> on the press page shows the file's current size."""
    page = os.path.join(PRESS, "index.html")
    html = open(page, encoding="utf-8").read()

    def repl(m):
        path = os.path.normpath(os.path.join(PRESS, m.group(1)))
        if not os.path.exists(path):
            raise SystemExit("missing download target: " + m.group(1))
        return '<span data-size="%s">%s</span>' % (m.group(1), human(os.path.getsize(path)))

    new = re.sub(r'<span data-size="([^"]+)">[^<]*</span>', repl, html)
    if new != html:
        open(page, "w", encoding="utf-8").write(new)
    sizes = {m.group(1): m.group(2) for m in re.finditer(r'data-size="([^"]+)">([^<]*)<', new)}
    json.dump(sizes, open(os.path.join(HERE, "sizes.json"), "w"), indent=1)
    return sizes


if __name__ == "__main__":
    os.makedirs(WEB, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    if len(sys.argv) > 2 and sys.argv[1] == "--import":
        import_sources(os.path.abspath(sys.argv[2]))
    icons()
    screenshots()
    og_image()
    print("zip", human(os.path.getsize(kit_zip())))
    for path, size in fill_sizes().items():
        print("%-60s %s" % (path, size))
