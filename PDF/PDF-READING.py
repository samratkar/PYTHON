import PyPDF2

# reading the pdf file
pdf_object = open('DATA-FILES/animal_farm.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_object)

# Number of pages in the PDF file
print(pdf_reader.numPages)

# get a certain page's text
page_object = pdf_reader.getPage(5)

# Extract text from the page_object
print(page_object.extractText())
