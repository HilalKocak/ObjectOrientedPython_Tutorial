# Dondurma, Dondurmaci
# stok ekle {"cikolata":200, "vanilya":300}  stok["cikolata"]
# satis yap
# kap ya da kulah secimi olsun
# 9 top dondurmadan fazla dondurma alanlara 1 top bedava verilsin
# nakit, kredi karti ve veresiye olmak uzere farkli odeme secenekleri
# musteri ismi sadece odeme yontemi veresiye iken alinsin
# hangi tur dondurmadan kac tane satildigi bilgisi tutulsun {"cikolata":10, "vanilya":20}
# toplam satis bilgisi tutulsun.
# karar zarar bilgisi tutulsun. 
# Dondurma yere duserse 1 top dondurma bedava verilsin.

class Dondurma:
    def __init__(self, tur, fiyat): # burada fiyat bilgisi 1 top icin
        self.tur = tur
        self.fiyat = fiyat

class Dondurmaci:
    def __init__(self):
        self.stok = {}
        self.satislar = [] # icerisinde bilgilerin bulundugu tuple listesi [("vanilya",3, "veresiye", "Ali veli"), (),,,,]
        self.kar_zarar = 0
        self.tur_satislar = {} # {"cikolata":10, "vanilya":20}

    def stok_ekle(self, dondurma, adet):
        if dondurma.tur not in self.stok:
            self.stok[dondurma.tur] = adet # {"cikolata":200, "vanilya":300, "cilek":400}
        else:
            self.stok[dondurma.tur] += adet

    def satis_yap(self, dondurma, adet, tercih, odeme_yontemi, musteri = None):
        if dondurma.tur not in self.stok or self.stok[dondurma.tur] < adet:
            return "Stok yetersiz"
        self.stok[dondurma.tur] -= adet
        toplam_fiyat = adet * dondurma.fiyat

        if tercih == "kap":
            toplam_fiyat = toplam_fiyat * 1.5

        if adet >= 9: # optional
            toplam_fiyat = (adet - adet//9) * dondurma.fiyat
            self.stok[dondurma.tur] -= adet//9
            self.kar_zarar -= (adet//9) * 3
        
        if odeme_yontemi == "veresiye":
            if not musteri:
                return "Musteri bilgileri eksik"
            else:
                self.satislar.append((dondurma.tur, adet, tercih, odeme_yontemi, musteri))
        else:
            self.satislar.append((dondurma.tur, adet, tercih, odeme_yontemi))
        self.kar_zarar += toplam_fiyat

        if dondurma.tur not in self.tur_satislar:
            self.tur_satislar[dondurma.tur] = adet
        else:
            self.tur_satislar[dondurma.tur] += adet

    def toplam_satis(self):
        return sum(self.tur_satislar.values())
    
    def kar_zarar_durumu(self):
        return self.kar_zarar
    
    def tur_satislar_getir(self):
        return self.tur_satislar
    
    def drop_ice_cream(self, dondurma):
        if dondurma.tur in self.stok:
            self.stok[dondurma.tur] -= 1
            self.kar_zarar -= 3
            return f"{dondurma.tur} dusuruldu 1 top ucretsiz dondurma verildi"
        else:
            "Dondurma kalmadi"

dondurma1 = Dondurma("Cikolata", 5) # 5: 1 top dondurmanin satis fiyati
dondurma2 = Dondurma("Vanilya", 5)
dondurma3 = Dondurma("Cilek", 5)

dondurmaci = Dondurmaci()

dondurmaci.stok_ekle(dondurma1, 100)
dondurmaci.stok_ekle(dondurma2, 150)
dondurmaci.stok_ekle(dondurma3, 120)

            
print("stok", dondurmaci.stok)
print(dondurmaci.kar_zarar_durumu())

dondurmaci.satis_yap(dondurma1, 10, "kulah", "kredi karti")
print("stok", dondurmaci.stok)
# dondurmaci.drop_ice_cream(dondurma2)
print(dondurmaci.kar_zarar_durumu())

print("Toplam satilan top miktari ", dondurmaci.toplam_satis())

print("*" * 30)

dondurmaci.satis_yap(dondurma3, 30, "kap", "kredi karti")
print("Kar zarar durumu ", dondurmaci.kar_zarar_durumu())
print("stok", dondurmaci.stok)
 
print(dondurmaci.drop_ice_cream(dondurma1))
print("stok", dondurmaci.stok)

print("Kar zarar durumu ", dondurmaci.kar_zarar_durumu())
