# getsafeshot.app

The website for [SafeShot](https://getsafeshot.app), a privacy utility for iPhone that covers
the personal details in a screenshot before it is shared. Served by GitHub Pages from `main`.

- `index.html` is the home page: icon, tagline, App Store badge, links.
- `press/` is the press kit, live at [getsafeshot.app/press](https://getsafeshot.app/press/):
  description, features, fact sheet, screenshots, icon, video, brand notes, a press release,
  and `SafeShot-Press-Kit.zip` with all of it. `SafeShot-Press-Kit.md` is the text half of
  the zip.
- `privacy/` and `terms/` are the privacy policy and the terms, moved here from Google Sites
  on 2026-09-10 with the text unchanged. The app's Settings links and the store listing were
  switched to these addresses in the app repository the same day; the Google Sites pages stay
  up until a build with the new links is on the App Store.
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

- The App Review status. Version 1.0 is in review, so both pages show a Coming soon pill
  and no store link. On release, swap the pill for the App Store badge
  (`press/assets/appstore-badge.svg`, kept for that day) linking to
  https://apps.apple.com/app/id6807279858.
- The quotes in the press release, which are drafted in the developer's voice.

No em dash anywhere, the same rule the app follows.

## Domain

`getsafeshot.app` is registered at Namecheap and attached to this Pages site since
2026-09-10. Advanced DNS there holds four A records for `@` (185.199.108.153,
185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME `www` to `vladeku.github.io`;
the parking URL Redirect record had to go, since it adds a fifth address to the apex. `CNAME`
in the repository root is GitHub's, written when the domain was set, and GitHub Pages
enforces HTTPS. The old address, https://vladeku.github.io/safeshot-landing/, redirects.
