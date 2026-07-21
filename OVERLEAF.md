# Editing the CV in Overleaf

The CV is a self-contained LaTeX document and does not require images, custom fonts, or bibliography files.

## Fastest option

1. Open <https://www.overleaf.com/>.
2. Select **New Project → Upload Project**.
3. Upload `CV_Zihao_Zhang_Overleaf.zip`.
4. Click **Recompile**.

The uploaded project contains `CV_Zihao_Zhang_en.tex`. Because it is the only `.tex` document, Overleaf should select it automatically. If it does not, open **Menu → Main document** and select `CV_Zihao_Zhang_en.tex`.

## Editing

- Personal details and all CV content are below `\begin{document}`.
- Reusable layout commands such as `\EducationEntry`, `\ExperienceEntry`, and `\Publication` are defined in the preamble.
- Links use `\href{URL}{visible text}`.
- LaTeX special characters must be escaped: write `\%`, `\&`, and `\_` for percent signs, ampersands, and underscores in visible text.

The project uses standard packages available on Overleaf and can be compiled with the default **pdfLaTeX** compiler.

## Publishing an updated PDF

After editing, choose **Download PDF** in Overleaf and replace `CV_Zihao_Zhang_en.pdf` in the homepage repository. The homepage already links to that filename.
