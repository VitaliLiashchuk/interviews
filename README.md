# Interviews

## CV Versions

This project contains multiple CV versions tailored for different roles:

- **CV/** - General/Main CV
- **CV_BACKEND/** - Backend Developer CV

Each folder contains:
- `cv.org` - Source org-mode format
- `cv.md` - Markdown format
- `cv.pdf` - Compiled PDF

## Steps to Make Your Markdown Beautiful

1. **Export org-mode to Markdown:** Use the `org-md-export-as-markdown` command to export your org-mode files to Markdown format.

2. **Convert Markdown to PDF:** Utilize Pandoc to convert your Markdown file to PDF. Here's a command example:

   For main CV:
   ```bash
   pandoc CV/cv.md --pdf-engine=weasyprint --css=custom.css -o CV/cv.pdf
   pandoc CV/cv.org -o CV/cv.pdf --template=./pandoc-latex-template/eisvogel.tex --listings --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -V toccolor=gray -V pagestyle=empty
   ```

   For backend CV:
   ```bash
   pandoc CV_BACKEND/cv.md --pdf-engine=weasyprint --css=custom.css -o CV_BACKEND/cv.pdf
   pandoc CV_BACKEND/cv.org -o CV_BACKEND/cv.pdf --template=./pandoc-latex-template/eisvogel.tex --listings --pdf-engine=xelatex -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -V toccolor=gray -V pagestyle=empty
   ```
