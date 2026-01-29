from invoke import task

@task
def build(c):
    """Build CV files: convert org to markdown and generate styled PDFs with weasyprint"""
    cv_dir = "CV"
    cv_file = "vitali_liashchuk_cv"

    print("Building CV files...")

    # Convert org to markdown
    print(f"Converting {cv_dir}/{cv_file}.org to markdown...")
    c.run(f"pandoc {cv_dir}/{cv_file}.org -o {cv_dir}/{cv_file}.md")

    # Generate PDF from markdown using weasyprint with custom CSS
    print(f"Generating {cv_dir}/{cv_file}.pdf with styling...")
    c.run(f"pandoc {cv_dir}/{cv_file}.md --pdf-engine=weasyprint --css=custom.css -o {cv_dir}/{cv_file}.pdf")

    print("✓ Build complete!")
    print(f"Generated files:")
    c.run(f"ls -lh {cv_dir}/{cv_file}.*")

@task
def build_plain(c):
    """Build CV files using pdflatex (no styling)"""
    cv_dir = "CV"
    cv_file = "vitali_liashchuk_cv"

    print("Building CV files with pdflatex...")

    # Convert org to markdown
    print(f"Converting {cv_dir}/{cv_file}.org to markdown...")
    c.run(f"pandoc {cv_dir}/{cv_file}.org -o {cv_dir}/{cv_file}.md")

    # Generate PDF from org using pdflatex
    print(f"Generating {cv_dir}/{cv_file}.pdf with pdflatex...")
    c.run(f"pandoc {cv_dir}/{cv_file}.org --pdf-engine=pdflatex -o {cv_dir}/{cv_file}.pdf")

    print("✓ Build complete!")
    print(f"Generated files:")
    c.run(f"ls -lh {cv_dir}/{cv_file}.*")

@task
def view(c):
    """Display CV file information"""
    cv_dir = "CV"
    cv_file = "vitali_liashchuk_cv"

    print(f"\nCV files in {cv_dir}/:")
    c.run(f"ls -lh {cv_dir}/{cv_file}.*")
