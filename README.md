# getsafeshot.app

The old domain of the app that has been called MaskFrame since 19 September 2026. Its site is
[maskframe.app](https://maskframe.app), from `vladeku/maskframe-landing`. Served by GitHub
Pages from `main`.

**This domain has to keep answering.** Every installed copy of versions 1.0 and 1.1 links to
`getsafeshot.app/privacy/` and `getsafeshot.app/terms/`, so those two, the home page and
`404.html` are redirects to the same path on `maskframe.app`: a meta refresh, a
`location.replace` that keeps the query and the fragment, a canonical link and `noindex`.
GitHub Pages cannot send a 301, and one repository serves one custom domain, which is why the
two sites are two repositories.

- `index.html` redirects to the home page on `maskframe.app`.
- `press/` is the press kit, live at [getsafeshot.app/press](https://getsafeshot.app/press/):
  description, features, fact sheet, screenshots, icon, video, brand notes, a press release,
  and `SafeShot-Press-Kit.zip` with all of it. `SafeShot-Press-Kit.md` is the text half of
  the zip.
- `privacy/` and `terms/` redirect to the documents on `maskframe.app`. They were moved here
  from Google Sites on 2026-09-10 and on to `maskframe.app` on 2026-09-19, under the new name
  only.
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

- Version 1.0 went live on the App Store on 14 September 2026; both pages carry the badge
  and the link, https://apps.apple.com/app/id6807279858. Update the release row and the
  press release when a version ships.
- The quotes in the press release, which are drafted in the developer's voice.

No em dash anywhere, the same rule the app follows.

## Domain

`getsafeshot.app` is registered at Namecheap and attached to this Pages site since
2026-09-10. Advanced DNS there holds four A records for `@` (185.199.108.153,
185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME `www` to `vladeku.github.io`;
the parking URL Redirect record had to go, since it adds a fifth address to the apex. `CNAME`
in the repository root is GitHub's, written when the domain was set, and GitHub Pages
enforces HTTPS. The old address, https://vladeku.github.io/safeshot-landing/, redirects.
