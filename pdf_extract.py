from PyPDF2 import PdfReader,PdfWriter
from future.backports.urllib.parse import parse_qs

reader = PdfReader("resume.pdf")
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

with open("output.pdf", "wb") as output_file:
    writer.write(output_file)

page_4 = reader.pages[3]
page_4.rotate(270)
writer2 = PdfWriter()
writer2.add_page(page_4)
with open("last_page.pdf", "wb") as fileobj:
    writer2.write(fileobj)

reader1 = PdfReader("resume.pdf")
reader2 = PdfReader("watermark.pdf")
writer1 = PdfWriter()
page = reader2.pages[0]
for p in reader1.pages:
    p.merge_page(page)
    writer1.add_page(p)

with open("withwatermark.pdf", "wb") as f:
    writer1.write(f)