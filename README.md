# Daniel Quek — personal site

Live at **[danielquek.com](https://danielquek.com)**.

A personal portfolio about data platforms, applied AI, automation and side projects. The site uses a three.js opening, JavaScript scroll animations, a light theme with a dark-mode toggle, and a clearly labelled scripted chat. Views expressed are personal.

## Source

- `index.html` — page content, inline styles and JavaScript; edit this file.
- `assets/` — portrait and project images.
- `build_site.py` — creates the standalone page and copies images into `site/dist/`.

The source HTML is a fragment. Run the build to add the full document wrapper, share metadata and favicon before hosting. The generated page loads three.js and fonts from external services.

## Build and preview

Requires Python 3. In Windows PowerShell, from the repository directory:

```powershell
python build_site.py
python -m http.server 8000 --bind 127.0.0.1 --directory site/dist
```

Open [localhost:8000](http://localhost:8000). Press Ctrl+C to stop the preview.

Upload the contents of `site/dist/` to a static host. Keep its images alongside `index.html`. The live site is hosted on ChatGPT Sites; publishing there is managed separately from this repository. Local hosting configuration and generated output are excluded from Git.

## Motion and accessibility

Journey includes a scroll-progress timeline, About uses portrait and text reveals, and Builds includes card reveals and pointer movement. These effects respect reduced-motion preferences. The chat uses pre-written answers and does not call an AI service.
