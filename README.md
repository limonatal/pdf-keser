
  ### PDF bölücü!
PDF'lerinizi başlıklara göre minik metin bölüklerine bölmek için bir araç.
  ## Nasıl kullanılır?
Depoyu klonlamanın akabinde projenin cmd ya da konsoldan cd ile ana dalına geldikten sonra python sanal ortamını aktive edin.
# Linux:
    > source /path/to/project/bin/activate
    ya da fish kullanıyorsanız.
    > source /path/to/project/bin/activate.fish
# Windows:
    > cd /path/to/project/bin
    > ./Activate.ps1

Geri kalanı çok kolay, bölmek istediğiniz pdf dosyanızı aynı klasöre koyarsanız aşağıdaki komut size pdf'in bölünmüş metin dosyalarından oluşan yeni bir klasör yaratacaktır:

    > python3 pdf-ayıklayıcı.py <pdf_ismi>.pdf
