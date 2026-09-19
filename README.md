# getsafeshot.app, retired

The site of the app while it was called SafeShot. The app has been MaskFrame since
19 September 2026 and its site is [maskframe.app](https://maskframe.app), from
`vladeku/maskframe-landing`. GitHub Pages was switched off here on 2026-09-19 and the
repository archived: `getsafeshot.app` answers nothing, by decision, and the links to it in
the installed 1.0 and 1.1 were let go with it. The press kit under `press/` went offline at
the same time and is kept here as the source for one on the new domain.

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
