class Mahasiswa:
    jumlah_mahasiswa = 0
    def __init__(self,nama,nim,prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matakuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matakuliah(self, matakuliah):
        if matakuliah not in self.matakuliah:
            self.matakuliah.append(matakuliah)
        else:
            print("Mata kuliah telah diambil.")
    def biodata(self):
        print(f"Nama saya:{self.nama}")
        print(f"NIM:{self.nim}")
        print(f"Prodi:{self.prodi}")
        for matkul in self.matakuliah:
            print(f"matkul:{matkul.nama},kode:{matkul.kode},sks:{matkul.sks}")
    @classmethod
    def jumlah(cls):
        return cls.jumlah_mahasiswa 
    @staticmethod
    def validasi(nim):
        return nim.startswith("23") and len(nim) == 10
            
class Matakuliah:
    def __init__(self,kode,nama,sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def info(self):
        return f"kode:{self.kode}, nama:{self.nama}, sks:{self.sks}"
    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3
    
class Kampus:
    jumlah_mahasiswa = 0 
    def __init__(self, nama_kampus, alamat):
        self.nama_kampus = nama_kampus
        self.alamat = alamat
    @classmethod
    def jumlah(cls):
        return f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}"
    @staticmethod
    def validasi_angka(nama_kampus):
        if nama_kampus.isalpha:
            return nama_kampus
    def info(self):
        return f"Nama Kampus: {self.nama_kampus}, Alamat: {self.alamat}"
    def tambah_mahasiswa(self):
        Kampus.jumlah_mahasiswa += 1

nama_kampus = input("masukkan nama kampus: ")
alamat_kampus = input("Alamat Kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)

matkul_list = []
print("\nMasukkan 8 Mata Kuliah:")
i = 1
while i <= 8:
    print(f"\nMata Kuliah ke-{i}")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks_input = input("SKS (2 atau 3): ")
    if sks_input.isdigit():
        sks = int(sks_input)
        if Matakuliah.validasi_sks(sks):
            matkul_list.append(Matakuliah(kode, nama, sks))
            i += 1
        else:
            print("SKS harus 2 atau 3.")
    else:
        print("Masukkan angka.")

mhs_list = []
print("\nMasukkan 6 Mahasiswa:")
min = 1
while min <= 6:
    print(f"\nMahasiswa ke-{min}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    if not Mahasiswa.validasi(nim):
        print("NIM harus diawali '23' dan terdiri dari 10 digit.")
        continue
    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)

    print("Pilih 4 mata kuliah dari daftar:")
    for j in range(len(matkul_list)):
        mk = matkul_list[j]
        print(f"{j+1}. {mk.nama} ({mk.kode}) - {mk.sks} SKS")

    pilih = 1
    while pilih <= 4:
        pilihan = input(f"Matkul ke-{pilih} (1-{len(matkul_list)}): ")
        if pilihan.isdigit():
            angka = int(pilihan)
            if 1 <= angka <= len(matkul_list):
                mhs.tambah_matakuliah(matkul_list[angka - 1])
                pilih+= 1
            else:
                print("Nomor tidak sesuai.")
        else:
            print("Masukkan angka.")

    mhs_list.append(mhs)
    min += 1

print("\n=== DATA MAHASISWA ===")
for mhs in mhs_list:
    mhs.biodata()

print("\n=== DATA KAMPUS ===")
kampus.info()
if Kampus.validasi_angka(nama_kampus):
    print("Nama kampus valid.")
else:
    print("Nama kampus tidak valid.")


