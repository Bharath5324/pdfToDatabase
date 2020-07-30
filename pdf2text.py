import pdfplumber
with pdfplumber.open(r'text.pdf') as pdf:
    x = pdf.pages[0]
    # print(x.extract_text())
    file_object = open(r"/home/vishnu/Desktop/Source-codes/pyth//test1.txt", "a")
    file_object.write(x.extract_text())

    file_object.close()