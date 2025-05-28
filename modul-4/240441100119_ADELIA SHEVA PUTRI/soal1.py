class RekeningBank:
    def __init__(self, nomor_rekening, nama, saldo):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo
    def set_setoran(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setoran harus lebih dari 0.")
    def set_penarikan(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo anda kurang atau penarikan tidak valid.")
    def get_info(self):
        print(f"Nama: {self.nama}")
        print(f"No Rek: {self.nomor_rekening}")
        print(f"Saldo: {self.__saldo}")
    def get_no_rek(self):
        return self.nomor_rekening
    
class Bank:
    data_rekening = []
    def tambah_rekening(self, rekening):
        Bank.data_rekening.append(rekening)
    def cari_rekening(self, no_rek):
        for i in self.data_rekening:
            if i.get_no_rek() == no_rek:
                return i
    def tarik(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.set_penarikan(jumlah)
            print("Penarikan berhasil.")
        else:
            print("Rekening tidak ditemukan.")
    def setor(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.set_setoran(jumlah)
            print("Setoran berhasil.")
        else:
            print("Rekening tidak ditemukan.")
    def info_rekening(self):
        if not self.data_rekening:
            print("Tidak ada rekening.")
        for i in self.data_rekening:
            i.get_info()
            print("--------------------")

def buat_rekening():
    while True:
        nama = input("Nama: ")
        if nama != "":
            break
        else:
            print("Harus diisi")
    while True:
        no_rek = input("No Rek: ")
        if no_rek.isdigit():
            break
        else:
            print("Nomor rekening harus angka.")
    while True:
        saldo = input("Saldo: ")
        if saldo.isdigit():
            saldo = float(saldo)
            break
        else:
            print("Saldo harus berupa angka.")
    return RekeningBank(no_rek, nama, saldo)

if __name__ == "__main__":
    bank = Bank()
    
    while True:
        print("\nMenu:")
        print("1. Tambah rekening")
        print("2. Setor")
        print("3. Tarik")
        print("4. Lihat info rekening tertentu")
        print("5. Info semua rekening")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            rekening_baru = buat_rekening()
            bank.tambah_rekening(rekening_baru)
            print("Rekening baru berhasil ditambahkan.")
        elif pilihan == "2":
            while True:
                no_rek = input("Masukkan No Rekening: ")
                if no_rek != "" and no_rek.isdigit():
                    break
                else:
                    print("Harus diisi dan harus angka")
            while True:
                jumlah = input("Jumlah Setoran: ")
                if jumlah != "" and jumlah.isdigit():
                    jumlah = float(jumlah)
                    break
                else:
                    print("Harus diisi dan harus angka")
            bank.setor(no_rek, jumlah)
        elif pilihan == "3":
            while True:
                no_rek = input("Masukkan No Rekening: ")
                if no_rek != "" and no_rek.isdigit():
                    break
                else:
                    print("Harus diisi dan harus angka")
            while True:
                jumlah = input("Jumlah penarikan: ")
                if jumlah != "" and jumlah.isdigit():
                    jumlah = float(jumlah)
                    break
                else:
                    print("Harus diisi dan harus angka")
            bank.tarik(no_rek, jumlah)
        elif pilihan == "4":
            while True:
                no_rek = input("Masukkan No Rekening: ")
                if no_rek != "" and no_rek.isdigit():
                    break
                else:
                    print("Harus diisi dan harus angka")
            rek = bank.cari_rekening(no_rek)
            if rek:
                rek.get_info()
            else:
                print("Rekening tidak ditemukan.")
        elif pilihan == "5":
            print("=== Info Semua Rekening ===")
            bank.info_rekening()
        elif pilihan == "6":
            print("makasiiiiiiiii")
            break
        else:
            print("Pilihan tidak valid.")