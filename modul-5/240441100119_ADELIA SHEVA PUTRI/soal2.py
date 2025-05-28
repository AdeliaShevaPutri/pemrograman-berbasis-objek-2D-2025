from abc import ABC, abstractmethod
class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100
    @abstractmethod
    def nyalakan(self):
        pass
    @abstractmethod
    def matikan(self):
        pass
    @abstractmethod
    def gunakan(self,jam):
        pass

class Laptop(PerangkatElektronik):
    def __init__(self):
        self.energi_tersisa = 100
    def nyalakan(self):
        print("Perangkat di nyalakan")
    def matikan(self):
        print("Perangkat di matikan")
    def gunakan(self, jam):
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis!")
    def status(self):
        print(f"Perangkat Laptop dengan jumlah baterai {self.energi_tersisa}%")
    
class Kulkas(PerangkatElektronik):
    def __init__(self):
        self.energi_tersisa = 100
    def nyalakan(self):
        print("Perangkat di nyalakan")
    def matikan(self):
        print("Perangkat di matikan")
    def gunakan(self,jam):
         self.energi_tersisa -= 5*jam
         if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
    def status(self):
        print(f"Perangkat Kulkas dengan jumlah energi {self.energi_tersisa}%")

print("⋆꙳✧༚୨୧⋆꙳✧༚ Perangkat Elektronik ༚✧꙳⋆୨୧༚✧꙳⋆")
print("1. Laptop")
print("2. Kulkas")
pilih = input("Pilih Perangkat: ")
if pilih == "1":
    perangkat = Laptop()
elif pilih == "2":
    perangkat = Kulkas()
else:
    print("Pilihan tidak valid")
    exit()

perangkat.nyalakan()
jam = int(input("Digunakan berapa jam: "))
perangkat.gunakan(jam)
perangkat.status()
perangkat.matikan()