# Interviews

## CV

The `CV/` folder contains:
- `vitali_liashchuk_cv.org` - Source org-mode format
- `vitali_liashchuk_cv.md` - Markdown format
- `vitali_liashchuk_cv.pdf` - Compiled PDF

## Conversion Workflow

### Convert org-mode to Markdown:
```bash
pandoc CV/vitali_liashchuk_cv.org -o CV/vitali_liashchuk_cv.md
```

### Generate PDF from Markdown:

**Option 1: Using weasyprint (recommended - simple and clean)**
```bash
pandoc CV/vitali_liashchuk_cv.md --pdf-engine=weasyprint -o CV/vitali_liashchuk_cv.pdf
```

**Option 2: Using pdflatex (alternative)**
```bash
pandoc CV/vitali_liashchuk_cv.org --pdf-engine=pdflatex -o CV/vitali_liashchuk_cv.pdf
```

### With Custom Styling (optional):
If you have a `custom.css` file:
```bash
pandoc CV/vitali_liashchuk_cv.md --pdf-engine=weasyprint --css=custom.css -o CV/vitali_liashchuk_cv.pdf
```
