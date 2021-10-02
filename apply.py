import os
import sys
import markdown
from weasyprint import HTML, CSS


def apply(argv) -> bool:
    # argv should only process 2 arguments
    if len(argv) != 2:
        print("> Invalid input. Please use the following format:")
        print(f'$ python3 apply.py "company_name" cover_letter_outline')
        print(f'> Note that the company name must be in quotes.')
        return False

    company_name = argv[0]
    outline = argv[1]

    # Create directory if it doesn't exist'
    if not os.path.exists("pdf"):
        os.mkdir("pdf")

    if not os.path.exists("css"):
        os.mkdir("css")

    # Format the PDF filename after converting all content
    pdf_filename = "pdf/" + company_name.lower().replace(" ", "_") + "_cover_letter" + ".pdf"

    with open(outline, mode='r', encoding='utf-8') as outline_file:
        # Convert Markdown to pure string
        content = outline_file.read()

        try:
            # Insert company name into template
            content = content.format(company_name, company_name, company_name)
        except:
            print("> An error occurred while formatting the outline with the company name.")
            print("> Please ensure the number of curly brackets in the outline"
                  " is the same as the string formatting in apply.py")
            return False

        # Convert Markdown as plain text to HTML
        html = markdown.markdown(content)

        # Write HTML content
        with open('output.html', mode='w', encoding='utf-8') as output_file:
            output_file.write(html)

        # Load stylesheet and convert styled HTML to PDF
        with open('css/style.css', 'r') as css_filename:
            # Convert CSS to plain string
            style = css_filename.read()

            try:
                HTML('output.html').write_pdf(pdf_filename, stylesheets=[CSS(string=style)])
            except:
                print("> An error occurred while converting HTML to PDF.")
                return False

        # Clean up unnecessary HTML
        os.remove("output.html")

    return True


if __name__ == '__main__':
    # Syntax: python3 apply.py company_name cover_letter_outline
    succeeded = apply(sys.argv[1:])

    print(
        "> Successfully created cover letter!"
        if succeeded
        else "> An error occurred when trying to create cover letter!"
    )
