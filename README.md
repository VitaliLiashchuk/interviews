# Interviews

## Steps to Make Your Markdown Beautiful

1. **Export org-mode to Markdown:** Use the `org-md-export-as-markdown` command to export your org-mode files to Markdown format.

2. **Convert Markdown to PDF:** Utilize Pandoc to convert your Markdown file to PDF. Here's a command example:

   ```bash
   pandoc CV/cv.md --pdf-engine=weasyprint --css=custom.css -o CV/cv.pdf
