# =======================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stock Barang Kantin (Berbasis File.txt)
#
# Nama : Hirzi Haidi Haqqi
# NIM  : J0403251073
# Kelas : TPL-B2
#========================================================

# ---------------------------------------
# Konstanta Nama File
# ---------------------------------------
nama_file="Stock_barang.txt"

# ---------------------------------------
# Fungsi: Membaca Data dari File
# ---------------------------------------

# Membaca data stock dari file teks
def baca_stock(nama_file):
    stock_dict = {} #Insisialisasi Data Dictionary

    with open(nama_file,"r",encoding="utf-8") as file :
         for baris in file:
            baris = baris.strip()
            kode, nama, stock = baris.split(",") #parsing data berdasarkan karakter (,)
            #Simpan Sebagai list "[kode,nama,stock]"
            stock_dict[kode] = {
                "nama" : nama,
                "stock" : int(stock)
            }
    return stock_dict

# ---------------------------------------
# Fungsi: Menyimpan Data ke File
# ---------------------------------------

def simpan_stock(nama_file,stock_dict):
    with open(nama_file,"w", encoding="utf-8") as file :
        for kode in sorted(stock_dict.keys()) :
            nama = stock_dict[kode]["nama"]
            stock = stock_dict[kode]["stock"]
            file.write(f"{kode},{nama},{stock}\n")
    print("Data Berhasil Disimpan")

# ---------------------------------------
# Fungsi: Menampilkan Semua Data
# ---------------------------------------

def tampilkan_semua(stock_dict):

    if len(stock_dict) == 0:
        print("Tidak ada data Barang")
        return

    #membuat Header Tabel
    print("==== Daftar Stock Barang ====")
    print(f"{"Kode" :<10} | {"Nama": <12} | {"Stock": >5}")
    print("-" * 32)
        
    for kode in sorted(stock_dict.keys()):
        nama=stock_dict[kode]["nama"]
        stock=stock_dict[kode]["stock"]
        print(f"{kode: <10} | {nama: <12} | {stock: >5}")

# ---------------------------------------
# Fungsi: Cari Barang Berdasarkan Kode
# ---------------------------------------

def cari_barang(stock_dict):
    #mencari data barang berdasarkan kode barang
    kode_cari = input("Masukkan Kode Barang yang dicari:").strip()

    if kode_cari in stock_dict:
        nama = stock_dict[kode_cari]["nama"]
        stock = stock_dict[kode_cari]["stock"]

        print("\n==== Data Stock Barang Ditemukan ====")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stock : {stock}")
    else :
        print("\n Data Tidak Ditemukan")

# ---------------------------------------
# Fungsi: Tambah Barang Baru
# ---------------------------------------

def tambah_barang(stock_dict):
    kode = input("Masukkan Kode Barang Baru (BRGXXX): ").strip()
    nama = input("Masukkan Nama Barang: ").strip()
    # Validasi kode tidak boleh duplikat
    if kode in stock_dict:
        print("Kode sudah digunakan. Penambahan dibatalkan.")
        return

    try:
        stock = int(input("Input Stock Awal: ").strip())
    except ValueError:
        print("Stock harus berupa angka.")
        return

    # simpan ke dictionary
    stock_dict[kode] = {
        "nama": nama,
        "stock": stock
    }

    print("Barang berhasil ditambahkan.")

# ---------------------------------------
# Fungsi: Update Stock Barang
# ---------------------------------------

def update_stock(stock_dict):
    kode = input("Masukkan Kode Barang yang akan diupdate stocknya:").strip()
    
    #cari kode barang yang akan diupdate stocknya
    if kode not in stock_dict :
        print("Kode Barang tidak ditemukan, update dibatalkan")
        return
    
    stock_lama = stock_dict[kode]["stock"]

    print("Pilih Jenis Update:")
    print("1. Tambah Stock")
    print("2. Kurangi Stock")

    pilihan =  input("Masukkan pilihan (1/2):").strip()
    try:
        jumlah = int(input("Masukkan Jumlah: ").strip())
    except ValueError: 
        print("Jumlah harus berupa angka. Update dibatalkan")
        return
    
    if pilihan == "1":
        stock_baru = stock_lama + jumlah
        print("Stock", kode, "anda sudah ditambahkan, stock awal:", stock_lama, "menjadi stock baru:", stock_baru)
    elif pilihan == "2":
        stock_baru = stock_lama - jumlah
        print("Stock", kode, "anda sudah dikurangi, stock awal:", stock_lama, "menjadi stock baru:", stock_baru)
    
    # Jika stock setelah diupdate menjadi negatif, maka update dibatalkan
    if stock_baru < 0:
        print("tetapi Stock tidak boleh negatif, Update dibatalkan")
        return
    
    # Memasukkan stock update baru ke dictionary
    stock_dict[kode]["stock"] = stock_baru

# ---------------------------------------
# Fungsi: Menghapus data barang
# ---------------------------------------

def hapus_barang(stock_dict):
    kode = input("Masukkan Kode Barang yang akan dihapus: ").strip()

    # Validasi kode ditemukan atau tidak
    if kode not in stock_dict:
        print("Kode barang tidak ditemukan.")
        return

    # Mengonfirmasi untuk melakukan penghapusan data
    konfirmasi = input(f"Yakin ingin menghapus {kode}? (y/n): ").lower()

    if konfirmasi == "y":
        del stock_dict[kode]
        print("Data barang berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

# ---------------------------------------
# Program Utama
# ---------------------------------------

def main():
    buka_data = baca_stock(nama_file)

    while True :
        print("\n=== MENU DATA STOCK BARANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode")
        print("3. Tambah Barang Baru")
        print("4. Update Stock Barang")
        print("5. Hapus Data Barang")
        print("6. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilihan Menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(buka_data)
        elif pilihan == "2":
            cari_barang(buka_data)
        elif pilihan == "3":
            tambah_barang(buka_data)
        elif pilihan == "4":
            update_stock(buka_data)
        elif pilihan == "5":
            hapus_barang(buka_data)
        elif pilihan == "6":
            simpan_stock(nama_file,buka_data)
        elif pilihan == "0":
            print("Anda sudah keluar dari Program, Program Selesai!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()