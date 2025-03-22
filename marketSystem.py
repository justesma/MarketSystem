market = {
    "elma":{"fiyat":10, "stok": 50},
    "muz":{"fiyat":15, "stok": 30},
    "peynir":{"fiyat":60, "stok": 20},
    "süt":{"fiyat":25, "stok": 10},
}
print("Market yönetim sistemine hoşgeldiniz!")
print("1. Market sahibi")
print("2. Müşteri")

giris= input("1 ya da 2'ye basınız: ")

if giris=="1":
    print("Market sahibi olarak giriş yaptınız.")
    while True:
        print("\n1. Ürün ekle")
        print("2. Ürün fiyatı güncelle")
        print("3. Ürün sil")
        print("4. Ürün listesini görüntüle")
        print("5. Çıkış")

        secim= input("Seçiminizi yapın:")

        if secim=="1":
            yeni_urun= input("Yeni ürünün adını girin: ")
            try:
                fiyat= int(input(f"{yeni_urun} ürününün fiyatını girin: "))
                stok= int(input(f"{yeni_urun} ürününün stok miktarını girin: "))
                market[yeni_urun]={"fiyat":fiyat,"stok":stok}
                print(f"{yeni_urun} ürünü başarıyla eklendi :) ")
            except ValueError:
                print("Geçersiz değer girdiniz. Lütfen sayı girin")

        elif secim=="2":
            urun= input("Fiyatını güncellemek istediğiniz ürünü giriniz: ")
            if urun in market:
                try:
                    yeni_fiyat= int(input(f"{urun} için yeni fiyatı girin: "))
                    market[urun]["fiyat"]=yeni_fiyat
                    print(f"{urun} ürününün fiyatı güncellendi")
                except ValueError:
                    print("Geçersiz fiyat girdiniz. Lütfen geçerli bir sayı girin.")
            else:
                print(f"{urun} ürünü bulunamadı.")
        elif secim =="3":
            urun=input("Silmek istediğiniz ürünün adını giriniz: ")
            if urun in market:
                del market[urun]
                print(f"{urun} ürünü başarıyla silindi.")
            else:
                print(f"{urun} ürünü bulunamadı.")
        elif secim=="4":
            print("\nMarket Ürün Listesi: ")
            for urun, detaylar in market.items():
                print(f"{urun} - fiyat:{detaylar['fiyat']} TL, stok: {detaylar['stok']}")

        elif secim=="5":
            print("Çıkış Yapılıyor!!!")
            break
        else:
            print("Geçersiz Seçim!")
elif giris =="2":
    print("Müşteri olarak giriş yaptınız.")
    toplam_tutar=0
    sepet={}
    while True:
        print("\n1. Ürünleri görüntüle")
        print("2. Ürün satın al")
        print("3. Sepeti görüntüle")
        print("4. Ödeme yap ve çıkış yap")

        secim=input("Seçiminizi yapın: ")



