from tabulate import tabulate
from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr

print("KONVERTER MATA UANG")

table = []
for kode, nilai in kurs.items():
    table.append([kode, nilai])

print(tabulate(table, headers=["Kode", "Kurs"], tablefmt="grid"))

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

if dari == "IDR":
    hasil = idr_ke_mata_uang(jumlah, ke)
    print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")

elif ke == "IDR":
    hasil = mata_uang_ke_idr(jumlah, dari)
    print(f"{jumlah} {dari} = Rp {hasil:,.0f}")

else:
    idr = mata_uang_ke_idr(jumlah, dari)
    hasil = idr_ke_mata_uang(idr, ke)
    print(f"{jumlah} {dari} = {hasil:.2f} {ke}")