import PyPDF2


with open("meetingminutes.pdf", "rb") as pdf_file_obj:
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    kk = pdf_reader.pages[1].extract_text()
    with open("Text_From_PDF.txt", "w") as pdf_text:
        pdf_text.write(kk)
