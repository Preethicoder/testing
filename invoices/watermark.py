from PyPDF2 import PdfReader,PdfWriter



reader1 = PdfReader("resume.pdf")
reader2 = PdfReader("watermark.pdf")
writer = PdfWriter()
page = reader2.pages[0]
for p in reader1.pages:
    p.mergePage(page)
    writer.addPage(p)

with open("withwatermark.pdf", "wb") as f:
    writer.write(f)
