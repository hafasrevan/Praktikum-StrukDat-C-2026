class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")

node1.next = node2
node2.next = node3
node3.next = None

antrean = LinkedList()
antrean.head = node1

print("Antrean awal:")
antrean.tampilkan_antrean()

print("\nVIP masuk antrean")
antrean.sisipkan_vip("B 2022 EFG", "D 8888 XYZ")

print("\nAntrean setelah VIP:")
antrean.tampilkan_antrean()