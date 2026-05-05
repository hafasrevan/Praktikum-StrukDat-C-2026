class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top is None

    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa pop.")
            return None
        popped_url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return popped_url

    def peek(self):
        if self.is_empty():
            print("Stack kosong.")
            return None
        return self.top.url

    def size(self):
        return self.count
    
history = StackLinkedList()

history.push("Honkai Star Rail")
history.push("Wutherin Wave")
history.push("Punishing Gray Raven")

print("Halaman saat ini:", history.peek())
history.pop()
print("Setelah back:", history.peek())
print("Jumlah riwayat:", history.size())