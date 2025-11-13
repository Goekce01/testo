from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

#create a pdf file reader object
pdf = PdfReader("Test_text.pdf")

# 2 steps to extract the text
#Step1 : grab the Page(s)

page_1_object = pdf.pages[0]
#print(page_1_object)

#Step2 extract the text from the page
text = page_1_object.extract_text()
#print(text)

# combine teh text from  all the pages
with Path("Test_text_2nd.txt").open(mode='w', encoding='utf-8') as output_file:
    text = ''
    for page in pdf.pages:
        text += page.extract_text() or ""
    output_file.write(text)

    # where's Time?
    time_pages = []
    for i, page in enumerate(pdf.pages):
        #page_num = page['/StructParents'] #actual page number is +1
        page_text = page.extract_text() or ""
        
        if 'time' in page_text: # page_text.find('time') for index position of time
            time_pages.append(i)

#print(time_pages)

#save "time" pages to a pdf

#create PdfReader object
input_pdf = PdfReader('Test_text.pdf')

# create PdfWriter object
pdf_writer = PdfWriter()

#Get the text from pages with 'Time'
for i in time_pages:
    page_object = pdf.pages[i]
    pdf_writer.add_page(page_object)

# save pages as pdf
with Path('time_pages.pdf').open(mode="wb") as output_file_2:
    pdf_writer.write(output_file_2)
