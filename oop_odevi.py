from abc import ABC, abstractmethod

# ==========================================
# 1. KAYNAK VE ALT SINIFLARI (VERİ MODELLERİ)
# ==========================================

class Kaynak(ABC):
    """Tüm kaynakların ortak özelliklerini barındıran soyut sınıf."""
    def __init__(self, baslik, kayit_no):
        self.baslik = baslik
        self.kayit_no = kayit_no

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayit_no(self):
        return self._kayit_no

    @kayit_no.setter
    def kayit_no(self, value):
        self._kayit_no = value

    @abstractmethod
    def __str__(self):
        pass


class Kitap(Kaynak):
    def __init__(self, baslik, kayit_no, yazar, sayfa_sayisi):
        super().__init__(baslik, kayit_no)
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"[KİTAP] Kayıt No: {self.kayit_no} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"


class Dergi(Kaynak):
    def __init__(self, baslik, kayit_no, yayin_donemi, sayi_no):
        super().__init__(baslik, kayit_no)
        self.yayin_donemi = yayin_donemi
        self.sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"[DERGİ] Kayıt No: {self.kayit_no} | Başlık: {self.baslik} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"


# ==========================================
# 2. İŞLEM SINIFLARI (MANTIK / YÖNETİM)
# ==========================================

class Islem(ABC):
    """CRUD işlemleri için şablon belirleyen soyut sınıf."""
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def ekle(self):
        baslik = input("Kitabın başlığını girin: ")
        kayit_no = input("Kitabın kayıt numarasını girin: ")
        
        # BONUS: Kayıt numarası tekrar kontrolü
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                print("Hata: Bu kayıt numarasına sahip bir kitap zaten var!")
                return

        yazar = input("Kitabın yazarını girin: ")
        sayfa_sayisi = input("Kitabın sayfa sayısını girin: ")
        
        yeni_kitap = Kitap(baslik, kayit_no, yazar, sayfa_sayisi)
        self.kitaplar.append(yeni_kitap)
        print("Kitap başarıyla eklendi.")
        # BONUS: Toplam kayıt sayısını gösterme
        print(f"Toplam Kitap Sayısı: {len(self.kitaplar)}")

    def sil(self):
        kayit_no = input("Silmek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                self.kitaplar.remove(kitap)
                print("Kitap başarıyla silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        kayit_no = input("Güncellemek istediğiniz kitabın kayıt numarasını girin: ")
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                kitap.baslik = input("Yeni Başlık: ")
                kitap.yazar = input("Yeni Yazar: ")
                kitap.sayfa_sayisi = input("Yeni Sayfa Sayısı: ")
                print("Kitap güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        # BONUS: Liste boşken uyarı mesajı
        if not self.kitaplar:
            print("Kayıt bulunamadı.")
            return
        print("\n--- KİTAP LİSTESİ ---")
        for kitap in self.kitaplar:
            print(kitap) # BONUS: __str__ metodu çağrılır
        print(f"Toplam Kitap Sayısı: {len(self.kitaplar)}")


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def ekle(self):
        baslik = input("Derginin başlığını girin: ")
        kayit_no = input("Derginin kayıt numarasını girin: ")
        
        # BONUS: Kayıt numarası tekrar kontrolü
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                print("Hata: Bu kayıt numarasına sahip bir dergi zaten var!")
                return

        yayin_donemi = input("Yayın dönemi (Aylık/Haftalık vb.): ")
        sayi_no = input("Sayı numarasını girin: ")
        
        yeni_dergi = Dergi(baslik, kayit_no, yayin_donemi, sayi_no)
        self.dergiler.append(yeni_dergi)
        print("Dergi başarıyla eklendi.")
        # BONUS: Toplam kayıt sayısını gösterme
        print(f"Toplam Dergi Sayısı: {len(self.dergiler)}")

    def sil(self):
        kayit_no = input("Silmek istediğiniz derginin kayıt numarasını girin: ")
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                self.dergiler.remove(dergi)
                print("Dergi başarıyla silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        kayit_no = input("Güncellemek istediğiniz derginin kayıt numarasını girin: ")
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                dergi.baslik = input("Yeni Başlık: ")
                dergi.yayin_donemi = input("Yeni Yayın Dönemi: ")
                dergi.sayi_no = input("Yeni Sayı Numarası: ")
                print("Dergi güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        # BONUS: Liste boşken uyarı mesajı
        if not self.dergiler:
            print("Kayıt bulunamadı.")
            return
        print("\n--- DERGİ LİSTESİ ---")
        for dergi in self.dergiler:
            print(dergi) # BONUS: __str__ metodu çağrılır
        print(f"Toplam Dergi Sayısı: {len(self.dergiler)}")


# ==========================================
# 3. MENÜ SINIFI VE ANA UYGULAMA DÖNGÜSÜ
# ==========================================

class Menu:
    @staticmethod
    def goster():
        print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")

def main():
    kitap_yonetimi = KitapIslem()
    dergi_yonetimi = DergiIslem()

    while True:
        Menu.goster()
        secim = input("\nYapmak istediğiniz işlemi seçin (1-9): ")

        if secim == '1':
            kitap_yonetimi.ekle()
        elif secim == '2':
            kitap_yonetimi.sil()
        elif secim == '3':
            kitap_yonetimi.guncelle()
        elif secim == '4':
            kitap_yonetimi.listele()
        elif secim == '5':
            dergi_yonetimi.ekle()
        elif secim == '6':
            dergi_yonetimi.sil()
        elif secim == '7':
            dergi_yonetimi.guncelle()
        elif secim == '8':
            dergi_yonetimi.listele()
        elif secim == '9':
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 9 arasında bir sayı girin.")

if __name__ == "__main__":
    main()