daftar_barang = ["Apel", "Pisang", "Jeruk", "Melon"]
harga_barang = [10000, 15000, 30000, 40000]

belanjaan = []
while True:
    barang = input("Masukkan barang yang ingin dibeli: ")
    if barang.lower() == "bayar":
        break
    if barang in daftar_barang:
        belanjaan.append(barang)
    else:
        print("Barang tidak tersedia.")

total = 0.0
for item in belanjaan:
    index = daftar_barang.index(item)
    total += harga_barang[index]

print("Total belanja: Rp", total)

if total > 50000:
    print ("total belanja melebihi dari Rp.50000 anda mendapatkan gratis dua melon,total pembelian anda Rp.", total)
else :
    if total > 25000:
     total -= total *0.1
     print("total belanja melebihi Rp.25000 memenuhi syarat untuk diskon 10%.")
     print("Total setelah diskon: Rp", total)
