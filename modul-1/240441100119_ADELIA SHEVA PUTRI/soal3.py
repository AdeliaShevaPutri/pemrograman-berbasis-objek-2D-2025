class Kucing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur= umur
    
    def suara(self):
        return f"{self.nama} mengeluarkan suara Meow!"
    
    def info_umur(self):
        return f"{self.nama} saat ini berumur {self.umur} tahun."

class Kuda:
    def __init__(self, nama, warna, jumlah_kaki):
        self.nama = nama
        self.warna = warna
        self.jumlah_kaki = jumlah_kaki
    
    def suara(self):
        return f"{self.nama} mengeluarkan suara Neigh!"
    
    def bergerak(self):
        return f"{self.nama} berlari cepat menggunakan {self.jumlah_kaki} kaki."

class Dinosaurus:
    def __init__(self, nama, periode, panjang_tubuh):
        self.nama = nama
        self.periode = periode
        self.panjang_tubuh = panjang_tubuh
    
    def suara(self):
        return f"{self.nama} mengeluarkan suara Roar!"
    
    def bergerak(self):
        return f"{self.nama} berjalan dengan langkah besar sepanjang {self.panjang_tubuh} meter."

list_kucing = [
    Kucing("cila", "anggora", 1),
    Kucing("cilo", "persia", 2)
]

list_kuda = [
    Kuda("thunder", "coklat", 4),
    Kuda("starpink", "pink", 4)
]

list_dinosaurus = [
    Dinosaurus("crusher", "jura tengah", 12),
    Dinosaurus("venom", "kapur akhir", 15)
]

for kucing in list_kucing:
    print(f"{kucing.nama} adalah seekor kucing ras {kucing.ras}.")
    print(f"{kucing.suara()}")
    print(f"{kucing.info_umur()}")
    print("-------------------------------")

for kuda in list_kuda:
    print(f"{kuda.nama} adalah seekor kuda berwarna {kuda.warna}.")
    print(f"{kuda.suara()}")
    print(f"{kuda.bergerak()}")
    print("-------------------------------")

for dinosaurus in list_dinosaurus:
    print(f"{dinosaurus.nama} adalah seekor dinosaurus  yang hidup pada periode {dinosaurus.periode}.")
    print(f"{dinosaurus.suara()}")
    print(f"{dinosaurus.bergerak()}")
    print("-------------------------------")

