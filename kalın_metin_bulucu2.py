import fitz
def kalınharflerinsatırlarıvesayfaları(pdf_path):
    doc = fitz.open(pdf_path)
    kalın_metinler = []
    satır_sayıcısı = 0
    #sıra=0
    özet=""
    #başlık=""
    üstbaşlık=""
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    #satır_metni = []
                    for span in line["spans"]:
                        satır_sayıcısı += 1
                        metin=span["text"]
                        #satır_metni.append(metin)
                        if (span["flags"] & (1 << 4)) or "bold" in span["font"].lower():
                            if metin[0].islower() or metin==" ":
                                özet+=metin
                                pass
                            else:
                                    #print(metin)
                                    #sıra = satır_sayıcısı
                                    büyük=0
                                    küçük=0
                                    metin.replace('"',"\"")
                                    for a in metin:
                                        if a.isupper():
                                            büyük+=1
                                        else:
                                            küçük+=1
                                    if büyük>küçük:
                                        üstbaşlık=metin
                                    #full_line = "".join(satır_metni).strip()
                                    #if full_line:
                                    kalın_metinler.append({
                                        "page": page_num,
                                        "line": satır_sayıcısı,
                                        "başlık": metin,
                                        "üstbaşlık" : üstbaşlık,
                                        "summary" : özet, })
                                    özet=""
#                                   metin=""
                                    pass
                        else:
                            özet+=metin

    return kalın_metinler
