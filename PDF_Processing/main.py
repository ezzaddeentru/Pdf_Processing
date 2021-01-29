import PyPDF2

with open("dummy.pdf", "rb") as dummy:
    reader = PyPDF2.PdfFileReader(dummy)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("new_dummy.pdf", "wb") as new_dummy:
        writer.write(new_dummy)