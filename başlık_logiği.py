dosya_hiyerarşisi=[]
def hiyerarşi(başlıklar_listesi):
    # İş: başlıklar_listesi [ {'başlık': ...}, ... ]
    # Her başlık için ana başlık hesapla (ör: 1.2.5 için 1.2), ve parent_title olarak ekle
    başlık_dict = {b['başlık']: b for b in başlıklar_listesi}

    prev_no_number_title = None

    for idx, a in enumerate(başlıklar_listesi):
        b = a["başlık"]

        # Sayı içeren başlık mı? (örn: "1.2", "3" gibi)
        has_number = any(char.isdigit() for char in b)
        # Parantez içeriyorsa ignore
        has_paren = ('(' in b or ')' in b)

        if '.' in b and has_number:
            parent_b = b.rsplit('.', 1)[0]
            if parent_b in başlık_dict and parent_b != b:
                a['hesaplanan_ustbaslik'] = parent_b
            # Eğer numaralı başlıktan önce sayısız ve parantezsiz bir başlık varsa onu da üstbaşlık yap
            elif prev_no_number_title:
                a['hesaplanan_ustbaslik'] = prev_no_number_title
            else:
                a['hesaplanan_ustbaslik'] = ''
        elif has_number and not has_paren:
            # Tek rakamlı başlıksa ("3" gibi), önceki olarak sayısız başlık varsa onu kullan
            if prev_no_number_title:
                a['hesaplanan_ustbaslik'] = prev_no_number_title
            else:
                a['hesaplanan_ustbaslik'] = ''
        else:
            # Sayısı veya parantezi olmayan başlık: referans için hatırlanır
            a['hesaplanan_ustbaslik'] = ''
            if not has_paren and not has_number:
                prev_no_number_title = b

    return başlıklar_listesi
