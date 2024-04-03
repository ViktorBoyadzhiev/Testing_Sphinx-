#file:///C:/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/index.html

import pdfkit
import os

current_file_location = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_location)
print("Current directory:", current_directory)

input_html_path = "/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/index.html"

# Absolute path to the output PDF file
output_pdf_path = "/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/file.pdf"

# Path to wkhtmltopdf
wkhtmltopdf_path = '/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

# Convert HTML to PDF using absolute paths
pdfkit.from_file(input_html_path, output_pdf_path, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))
