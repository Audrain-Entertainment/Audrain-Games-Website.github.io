# Audrain Entertainment / Kevin Audrain Website

This repository contains the static website for Audrain Entertainment and Kevin Audrain’s professional profile. The site is built with plain HTML and CSS and is designed to be easy to maintain and publish to GitHub Pages.

## What the site includes

- A studio/home landing page for Audrain Entertainment
- A professional history page for Kevin Audrain
- A detailed resume page
- An Android games page listing Google Play titles
- An itch.io games page for published indie game links
- A privacy policy page for the Android apps

## Current structure

- pages/ — main HTML pages
  - index.html — site home page
  - pages/kevin.html — professional history
  - pages/resume.html — detailed resume
  - pages/android-games.html — Google Play games list
  - pages/itch-games.html — itch.io page
  - pages/privacy-policy.html — privacy policy
- assets/ — site assets
  - assets/images/ — logos and photos
  - assets/css/ — stylesheet
  - assets/docs/ — downloadable resume PDF
- scripts/ — helper scripts
  - scripts/make_resume_pdf.py — generates the PDF resume from README.md

## Notes on the current site

- The site is static and does not require a build step.
- The root index.html is the site home page and links to the content pages in pages/.
- The resume PDF is stored in assets/docs/KevinAudrain_Resume.pdf.

## Updating content

To update the site content:

- Edit the relevant HTML file in pages/
- Update shared styling in assets/css/styles.css
- Replace images in assets/images/ if needed

## Generating the resume PDF

From the repository root, run:

```bash
python scripts/make_resume_pdf.py
```

This generates the PDF at assets/docs/KevinAudrain_Resume.pdf.

## Contact

- Email: kevin@audrain.games
- LinkedIn: https://www.linkedin.com/in/kevin-audrain
- GitHub: https://github.com/draino7n7
- Website: https://audrain.games/
