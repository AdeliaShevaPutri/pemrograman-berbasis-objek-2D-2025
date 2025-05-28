from abc import ABC, abstractmethod
class Manusia(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        return f"{self.nama} sedang berbicara tentang politik."

    def bekerja(self):
        return f"{self.nama} bekerja sebagai polisi."

    def makan(self):
        return f"{self.nama} makan sate ayam."

class Beni(Manusia):
    def berbicara(self):
        return f"{self.nama} sedang berbicara tentang teknologi."

    def bekerja(self):
        return f"{self.nama} bekerja sebagai pilot."

    def makan(self):
        return f"{self.nama} makan nasi goreng."

class Fani(Manusia):
    def berbicara(self):
        return f"{self.nama} sedang berbicara tentang seni."

    def bekerja(self):
        return f"{self.nama} bekerja sebagai pelukis."

    def makan(self):
        return f"{self.nama} makan mie ayam."

class Jani(Manusia):
    def berbicara(self):
        return f"{self.nama} sedang berbicara tentang musik."

    def bekerja(self):
        return f"{self.nama} bekerja sebagai musisi."

    def makan(self):
        return f"{self.nama} makan dimsum."

while True:
    print("\n⋆꙳✧༚୨୧⋆꙳✧༚ pilih ༚✧꙳⋆୨୧༚✧꙳⋆")
    print("1. Joko")
    print("2. Beni")
    print("3. Fani")
    print("4. Jani")
    print("5. Keluar")

    pilih = input("Pilih menu (1-5): ")
    if pilih == "5":
        print("babaiii")
        exit()
    else:
        nama = input("Masukkan nama: ")
        if pilih == "1" and nama.lower() == "joko":
            orang = Joko(nama)
            print(f"\n⋆｡˚｡⋆ Aktivitas {nama} ⋆｡˚｡⋆")
            print(orang.berbicara())
            print(orang.bekerja())
            print(orang.makan())
        elif pilih == "2" and nama.lower() == "beni":
            orang = Beni(nama)
            print(f"\n⋆｡˚｡⋆ Aktivitas {nama} ⋆｡˚｡⋆")
            print(orang.berbicara())
            print(orang.bekerja())
            print(orang.makan())
        elif pilih == "3" and nama.lower() == "fani":
            orang = Fani(nama)
            print(f"\n⋆｡˚｡⋆ Aktivitas {nama} ⋆｡˚｡⋆")
            print(orang.berbicara())
            print(orang.bekerja())
            print(orang.makan())
        elif pilih == "4" and nama.lower() == "jani":
            orang = Jani(nama)
            print(f"\n⋆｡˚｡⋆ Aktivitas {nama} ⋆｡˚｡⋆")
            print(orang.berbicara())
            print(orang.bekerja())
            print(orang.makan())
        else:
            print("Pilihan tidak valid atau nama tidak cocok.")
