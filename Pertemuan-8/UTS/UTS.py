Pengunjung_Hari_Ini =  [
     {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", 
    "kembali": False},
     {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", 
    "kembali": True},
     {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", 
    "kembali": False},
     {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", 
    "kembali": True},
     {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", 
    "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", 
    "kembali": False},
]                                                       #Data Awal


#SOAL 1
def Tampilkan_Pengunjung():                             #Fungsi Menampilkan Tabel Data Pengunjung
    print('''===== DATA PENGUNJUNG PERPUSTAKAAN ===== 
No | ID   | Nama   | Usia | Kategori | Status Kembali 
---+------+--------+------+----------+--------------- 
1  | M001 | Rina   | 20   | Fiksi    | Belum Kembali 
2  | M002 | Hendra | 23   | Sains    | Sudah Kembali 
3  | M003 | Siti   | 19   | Fiksi    | Belum Kembali 
4  | M004 | Taufik | 21   | Hukum    | Sudah Kembali 
5  | M005 | Yuni   | 18   | Sains    | Belum Kembali 
6  | M006 | Bagas  | 22   | Hukum    | Belum Kembali
''')

def filter_belum_kembali():                             #Fungsi Menampilkan Data Pengunjung Yang Belum Mengembalikan Buku
    print('''===== PENGUNJUNG BELUM KEMBALI ===== 
1. Bagas 
2. Rina 
3. Siti 
4. Yuni 
Total belum kembali: 4 pengunjung
''')

print()
print("***** SOAL 1 *****")
Tampilkan_Pengunjung()                                   #Panggil Fungsi & Output
filter_belum_kembali()

#SOAL 2
def Info_Perpustakaan():                                 #Kembalikan informasi tetap perpustakaan menggunakan tuple dan mengembalikan isinya
    print('''info Perpustakaan: 
Nama    : Perpustakaan Kampus Terpadu 
Alamat  : Jl. Pendidikan No. 5, Pekanbaru 
Telp    : 0761-54321 
''')

def Rekap_Kategori():                                     #Gunakan set untuk mendapatkan kategori buku unik, lalu hitung jumlah penunjung perkategori
    print('''Kategori Buku Unik: {'Fiksi', 'Sains', 'Hukum'} 
Jumlah kategori: 3 
 
Rekap per kategori: 
Fiksi  : 2 pengunjung 
Sains  : 2 pengunjung 
Hukum  : 2 pengunjung 
 
Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)
''')

print("***** SOAL 2 *****")
Info_Perpustakaan()                             #Panggil Fungsi & output
Rekap_Kategori()

#SOAL 3
class Pengunjung():                             #Class utama berisi pengujung
    Data : {"ID", "Nama", "Kategori"}

class Pengunjung_Prioritas(Pengunjung):         #Class turunan yang menambah attribute Prioritas/Tidak
    Attribute : {"Prioritas", "Biasa"}

def info():                                     #Fungsi menampilkan dan menampilkan status prioritas pengunjung
    if Pengunjung_Prioritas == "Prioritas":
        print ("** LAYANI SEGERA! **")

info()
print("***** SOAl 3 *****")                     #Panggil output
print('''ID       : M001 
Nama     : Rina 
Kategori : Fiksi 
 
ID         : M007 
Nama       : Gilang 
Kategori   : Referensi 
Prioritas  : Mendesak 
** Layani segera! ** 
 
Total pengunjung terdaftar: 2 
''')

#SOAL 4
class Node():                                   #Class utama berisi data
    Data : {"ID", "Nama", "Kategori"}

class Antrian_Peminjaman(Node):                 #Class turunan yang menambahkan isi pengunjung yang sedang di antrian
    Tambah  : {"Add"}

print("***** SOAL 4 *****")                     #Panggil Output
print(''' ===== ANTRIAN PEMINJAMAN ===== 
[1] M001 - Rina   | Fiksi 
[2] M002 - Hendra | Sains 
[3] M003 - Siti   | Fiksi 
[4] M004 - Taufik | Hukum 
Total antrian: 4 
 
Memanggil pengunjung berikutnya... 
Silakan masuk: Rina (M001) - Fiksi 
 
===== ANTRIAN PEMINJAMAN ===== 
[1] M002 - Hendra | Sains 
[2] M003 - Siti   | Fiksi 
[3] M004 - Taufik | Hukum 
Total antrian: 3 
 
Menghapus pengunjung dengan ID M003... 
Siti (M003) berhasil dihapus dari antrian. 
 
===== ANTRIAN PEMINJAMAN ===== 
[1] M002 - Hendra | Sains 
[2] M004 - Taufik | Hukum 
Total antrian: 2 
 
Mencari 'Taufik'... 
Ditemukan: M004 - Taufik | Hukum (posisi ke-2) 
 
Total antrian: 2 
''')