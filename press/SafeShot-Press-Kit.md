# SafeShot press kit

Cover what you didn't mean to share.

SafeShot finds the personal details in a screenshot, covers them on your iPhone, and shows
you every mask before you share the copy.

Press page with images and downloads: https://getsafeshot.app/press/
Contact: Vladimir Khuraskin, khuraskin.dev@gmail.com, https://x.com/vladeku

## Short description

SafeShot finds the personal details in a screenshot on your iPhone and covers them. You review
every mask, cover anything it missed, and share the copy.

## Description

SafeShot is a privacy utility for iPhone. Take a screenshot, tap Share, pick SafeShot, and the
editor opens with the personal details already covered: card numbers, IBANs, phone numbers,
email addresses, verification codes, faces and QR codes. With Apple Intelligence turned on,
SafeShot also reads the screenshot for context and catches what no pattern can describe, such
as an account balance, a name in a chat, a street address or a date of birth.

Every suggestion is a mask you can review. Tap a mask to uncover what sits under it, hold to
remove it, drag a box over anything SafeShot missed, undo and redo. The copy you share is a new
image with the masks baked in. The covered pixels are gone and the original stays untouched.

The analysis runs on the iPhone. SafeShot has no server, no account and no analytics, and the
Apple Intelligence model it uses never leaves the device.

## Key features

What it finds

- Pattern checks on every screenshot: card numbers, IBANs, phone numbers in the formats of
  twenty countries, email addresses, one-time codes, IP addresses and map coordinates.
- Image detection: faces and QR codes.
- Apple Intelligence for context: an account balance, a person's name, a street address, a
  date of birth, a username, a booking reference, a medical result. The model sees the picture
  and a numbered list of the text on it and answers with numbers. Vision supplies the
  coordinates, so every mask sits on a line of text Vision found.

You decide

- Tap a mask to uncover it and tap again to cover it. Hold to remove it, drag a corner to
  resize it, or drag over anything SafeShot missed.
- Undo and redo, mask style included.
- Pinch to zoom up to 3x for small text.
- Solid masks by default. The style menu also offers pixelate and blur, under a warning that
  blurred or pixelated details may still be recoverable.

What leaves the phone

- The export is a new image. SafeShot replaces the covered pixels, leaves the original
  untouched, and strips the location, capture date and device metadata from the copy.
- Works from the share sheet in Photos, Files and any app that shares images, and from the
  app itself.

Built for iOS 27

- SwiftUI, Vision and the Foundation Models framework. Dark Mode, Dynamic Type, haptics.
- Localized into 16 languages: Chinese (Simplified and Traditional), Danish, Dutch, English,
  French, German, Italian, Japanese, Korean, Norwegian, Portuguese, Russian, Spanish, Swedish,
  Turkish and Vietnamese.

## How it works

1. Take a screenshot, tap Share, pick SafeShot. Or open SafeShot and choose one from the
   library.
2. SafeShot finds the personal details. Pattern checks and image detection run on every
   screenshot. Apple Intelligence reads it for context.
3. Review. Masks sit over the suggestions. Tap to uncover, hold to remove, drag to cover more.
   The status line counts what is covered and never claims the screenshot is clean.
4. Share the copy. The export is a new image with the masks baked in and no metadata from the
   original.

## Where the data goes

- The screenshot: SafeShot copies it into a protected temporary file when you open it and
  deletes the copy when the editor closes.
- The analysis runs on the iPhone. Vision reads the text, faces and codes, and the Foundation
  Models framework runs the language model on the device. SafeShot never uses Private Cloud
  Compute, and the build fails if that model gets linked in.
- The copy goes wherever you send it, through the system share sheet.
- After a share, SafeShot saves the original screenshot and its masks to your own iCloud, so
  you can reopen a shared copy and edit it again. The developer cannot read it.
- Purchases go through the App Store and RevenueCat, the one third party the app talks to.
- Not collected: no server of our own, no account, no analytics.

## Who it is for

Anyone who explains things with screenshots: a bank confirmation for a landlord, a boarding
pass for a friend, a chat posted to a group for advice, a bug report with an order number in
it, a support ticket with an account page attached. Each one carries something the other
person does not need, and SafeShot covers it before you send.

## From the developer

I send screenshots all day. A receipt to prove a transfer went through, a chat to ask a friend
what they would answer, a settings page to a support agent. Almost every one has something on
it the other person does not need: a balance in the corner, a phone number under a name, a
street address three messages up. Covering it by hand means the markup pen, a shaky rectangle
and a second look I skip when I am in a hurry.

iOS 27 gave me a way to do this. Apple Intelligence can now look at an image on the device and
say what is on it, and Vision has read text on screen for years. SafeShot puts the two
together: Vision says where every line is, the model says which lines are private, and you
decide. No app can promise to remove all your private information, and that promise is what
makes you send a screenshot without a second look. So SafeShot suggests, and you decide.

The other choices followed from that one. Solid masks are the default, because a blur can be
undone. There is no server, because a screenshot of your bank app has no business leaving the
phone. Pro is one purchase, because I would not pay a subscription for a utility either.

Vladimir Khuraskin

## Pricing

SafeShot is free to download. One screenshot a day goes through the whole app, every feature
included. SafeShot Pro removes the daily limit for a single purchase of $14.99 (Lifetime Pro),
with no subscription. Prices vary by country.

Reviewers can ask for a promo code or a TestFlight build by email: khuraskin.dev@gmail.com.

## Fact sheet

- App name: SafeShot (on the App Store: SafeShot: Redact, Mosaic, Blur)
- Developer: Vladimir Khuraskin, independent developer
- Platform: iPhone
- Requires: iOS 27 and an iPhone that supports Apple Intelligence, iPhone 15 Pro or later.
  With Apple Intelligence turned off, the pattern checks and image detection still run.
- Price: free, one screenshot a day. SafeShot Pro: $14.99, one purchase.
- Version: 1.0
- Status: in App Review
- App Store: https://apps.apple.com/app/id6807279858
- Category: Utilities. Secondary: Photo & Video
- Age rating: 4+
- Languages: 16, listed above
- Built with: SwiftUI, Vision, Foundation Models (Apple Intelligence), SwiftData with CloudKit
- Website: https://getsafeshot.app
- Privacy policy: https://sites.google.com/view/safeshot-privacy-policy
- Terms: https://sites.google.com/view/safeshot-terms-and-conditions
- Contact: khuraskin.dev@gmail.com
- X: https://x.com/vladeku

## Brand

- The name is SafeShot, one word, with a capital S at the start and in the middle. Two
  spellings to avoid: Safe Shot and Safeshot.
- The app writes Apple Intelligence out in full and never shortens it to AI.
- Accent teal: #197894 in light appearance, #258FAD in dark. Icon gradient: #3CB6CE to
  #197894. Mask black: #08080A.
- Type: San Francisco, the system font.
- Use the icon as supplied, with the corners it comes with, on its own. Do not recolour it
  or add effects.

## What is in this kit

- Icon: the 1024 px app icon in all six iOS 27 renditions (Default, Dark, Clear Light, Clear
  Dark, Tinted Light, Tinted Dark) plus 512, 256 and 180 px.
- Screenshots/App Store: the three App Store slides, 1320 x 2868, English.
- Screenshots/Raw: five iPhone 17 Pro captures, 1206 x 2622: Home, Editor, Review, Mask
  styles, Dark Mode.
- Screenshots/Framed: the same five inside an iPhone frame on a transparent ground,
  1470 x 3000.
- Video: a 33 second clip of a transfer receipt going through the editor and the share sheet,
  524 x 1080, H.264, no audio, plus a poster frame.

Every screen is drawn, and the people, accounts and numbers on it are fictional.

## Press release

FOR IMMEDIATE RELEASE

SafeShot covers the personal details in a screenshot before you share it, on the iPhone itself

Independent developer Vladimir Khuraskin today released SafeShot, a privacy utility for iPhone
that finds the personal details in a screenshot and covers them before the screenshot goes
out. SafeShot runs its analysis on the device with Apple Intelligence and ships with no
server, no account and no analytics.

Take a screenshot, tap Share, pick SafeShot, and the editor opens with the personal details
already covered. Pattern checks find card numbers, IBANs, phone numbers, email addresses and
verification codes; image detection finds faces and QR codes; Apple Intelligence reads the
screen for context and finds what no pattern can, such as an account balance, a name in a
chat, a street address or a date of birth.

Every suggestion is a mask the user reviews. Tap a mask to uncover it, hold to remove it, drag
over anything the app missed, then share. The copy is a new image with the masks baked in and
no location, date or device metadata from the original.

"The screenshot apps I tried either blur a face for looks or hand you a marker," said
Khuraskin. "SafeShot reads the screen the way you would, points at the balance and the
address, and lets you decide."

"Solid masks are the default because a blur can be undone. The app says so right in the style
menu."

SafeShot is available on the App Store for iPhone 15 Pro and later running iOS 27, in 16
languages. It is free with one screenshot a day. SafeShot Pro removes the daily limit for
$14.99, one purchase, no subscription.

About the developer. Vladimir Khuraskin is an independent developer of iPhone apps. His
earlier apps include Kip, a baby sleep tracker; Plantz, a plant identifier; Astersong, a voice
journal; and Caroosel, a carousel post maker.

Contact: khuraskin.dev@gmail.com. Press kit: https://getsafeshot.app/press/
