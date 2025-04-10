class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

    def berlari(self):
        print(f"{self.nama} sedang berlari")

orang1 = Manusia("Sheva", 19, "Jl. Pelangi Timur No. 25")
print(f"Nama:{orang1.nama}, Umur:{orang1.umur}, Alamat:{orang1.alamat}")
orang1.berjalan()

orang2 = Manusia("Sella", 22, "Jl. Mawar Indah No. 10")
print(f"Nama:{orang2.nama}, Umur:{orang2.umur}, Alamat:{orang2.alamat}")
orang2.berlari()

orang3 = Manusia("Nelly", 20, "Jl. Cemara Hijau No. 88")
print(f"Nama:{orang3.nama}, Umur:{orang3.umur}, Alamat:{orang3.alamat}")
orang3.berjalan()

orang4 = Manusia("Maudya",25, "Jl. Anggrek Lestari No. 5")
print(f"Nama:{orang4.nama}, Umur:{orang4.umur}, Alamat:{orang4.alamat}")
orang4.berlari()

orang5 = Manusia("Novi", 20, "Jl. Merdeka No. 99")
print(f"Nama:{orang5.nama}, Umur:{orang5.umur}, Alamat:{orang5.alamat}")
orang5.berjalan()




