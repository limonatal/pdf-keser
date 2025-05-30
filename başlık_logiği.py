def hiyerarşi(başlıklar_listesi):
    # İş: başlıklar_listesi [ {'başlık': ...}, ... ]
    # Her başlık için ana başlık hesapla (ör: 1.2.5 için 1.2), ve parent_title olarak ekle
    başlık_dict = {b['başlık']: b for b in başlıklar_listesi}

    prev_no_number_title = None

    for idx, a in enumerate(başlıklar_listesi):
        b = a["başlık"]
        has_yasaörnekyorum = -b.find("Örnek") * -b.find("Yorum") * -b.find("Yasa")
        # Sayı içeren başlık mı? (örn: "1.2", "3" gibi)
        has_number = any(char.isdigit() for char in b)
        # Parantez içeriyorsa ignore
        has_paren = ('(' in b or ')' in b)
        if '.' in b and has_number:
            parent_b = b.rsplit('.', 1)[0]
            if parent_b in başlık_dict and parent_b != b:
                a['öncülbaşlık'] = parent_b
            # Eğer numaralı başlıktan önce sayısız ve parantezsiz bir başlık varsa onu da üstbaşlık yap
            elif prev_no_number_title:
                a['öncülbaşlık'] = prev_no_number_title
            else:
                a['öncülbaşlık'] = ''
        elif has_number:
            # Tek rakamlı başlıksa ("3" gibi), önceki olarak sayısız başlık varsa onu kullan
            if prev_no_number_title:
                a['öncülbaşlık'] = prev_no_number_title
            else:
                a['öncülbaşlık'] = ''
        elif has_paren:
                    # Tek rakamlı başlıksa ("3" gibi), önceki olarak sayısız başlık varsa onu kullan
                if prev_no_number_title:
                    a['öncülbaşlık'] = prev_no_number_title
                else:
                    a['öncülbaşlık'] = ''
        else:
            # Sayısı veya parantezi olmayan başlık: referans için hatırlanır
            a['öncülbaşlık'] = ''
            if not has_paren and not has_number and has_yasaörnekyorum:
                prev_no_number_title = b
                #print(b)
#    for a in başlıklar_listesi:
#        print(a['öncülbaşlık'])
    return başlıklar_listesi
