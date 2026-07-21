# Zihao Zhang — Academic Homepage

This is a static, responsive academic homepage for Zihao Zhang. It is intentionally framework-free so it can be deployed directly to GitHub Pages.

## Local preview

Any static file server works. For example:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Files

- `index.html` — page content and semantic structure.
- `styles.css` — responsive visual system and layout.
- `script.js` — mobile navigation and section-aware navigation state.
- `CV_Zihao_Zhang_en.tex` — editable LaTeX source for the English CV.
- `CV_Zihao_Zhang_en.pdf` — downloadable English CV.
- `CV_Zihao_Zhang_Overleaf.zip` — self-contained project that can be uploaded directly to Overleaf.
- `OVERLEAF.md` — concise editing and compilation instructions.
- `assets/papers/` — locally cached paper thumbnails used in the publication cards.

The Google Scholar entry links to the public profile. SPEED links to its public arXiv paper, source-code repository, and project page.

## Editing the CV in Overleaf

The LaTeX source is now the source of truth; the previous Python/ReportLab generator has been retired. See `OVERLEAF.md` or upload `CV_Zihao_Zhang_Overleaf.zip` as a new Overleaf project.
