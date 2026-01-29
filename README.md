# Interviews

## CV

The `CV/` folder contains:
- `vitali_liashchuk_cv.org` - Source org-mode format
- `vitali_liashchuk_cv.md` - Markdown format
- `vitali_liashchuk_cv.pdf` - Compiled PDF

## Build Commands

This project uses [PyInvoke](https://www.pyinvoke.org/) to automate the build process.

### Quick Build:
```bash
# Build with styling (weasyprint + custom.css) - default
invoke build

# Build without styling (pdflatex)
invoke build-plain

# View file information
invoke view
```

### Manual Conversion Workflow

If you prefer to run pandoc commands directly:

**Convert org-mode to Markdown:**
```bash
pandoc CV/vitali_liashchuk_cv.org -o CV/vitali_liashchuk_cv.md
```

**Generate PDF:**

Using pdflatex:
```bash
pandoc CV/vitali_liashchuk_cv.org --pdf-engine=pdflatex -o CV/vitali_liashchuk_cv.pdf
```

Using weasyprint:
```bash
pandoc CV/vitali_liashchuk_cv.md --pdf-engine=weasyprint -o CV/vitali_liashchuk_cv.pdf
```
