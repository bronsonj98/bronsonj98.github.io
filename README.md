# bronsonj98.github.io

Source for the personal academic website of Moonseong (Bronson) Jeong, https://bronsonj98.github.io/, built with Jekyll on GitHub Pages from the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template (MIT License; see LICENSE).

Content lives in `_pages/` (home, CV, publications, talks, teaching), `_publications/`, `_talks/`, `_teaching/`, and `llms.txt`. The homepage layout is `_layouts/home-modern.html` with styles in `assets/css/site-redesign.css`. The PDF CV in `files/` is built from `cv_src/cv.tex` (Tectonic); `cv_src/` is excluded from the Jekyll build.

Pushing to `master` triggers the GitHub Pages build; check it with `gh run list -R bronsonj98/bronsonj98.github.io`.
