data_aktivitas = [("Diki",88),("Aqul",45),("abid",92),("Rehan",70)]

for x,y in data_aktivitas:
    if y > 80:
        print (f"{x}, Mendapatkan predikat gold")

    elif y >= 50 and y <= 80:
        print (f"{x}, Mendapatkan predikat silver")

    else:
        print (f"{x}, Mendapatkan predikat bronze")