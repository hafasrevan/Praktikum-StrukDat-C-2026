class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(self, id_buku, judul):
    new_node = Node(id_buku, judul)

    if self.root is None:
        self.root = new_node
        return

    current = self.root

    while True:
        if id_buku < current.id:
            if current.left is None:
                current.left = new_node
                return
            current = current.left

        else:
            if current.right is None:
                current.right = new_node
                return
            current = current.right

def search(self, id_buku):
    current = self.root

    while current:
        if id_buku == current.id:
            return current
        elif id_buku < current.id:
            current = current.left
        else:
            current = current.right

    return None

def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(f"{node.id} - {node.judul}")
        self.inorder(node.right)

def get_min(self):
    current = self.root
    while current.left:
        current = current.left
    return current.id

def get_max(self):
    current = self.root
    while current.right:
        current = current.right
    return current.id

def height(self, node):
    if node is None:
        return -1

    left = self.height(node.left)
    right = self.height(node.right)

    return max(left, right) + 1

bst = BST()

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

print("\nInorder:")
bst.inorder(bst.root)

print("\nSearch 60:", bst.search(60).judul if bst.search(60) else "Tidak ditemukan")
print("Search 100:", "Ditemukan" if bst.search(100) else "Tidak ditemukan")

print("Min:", bst.get_min())
print("Max:", bst.get_max())
print("Height:", bst.height(bst.root))