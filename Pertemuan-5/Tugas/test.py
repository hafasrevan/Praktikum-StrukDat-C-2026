class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_kendaraan(self, plat):
        baru = Node(plat)

        if self.head is None:
            self.head = baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = baru

    def sisipkan_vip(self, plat_baru, plat_target):
        current = self.head

        while current:
            if current.plat == plat_target:
                baru = Node(plat_baru)

                baru.next = current.next
                current.next = baru

                print(f"Kendaraan VIP {plat_baru} disisipkan setelah {plat_target}")
                return

            current = current.next

        print("Plat target tidak ditemukan dalam antrean.")

    def tampilkan_antrean(self):
        current = self.head

        if current is None:
            print("Antrean kosong")
            return

        while current:
            print(current.plat, end=" -> ")
            current = current.next
        print("None")


# Contoh penggunaan
antrean = LinkedList()

antrean.tambah_kendaraan("BM1111AA")
antrean.tambah_kendaraan("BM2222BB")
antrean.tambah_kendaraan("BM3333CC")

print("Antrean awal:")
antrean.tampilkan_antrean()

print("\nVIP masuk antrean")
antrean.sisipkan_vip("BMVIP01", "BM2222BB")

print("\nAntrean setelah VIP:")
antrean.tampilkan_antrean()