#NUMBER 1
#Data mahasiswa
mahasiswa = [
    {"nama": "Andi", "nilai": 80},
    {"nama": "Budi", "nilai": 70},
    {"nama": "Cici", "nilai": 90},
    {"nama": "Dodi", "nilai": 60},
    {"nama": "Eka", "nilai": 85}
]

# Fungsi untuk menampilkan tabel
def tampilkan_tabel(data):
    print("=" * 30)
    print(f"{'Nama':<10} {'Nilai':<10}")
    print("=" * 30)

    for mhs in data:
        print(f"{mhs['nama']:<10} {mhs['nilai']:<10}")

    print("=" * 30)


#Filter data
# Ambil mahasiswa dengan nilai >= 75
lulus = [mhs for mhs in mahasiswa if mhs["nilai"] >= 75]

#Sorting berdasarkan nama
lulus.sort(key=lambda x: x["nama"])

#Tampilkan hasil dalam bentuk tabel
tampilkan_tabel(lulus)

#Print Jumlah Akhir
print(f"Jumlah mahasiswa lulus: {len(lulus)}")

#***********************************************************

#NOMOR 2
# Data dalam bentuk tuple (immutable)
data_nilai = (80, 70, 90, 80, 60, 70, 80, 90, 60)

#Ambil nilai unik menggunakan set
nilai_unik = set(data_nilai)

print("Nilai unik:", nilai_unik)


#Hitung frekuensi menggunakan dictionary
frekuensi = {}

for nilai in data_nilai:
    if nilai in frekuensi:
        frekuensi[nilai] += 1
    else:
        frekuensi[nilai] = 1

print("Frekuensi nilai:", frekuensi)


#Mencari frekuensi tertinggi
maks_frekuensi = max(frekuensi.values())

# Cari semua nilai dengan frekuensi tertinggi
nilai_terbanyak = [nilai for nilai, jumlah in frekuensi.items() if jumlah == maks_frekuensi]


#Tampilkan hasil
print("Frekuensi tertinggi:", maks_frekuensi)
print("Nilai dengan frekuensi tertinggi:", nilai_terbanyak)

#**************************************************************************************************

#NOMOR 3
# Class Induk
class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nilai):
        self.__nama = nama 
        self.__nilai = nilai
        Mahasiswa.jumlah_mahasiswa += 1

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Getter untuk nilai
    def get_nilai(self):
        return self.__nilai

    # Method biasa
    def tampilkan_info(self):
        print(f"Nama: {self.__nama}, Nilai: {self.__nilai}")

    # Method statis
    @staticmethod
    def total_mahasiswa():
        return Mahasiswa.jumlah_mahasiswa


#Class Turunan 
class MahasiswaLulus(Mahasiswa):

    def __init__(self, nama, nilai):
        super().__init__(nama, nilai)


    def tampilkan_info(self):
        print(f"{self.get_nama()} LULUS dengan nilai {self.get_nilai()}")


#Program Utama
m1 = Mahasiswa("Andi", 70)
m2 = MahasiswaLulus("Budi", 85)
m3 = MahasiswaLulus("Cici", 90)

print("=== Data Mahasiswa ===")
m1.tampilkan_info()
m2.tampilkan_info()
m3.tampilkan_info()

print("\nTotal mahasiswa:", Mahasiswa.total_mahasiswa())

#*****************************************************************

#NOMOR 4
#Class Node
class Node:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama
        self.next = None


#Class Antrian
class Antrian:
    def __init__(self):
        self.head = None

    # ke akhir
    def enqueue(self, id, nama):
        new_node = Node(id, nama)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        print(f"{nama} berhasil ditambahkan ke antrian.")

    # dari depan
    def dequeue(self):
        if self.head is None:
            print("Antrian kosong!")
            return

        print(f"{self.head.nama} keluar dari antrian.")
        self.head = self.head.next

    #Tampilkan antrian
    def tampilkan(self):
        current = self.head
        print("\nIsi Antrian:")

        if current is None:
            print("Antrian kosong")
            return

        while current:
            print(f"ID: {current.id}, Nama: {current.nama}")
            current = current.next

    #Cari berdasarkan nama
    def cari_nama(self, nama):
        current = self.head

        while current:
            if current.nama == nama:
                print(f"{nama} ditemukan dengan ID {current.id}")
                return
            current = current.next

        print(f"{nama} tidak ditemukan.")

    # Hapus berdasarkan ID
    def hapus_id(self, id):
        current = self.head
        prev = None

        # Kondisi: antrian kosong
        if current is None:
            print("Antrian kosong!")
            return

        #Kondisi 1: node di head
        if current.id == id:
            print(f"{current.nama} (ID: {id}) dihapus dari head.")
            self.head = current.next
            return

        #Kondisi 2: tengah / akhir
        while current and current.id != id:
            prev = current
            current = current.next

        if current is None:
            #Kondisi 3: ID tidak ditemukan
            print(f"ID {id} tidak ditemukan dalam antrian.")
        else:
            print(f"{current.nama} (ID: {id}) dihapus dari antrian.")
            prev.next = current.next


#Program Utama
antrian = Antrian()

antrian.enqueue(1, "Andi")
antrian.enqueue(2, "Budi")
antrian.enqueue(3, "Cici")
antrian.enqueue(4, "Dodi")

antrian.tampilkan()

antrian.dequeue()
antrian.tampilkan()

antrian.cari_nama("Cici")

antrian.hapus_id(3) 
antrian.hapus_id(1)
antrian.hapus_id(10) 

antrian.tampilkan()