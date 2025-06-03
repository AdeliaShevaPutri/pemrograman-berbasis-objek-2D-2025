class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self,sisi):
        self.sisi = sisi
    def luas(self):
        return f"Luas: {self.sisi * self.sisi}"

class Lingkaran(BangunDatar):
    def __init__(self,diameter):
        self.pi = 3.14
        self.diameter = diameter
    def luas(self):
        return f"Luas: {self.pi * (self.diameter/2)}"

class Segitiga(BangunDatar):
    def __init__(self,a,t):
        self.a = a
        self.t = t
    def luas(self):
        return f"Luas: {1/2 * self.a * self.t}"
    
def luas_persegi(persegi):
    return persegi.luas()

def luas_lingkaran(lingkaran):
    return lingkaran.luas()

def luas_segitiga(segitiga):
    return segitiga.luas()

while True:
    print("\n==Hitung Luas==")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")
    pilih = input("Pilih hitung luas: ")
    if pilih == "1":
        sisi = float(input("sisi: "))
        persegi = Persegi(sisi)
        print(luas_persegi(persegi))
    elif pilih == "2":
        diameter = float(input("Diameter: "))
        lingkaran = Lingkaran(diameter)
        print(luas_lingkaran(lingkaran))
    elif pilih == "3":
        alas = float(input("Alas: "))
        tinggi = float(input("Tinggi: "))
        segitiga = Segitiga(alas,tinggi)
        print(luas_segitiga(segitiga))
    elif pilih == "4":
        break
    else:
        print("Pilihan tidak valid")