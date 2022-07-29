import urllib.request
import urllib.parse

try:
    print("\n")

    size=input("Karekod boyutunu giriniz: ")

    veri=input("İçerik: ")

    veriler= {
        'size' :size+ 'x'+ size,
        'data' :veri 
    }

    parametreler=urllib.parse.urlencode(veriler)

    api_link="https://api.qrserver.com/v1/create-qr-code/?" +parametreler

    urllib.request.urlretrieve(api_link,'QR_Code.png')
    print("\n")

    print("Karekod başarıyla oluşturuldu.")
    print("QR_Code.png isimli dosyadan ulaşabilirsiniz.")
    print("\n")
except:
    print("Beklenmeyen bir hata oluştu.")