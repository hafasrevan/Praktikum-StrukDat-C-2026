class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def hapusKendaraan(self, plat):
        current = self.head
        prev = None

        while current is not None:
            if current.plat == plat:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                print(f"Kendaraan dengan plat {plat} dihapus dari antrean.")
                return

            prev = current
            current = current.next

        print("Kendaraan tidak ditemukan.")

    def tampilkanAntrean(self):
        current = self.head
        if current is None:
            print("Antrean kosong")
            return

        print("Antrean kendaraan:")
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
antrean.tail = node3

antrean.tampilkanAntrean()

print("\nAda kendaraan mogok...\n")
antrean.hapusKendaraan("B 2022 EFG") 
antrean.hapusKendaraan("D 8888 XYZ")  

antrean.tampilkanAntrean()