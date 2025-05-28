class Buku:
    def __init__(self,judul,penulis,jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman
    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_jumlah_halaman(self):
        return self.__jumlah_halaman
    
    def info_buku(self):
        print(f"Judul Buku: {self.get_judul()}")
        print(f"Nama Penulis: {self.get_penulis()}")
        print(f"Jumlah Halaman: {self.get_jumlah_halaman()}")

class Perpustakaan:
    list_buku = []
    def tambah_buku(self,buku):
        Perpustakaan.list_buku.append(buku)
    def info_buku(self):
        if not self.list_buku:
            print("Belum ada buku yang ditambahkan")
        else:
            for i in self.list_buku:
                i.info_buku()
                print("-------------------------------")

if __name__ == "__main__":
    perpus = Perpustakaan()

    while True:
        print("\nMenu")
        print("1. Tambah Buku")
        print("2. Info Buku")
        print("3. Keluar")
        pilihan = input("pilihan: ")
        if pilihan == "1":
            while True:
                judul = input("Judul: ")
                if judul != "":
                    break
                else:
                    print("harus diisi")
            while True:
                penulis = input("Penulis: ")
                if penulis != "":
                    break
                else:
                    print("harus diisi")
            while True:
                jumlah_halaman = input("Jumlah Halaman: ")
                if jumlah_halaman != "" and jumlah_halaman.isdigit():
                    break
                else:
                    print("harus diisi dan berupa angka")
            buku = Buku(judul,penulis,jumlah_halaman)
            perpus.tambah_buku(buku)
            print("Buku berhasil ditambahkan")
        elif pilihan == "2":
            print("===Info Buku==")
            perpus.info_buku()
        elif pilihan == "3":
            break
        else:
            print("tidak ada dalam pilihan")