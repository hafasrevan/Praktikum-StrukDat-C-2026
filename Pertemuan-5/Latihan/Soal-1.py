Stok_Barang = [15,40,30,10,25]
Stok_Barang.pop (3)
Stok_Barang.insert (3, 50)
Stok_Barang.append (5)

print(Stok_Barang)

Stok_Barang.sort (reverse=True)

print(Stok_Barang)


print (sum (Stok_Barang)/len(Stok_Barang))
if sum(Stok_Barang)/len(Stok_Barang) > 20:
    print ("Stok aman")
else :
    print ("Waspada")

print("stok aman") if sum(Stok_Barang)/len(Stok_Barang) > 20 else "waspada"