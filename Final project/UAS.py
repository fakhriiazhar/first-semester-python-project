import os

class barang:
    def __init__(self, nama, stok, harga, jenis):
        self.nama = nama 
        self.stok = stok
        self.harga = harga
        self.jenis = jenis 


    def __str__(self):
        return f"|| Nama Barang: {self.nama} || Stok: {self.stok} || Harga: {self.harga} || jenis: {self.jenis} ||\n"

def list_barang():
    if not os.path.exists('daftar_barang.txt'):
        print("File daftar_barang.txt belum ada.")
        return

    with open('daftar_barang.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Belum ada barang tersedia.")
        else:
            print("Daftar Barang Tersedia:")
            for barang_data in data:
                print(barang_data.strip())

def tambah_barang():    
    nama_barang = input("Masukkan nama barang: ")
    stok_barang = int(input("Masukkan jumlah stok barang: "))
    harga_barang = int(input("Masukkan harga barang: "))
    jenis_barang = input("masukan jenis barang:")
    with open('daftar_barang.txt', 'a') as file:
        file.write(f"|| Nama Barang: {nama_barang} || Stok: {stok_barang} || Harga : Rp.{harga_barang:,.2f} || jenis: {jenis_barang} ||\n")
    if stok_barang > 5 :
        print (f'{nama_barang} berhasil ditambahkan,stok mencukupi')
    elif stok_barang <= 5:
        print (f'{nama_barang} berhasil ditambahkan,stok kurang mencukupi')


def cari_barang(nama):
    found = False
    with open('daftar_barang.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Belum ada barang tersedia.")
        else:
            for barang_data in data:
                if f"Nama Barang: {nama}" in barang_data:
                    print(barang_data.strip())
                    found = True
                    break

    if not found:
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")

def update_stok(nama):
    found = False
    with open('daftar_barang.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Belum ada barang tersedia.")
        else:
            updated_data = []
            for barang_data in data:
                if f"Nama Barang: {nama}" in barang_data:
                    try:
                        jumlah_baru = int(input("Masukkan jumlah stok baru: "))
                        harga = int(input("Masukkan harga barang: "))
                        jenis = input("Masukkan jenis barang: ")
                        updated_data.append(f"|| Nama Barang: {nama} || Stok: {jumlah_baru} || harga : Rp.{harga:,.2f} || jenis : {jenis} \n")
                        found = True
                    except ValueError:
                         print("Input tidak valid. Harap masukkan angka.")
                         return
                else:
                    updated_data.append(barang_data)


            if found:
                with open('daftar_barang.txt', 'w') as file:
                    file.writelines(updated_data)
                print(f"stok {nama} berhasil diperbarui menjadi {jumlah_baru}.")
                if jumlah_baru <= 5:
                    print (f'stok {nama} berhasil di perbarui menjadi {jumlah_baru}, stok kurang mencukupi')
            else:
                print(f"Barang dengan nama '{nama}' tidak ditemukan.")

def hapus_barang(nama):
    found = False
    with open('daftar_barang.txt', 'r') as file:
        data = file.readlines()
        if not data:
            print("Belum ada barang dengan tersedia.")
        else:
            updated_data = []
            for barang_data in data:
                if f"Nama Barang: {nama}" in barang_data:
                    found = True
                else:
                    updated_data.append(barang_data)
            if found:
                with open('daftar_barang.txt', 'w') as file:
                    file.writelines(updated_data)
                print(f"{nama} berhasil dihapus.")
            else:
                print(f"Barang dengan nama '{nama}' tidak ditemukan.")

def filter_barang_sesuai_jenis(jenis_barang):
    found = False
    with open('daftar_barang.txt', 'r') as file:
        data = file.readlines()
        data_barang = [barang2.strip() for barang2 in data if f"jenis: {jenis_barang.lower()}" in barang2.lower()]
        if not data_barang:
            print(f"Tidak ada barang dengan jenis {jenis_barang}.")
        else:
            found = True
            print(f"Barang dengan jenis {jenis_barang}:")
            for barang in data_barang:
                print(barang)   
    return found

def main():
    while True:
        print("\n===== Manajemen pengelolaan barang Toko=====")
        print("1. Tambah Barang")
        print("2. List Nama Barang")
        print("3. Cari Barang")
        print("4. Update Stok Barang")
        print("5. Hapus barang")
        print("6. filter barang sesuai jenis")
        print("7. keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == '1' or pilihan.upper == 'TB' or pilihan.lower() == 'tb':
            tambah_barang()
        elif pilihan == '2' or pilihan.upper == 'LB'or pilihan.lower() == 'lb':
            list_barang()
        elif pilihan == '3' or pilihan.upper == 'CB'or pilihan.lower() == 'cb':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            cari_barang(nama_barang)
        elif pilihan == '4' or pilihan.upper() == 'USB' or pilihan.lower() == 'usb':
            nama_barang = input("Masukkan nama barang yang ingin diupdate stoknya: ")
            update_stok(nama_barang)    
        elif pilihan == '5' or pilihan.upper() == "HB" or pilihan.lower() == 'hb':
            nama_barang = input ("masukan barang yang ingin di hapus :")
            hapus_barang(nama_barang)
        elif pilihan == '6' or pilihan.upper() == 'FB'or pilihan.lower() == 'fb':
            jenis_barang = input("masukan jenis barang yang ingin di filter:")
            filter_barang_sesuai_jenis(jenis_barang)
        elif pilihan == '7' or pilihan.upper() == 'K' or pilihan.lower() == 'k':  
            print("terima kasih telah menggunakan aplikasi")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
