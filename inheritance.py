class calisanlar():
    def __init__(self,ad,soyad,maas,departman):
        print("Çalışan sınıfının init fonksiyonu.")

        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman

    def BilgileriGoster(self):
        print("""
                        Bilgiler Yazdırılıyor...
        Ad : {}\nSoyad : {}\nMaaş : {}\nDepartman : {}\n """.format(self.ad,self.soyad,self.maas,self.departman))

    def DepartmanDegistir(self,yeni_departman):
        self.departman = yeni_departman

class yonetici(calisanlar):
    def __init__(self,ad,soyad,maas,departman,kisi_sayisi):
        print("Yönetici sınıfının init fonksiyonu.")
        super().__init__(ad, soyad, maas, departman)
        self.kisi_sayisi = kisi_sayisi

    def BilgileriGoster(self):
        print("""
                        Bilgiler Yazdırılıyor...
        Ad : {}\nSoyad : {}\nMaaş : {}\nDepartman : {}\n Kişi Sayısı : {}\n""".format(self.ad,self.soyad,self.maas,self.departman,self.kisi_sayisi))




    def zam_yap(self,zam_miktari):
        self.maas+=zam_miktari





#calisan1 = calisanlar("Taha","Oyanık",5000,"Bilişim")
#calisan1.BilgileriGoster()
yonetici1 = yonetici("Mustafa","Aslan",10000,"M.Yardımcısı",5)
yonetici1.zam_yap(500)
yonetici1.BilgileriGoster()
