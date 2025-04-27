import fitz  # PyMuPDF
#import statistics
import os
def kalınharflerinsatırlarıvesayfaları(pdf_path):
    doc = fitz.open(pdf_path)
    bold_lines = []
    #font_büyüklüğü = []
    line_counter = 0
    sıra=0
    özet=""
    başlık=""
    üstbaşlık=""
    üstte=0
    #os.rmdir(pdf_path[:-4])
    try:
        os.mkdir(pdf_path[:-4])
    except:
        for filename in os.listdir(pdf_path[:-4]):
            file_path = os.path.join(pdf_path[:-4], filename)
            os.remove(file_path)
    os.chdir(pdf_path[:-4])
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        #line_counter = 0  # Reset line counter for each page
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_counter += 1
                    line_text = []
                    bold_found = False
                    #öncekisatırdakalın=0
                    for span in line["spans"]:
                        metin=span["text"]
                        kalın_mı = (span["flags"] & (1 << 4)) or "bold" in span["font"].lower()
                        for i in range(10):
                            if metin==f"{i}":
                                kalın_mı=False
                        if len(metin)<=4:
                            kalın_mı=False
#                           for i in range(len(metin)):
#                                   print(ord(metin[i]),"\n")
#                                   if ord(metin[i])>300:
#                                           kalın_mı = False
                        line_text.append(metin)
                        #font_büyüklüğü.append(span["size"])
                        if kalın_mı: #and öncekisatırdakalın==0:
                            bold_found = True
                            if metin[0].islower():
                                özet+=metin
                                pass
                            else:
                                with open(pdf_path[:-4]+f"{sıra}.json","a") as f:
                                    f.write("{\n")
                                    f.write(f" \"title\": \"{başlık}\",\n \"parent_title\":\"{üstbaşlık}\",\n \"page\": {page_num},\n \"summary\": \"{özet}\"")
                                    sıra = line_counter
                                    başlık=metin
                                    büyük=0
                                    küçük=0
                                    for a in metin:
                                        if a.islower():
                                            küçük+=1
                                            print(küçük,büyük)
                                        else:
                                            büyük+=1
#                                        match a.isupper():
#                                            case False:
#                                                küçük+=0
#
#                                            case True:
#                                                büyük+=1
#                                                print(küçük)
                                    if büyük>=küçük:
                                        üstbaşlık=metin
                                    f.write("\n}")
                                    özet=""
                                    pass
                            #öncekisatırdakalın=1
                        else:
                            özet+=metin
                    if bold_found:
                        full_line = "".join(line_text).strip()
                        if full_line:
                            bold_lines.append({
                                "page": page_num,
                                "line": line_counter,
                                "text": full_line
                            })
    return bold_lines
#def büyükfontlar(pdf_path):
