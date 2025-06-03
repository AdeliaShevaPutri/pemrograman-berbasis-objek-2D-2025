from abc import ABC, abstractmethod
class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji():
        pass

class KaryawanTetap(Karyawan):
    def __init__(self,gaji,tunjangan):
        self.gaji = gaji
        self.tunjangan = tunjangan
        self.bpjs = 2/100 * self.gaji
        self.lembur = 100000
    def hitung_gaji(self,jam):
        if jam > 0:
            return self.gaji + self.tunjangan + self.lembur*jam - self.bpjs
        else:
            return self.gaji + self.tunjangan - self.bpjs
        
class KaryawanKontrak(Karyawan):
    def __init__(self,gaji,kontrak):
        self.gaji = gaji
        self.kontrak = kontrak
        self.lembur = 100000
        self.bpjs = 80000
    def hitung_gaji(self,jam):
        if self.kontrak > 3:
            total_gaji = self.gaji - self.bpjs
            if jam > 0:
                total_gaji += self.lembur*jam
                return total_gaji
            else:
                return total_gaji - self.bpjs
        else:
            if jam > 0:
                return self.gaji + self.lembur*jam
            else:
                return self.gaji

def gaji_tetap(gaji):
    jam = int(input("Jam Lembur 1 bulan: "))
    return gaji.hitung_gaji(jam)
def gaji_kontrak(gaji):
    jam = int(input("Jam lembur 1 bulan: "))
    return gaji.hitung_gaji(jam)
while True:
    print("==Hitung Gaji==")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")
    print("3. Keluar")
    pilih = input("pilih: ")
    if pilih == "1":
        gaji = float(input("Gaji: "))
        tunjangan = float(input("Tunjangan: "))
        tetap = KaryawanTetap(gaji,tunjangan)
        print(gaji_tetap(tetap))
    elif pilih == "2":
        gaji = float(input("Gaji: "))
        kontrak = int(input("Kontrak perbulan: "))
        kontrak = KaryawanKontrak(gaji,kontrak)
        print(gaji_kontrak(kontrak))
    elif pilih == "3":
        break
    else:
        print("Pilihan tidak valid")