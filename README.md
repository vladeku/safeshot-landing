# getsafeshot.app

The website for [SafeShot](https://getsafeshot.app), a privacy utility for iPhone that covers
the personal details in a screenshot before it is shared. Served by GitHub Pages from `main`.

- `index.html` is the home page: icon, tagline, App Store badge, links.
- `press/` is the press kit, live at [getsafeshot.app/press](https://getsafeshot.app/press/):
  description, features, fact sheet, screenshots, icon, video, brand notes, a press release,
  and `SafeShot-Press-Kit.zip` with all of it. `SafeShot-Press-Kit.md` is the text half of
  the zip.
- `build/build.py` derives the framed screenshots, the `.webp` thumbnails, the smaller icon
  sizes, the favicon, the OG image, the zip and the file sizes shown beside every download
  link from the source files under `press/assets`.

## Updating the assets

The sources come out of the app repository, `safeshot-ios`: `make icon` renders the icon into
`.build/icon/`, the screenshot scripts under `Tools/screenshots` produce the App Store set and
the raw captures, and `SafeShot/Onboarding/onboarding.mp4` is the demo clip.

```bash
python3 build/build.py --import ../safeshot-ios   # copy the sources in, re-encode the clip
python3 build/build.py                            # derive everything else
```

Needs Pillow with WebP, ffmpeg for the import, and Google Chrome for the OG image. Commit the
derived files too: GitHub Pages serves the repository as it is.

## Updating the text

The press page and `press/SafeShot-Press-Kit.md` carry the same copy. Change both. Things
that will change first:

- The App Review status and the App Store link. Version 1.0 is in review; the badge and the
  App Store link resolve once Apple releases it.
- The quotes in the press release, which are drafted in the developer's voice.

No em dash anywhere, the same rule the app follows.

## Domain

`getsafeshot.app` is registered at Namecheap. For GitHub Pages it needs these records in
Advanced DNS:

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | vladeku.github.io |

Remove the parking records first. Then set the domain on the Pages site and turn on HTTPS
once the certificate is issued:

```bash
gh api -X PUT repos/vladeku/safeshot-landing/pages -f cname=getsafeshot.app
gh api -X PUT repos/vladeku/safeshot-landing/pages -F https_enforced=true
```

Until the records exist the site is at https://vladeku.github.io/safeshot-landing/.
