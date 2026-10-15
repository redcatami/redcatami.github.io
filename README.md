# Redcatami — personal brand website

A responsive, build-free website for Stanislav Kvitko (Redcatami), ready for GitHub Pages. Includes nine public Credly badges, a scrollable carousel, individual badge links, and a clickable TryHackMe profile icon.

## Deploy on GitHub Pages

1. Extract the ZIP. Upload the **contents** of `redcatami/` to the root of your GitHub repository (so `index.html` is at the repository root).
2. Commit the files to your `main` branch.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, select **GitHub Actions**. The included `.github/workflows/pages.yml` publishes the static website on pushes to `main`.
5. Wait for GitHub's Pages deployment to finish. Open the URL shown in the Pages settings.

Published from the root of `redcatami/redcatami.github.io` to https://redcatami.github.io/. All local assets use relative paths, so the files also work on a project repository site. No build command, package installation, API key, or server is required.

## Preview

Open `index.html` directly in a browser, or serve this folder with any static web server. The website does not fetch JSON at runtime and works from a local file. Internet access is needed for the original badge images and outbound profiles.

## Files

- `index.html` — all content and badge cards; fully usable without JavaScript
- `styles.css` — responsive layout, visual identity, reduced-motion support
- `script.js` — carousel buttons, keyboard navigation, image fallback, footer year
- `assets/mark.svg` — original Redcatami cat mark and favicon
- `badges.json` — reference snapshot of verified badge names, dates, artwork, and destinations; **not a runtime data source**
- `.nojekyll` — tells GitHub Pages to serve static files directly

## Credential sources and accuracy

Reviewed the rendered public [Credly profile](https://www.credly.com/users/stanislav-kvitko.67c29f61/badges/credly) on **October 15, 2026**. All nine card destinations and artwork URLs were extracted from the profile's public badge cards. No badge IDs were guessed. Microsoft Azure Fundamentals is labeled AZ-900 as requested by the owner. No scores, job history, professional experience, project accomplishments, or TryHackMe rankings are claimed.

The collection contains CompTIA A+, Network+, Security+, Microsoft Azure Fundamentals, ISC2 CC, CompTIA CIOS and CSIS stackable credentials, APISEC|CON 2025 attendance, and the historical ISC2 Candidate badge. **ISC2 Candidate expired February 5, 2024** and is explicitly marked expired. Conference attendance is not presented as certification. Dates are a static snapshot, not a live validity check; review them periodically against Credly.

TryHackMe points to the exact owner-supplied [Redcatami profile](https://tryhackme.com/p/redcatami). Its icon is an original cloud/terminal illustration, not an official TryHackMe logo. Credential images are original images hosted by Credly and belong to their respective issuers. The site is not affiliated with those issuers.

## Update content

Edit the badge anchors in `index.html`, and keep the reference snapshot in `badges.json` in sync. For a new badge, verify its public record on the owner's Credly profile before adding its name, artwork, and individual URL. If an individual URL cannot be verified, use the profile URL above. Do not invent UUIDs. Update the review date whenever you review the credential collection.

Badge artwork loads from `images.credly.com`, with a readable text fallback if an image fails. There are no analytics, tracking scripts, embedded third-party widgets, remote fonts, or live API dependencies. External links open in a new tab with `noopener noreferrer`.

## Accessibility and interaction

The carousel supports horizontal touch scrolling, a native scrollbar, Previous/Next buttons, keyboard arrows while focused, and ordinary Tab navigation to every badge. It does not autoplay. Reduced-motion preferences disable animated scrolling. Navigation, focus indicators, headings, a skip link, descriptive link names, and image alternatives are included. Without JavaScript, all badge links and native scrolling remain available.
