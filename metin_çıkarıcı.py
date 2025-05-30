import fitz
def metinçıkarıcı(pdf_path):
    doc = fitz.open(pdf_path)
    for sayfa in doc:
        metin = sayfa.get_text()
        with open(pdf_path[:-3]+"txt","a") as f:
            f.write(metin)
            #f.write( "*** \n")
