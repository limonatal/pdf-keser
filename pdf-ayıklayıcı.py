from kalın_metin_bulucu import  kalınharflerinsatırlarıvesayfaları
#from metin_çıkarıcı import metinçıkarıcı
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Kullanım: python pdf-ayıklayıcı.py girdi.pdf")
        sys.exit(1)

    bold_lines =  kalınharflerinsatırlarıvesayfaları(sys.argv[1])

    print(f"{len(bold_lines)} kadar başlık bulundu.")
    for entry in bold_lines:
        print(f"Sayfa {entry['page']} Satır {entry['line']} Metin {entry['text']}")
