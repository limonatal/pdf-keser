from kalın_metin_bulucu2 import  kalınharflerinsatırlarıvesayfaları
from json_üretici import json_türet
#from metin_çıkarıcı import metinçıkarıcı
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(sys.argv)
        print("Kullanım: python pdf-keser.py (--üret) girdi.pdf")
        sys.exit(1)
#    elif sys.argv=="üret":
#        json_türet(kalın_başlıklar)
    jçalıştır=0
    for a in sys.argv:
        if a=="--üret" or a=="-ü":
            jçalıştır=1
        elif (a[-4:]) == ".pdf":
            kalın_başlıklar=kalınharflerinsatırlarıvesayfaları(a)
            print(f"{len(kalın_başlıklar)} kadar başlık bulundu.")
            for girdi in kalın_başlıklar:
                pass
                #print(f"Sayfa: {girdi['page']}, Satır: {girdi['line']}, Başlık: {girdi["başlık"]}, Üstbaşlık: {girdi["üstbaşlık"]} Metin: {girdi['summary']} \n")
            if jçalıştır:
                json_türet(kalın_başlıklar,a)
#        else:
#            print(".pdf'li bir dosya gir lan mal.")
