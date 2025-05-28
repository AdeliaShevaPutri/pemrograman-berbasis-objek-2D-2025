class Pasien:
    def __init__(self,nama,umur,keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
    def get_nama(self):
        return self.__nama
    
    def get_umur(self):
        return self.__umur
    
    def get_keluhan(self):
        return self.__keluhan
    
    def info_pasien(self):
        print(f"Nama Pasien: {self.get_nama()}")
        print(f"Umur: {self.get_umur()}")
        print(f"Keluhan: {self.get_keluhan()}")

class Klinik:
    list_pasien = []
    def tambah_pasien(self,pasien):
        Klinik.list_pasien.append(pasien)
    def info_klinik(self):
        if not self.list_pasien:
            print("Belum ada dftar pasien")
        else:
            for i in self.list_pasien:
                i.info_pasien()
                print("-------------------------------")

if __name__ == "__main__":
    klinik = Klinik()

    while True:
        print("\nMenu")
        print("1. Tambah Pasien")
        print("2. Info Pasien")
        print("3. Keluar")
        pilihan = input("pilihan: ")
        if pilihan == "1":
            while True:
                nama = input("nama: ")
                if nama != "":
                    break
                else:
                    print("harus diisi")
            while True:
                umur = input("umur: ")
                if umur != "" and umur.isdigit():
                    break
                else:
                    print("harus diisi dan berupa angka")
            while True:
                keluhan = input("Keluhan: ")
                if keluhan != "":
                    break
                else:
                    print("harus diisi")
            pasien = Pasien(nama,umur,keluhan)
            klinik.tambah_pasien(pasien)
            print("Data pasien berhasil ditambahkan")
        elif pilihan == "2":
            print("===Info Pasien==")
            klinik.info_klinik()
        elif pilihan == "3":
            break
        else:
            print("tidak ada dalam pilihan")