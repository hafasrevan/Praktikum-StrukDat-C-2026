class Stackclass:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.empty():
            print ("Stack kosong, tidak ada yang bisa dihapus :v")
            return None

    def peek(self):
        if self.is_empty():
            print ("Stack kosong")
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)


history = Stackclass()

history.push("Honkai Star Rail")
history.push("Wutherin Wave")
history.push("Punishing Gray Raven")

print("Stack: ", history.items)
print("Pop: ", history.pop())
print("Stack after Pop: ", history.items)
print("Peek: ", history.peek())
print("isEmpty: ", history.is_empty())
print("Size: ", history.size())
