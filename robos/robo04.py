import PyPDF2
from openpyxl import Workbook

pdf_file = open("gastos.pdf", 'rb')

read_pdf = PyPDF2.PdfFileReader(pdf_file)

no_of_pages = read_pdf.getNumPages()

page = read_pdf.getPage(0)

page_content = page.extractText()

parsed = page_content.splitlines()

print(parsed)
