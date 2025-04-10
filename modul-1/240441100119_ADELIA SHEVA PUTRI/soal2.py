class Mahasiswa:
    def __init__(self,nama,nim,prodi,alamat):
        self.nama = nama
        self.nim = nim 
        self.prodi = prodi
        self.alamat = alamat
        
    def info_mahasiswa(self):
        return f"nama saya {self.nama} dengan NIM {self.nim} dari prodi {self.prodi} dan saya dari {self.alamat}"

print("masukkan data mahasiswa ke-1")
mhs1 = Mahasiswa(input("Nama :"),input("Nim :"),input("Prodi :"),input("Alamat :"))
print(mhs1.info_mahasiswa())
print("-----------------------------------------------------")

print("masukkan data mahasiswa ke-2")
mhs2 = Mahasiswa(input("Nama :"),input("Nim :"),input("Prodi :"),input("Alamat :"))
print(mhs2.info_mahasiswa())
print("-----------------------------------------------------")

print("masukkan data mahasiswa ke-3")
mhs3 = Mahasiswa(input("Nama :"),input("Nim :"),input("Prodi :"),input("Alamat :"))
print(mhs3.info_mahasiswa())
print("-----------------------------------------------------")



