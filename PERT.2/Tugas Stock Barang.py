###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 1 : Membuat Fungsi Load Data
#-------------------------------------------------------#

nama_file="Stock_barang.txt"

#membuat fungsi bacadata barang 
def baca_data_barang(nama_file):
    data_dict = {} #Insisialisasi Data Dictionary

    with open(nama_file,"r",encoding="utf-8") as file :
         for baris in file:
            baris = baris.strip()
            kode, nama, stock = baris.split(",") #parsing data berdasarkan karakter (,)
            #Simpan Sebagai list "[kode,nama,stock]"
            data_dict[kode] = {
                "nama" : nama,
                "stock" : int(stock)
            }
    return data_dict

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 2 : Membuat Fungsi Menampilkan Data
#-------------------------------------------------------#

def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Tidak ada data Barang")
        return

    #membuat Header Tabel
    print("==== Daftar Stock Barang ====")
    print(f"{"Kode" :<10} | {"Nama": <12} | {"Stock": >5}")
    print("-" * 32)
        
    for kode in sorted(data_dict.keys()):
        nama=data_dict[kode]["nama"]
        stock=data_dict[kode]["stock"]
        print(f"{kode: <10} | {nama: <12} | {stock: >5}")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 3 : Membuat Fungsi Mencari Data
#-------------------------------------------------------#

def cari_data(data_dict):
    #mencari data barang berdasarkan kode barang
    kode_cari = input("Masukkan Kode Barang yang dicari:").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stock = data_dict[kode_cari]["stock"]

        print("\n==== Data Stock Barang Ditemukan ====")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stock : {stock}")
    else :
        print("\n Data Tidak Ditemukan")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 4 : Membuat Fungsi Menambahkan Barang
#-------------------------------------------------------#

def tambah_data(data_dict):
    kode = input("Masukkan Kode Barang Baru (BRGXXX): ").strip()
    nama = input("Masukkan Nama Barang: ").strip()
    # cek apakah kode sudah ada
    if kode in data_dict:
        print("Kode sudah ada. Penambahan dibatalkan.")
        return

    try:
        stock = int(input("Masukkan Stock Barang: ").strip())
    except ValueError:
        print("Stock harus berupa angka.")
        return

    # simpan ke dictionary
    data_dict[kode] = {
        "nama": nama,
        "stock": stock
    }

    print("Barang berhasil ditambahkan.")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 5 : Membuat Fungsi Update Stock Barang
#-------------------------------------------------------#

def update_stock(data_dict):
    kode = input("Masukkan Kode Barang yang akan diupdate stocknya:").strip()
    
    #cari kode barang yang akan diupdate stocknya
    if kode not in data_dict :
        print("Kode Barang tidak ditemukan, update dibatalkan")
        return
    try:
        stock_baru = int(input("Masukkan Stock baru: ").strip())
    except ValueError: 
        print("Stock harus berupa angka. Update dibatalkan")
        return
    
    stock_lama = data_dict[kode]["stock"]
    #memasukkan stock update baru ke dictionary
    data_dict[kode]["stock"] = stock_baru

    print(f"Update berhail. stock {kode} berubah dari {stock_lama} menjadi {stock_baru}")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 6 : Membuat Fungsi Hapus Data Barang
#-------------------------------------------------------#

def hapus_data(data_dict):
    kode = input("Masukkan Kode Barang yang akan dihapus: ").strip()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan.")
        return

    # Mengonfirmasi untuk melakukan penghapusan data
    konfirmasi = input(f"Yakin ingin menghapus {kode}? (y/n): ").lower()

    if konfirmasi == "y":
        del data_dict[kode]
        print("Data barang berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 7 : Membuat Fungsi Menyimpan perubahan data ke file
#-------------------------------------------------------#

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="utf-8") as file :
        for kode in sorted(data_dict.keys()) :
            nama = data_dict[kode]["nama"]
            stock = data_dict[kode]["stock"]
            file.write(f"{kode},{nama},{stock}\n")
    print("Data Berhasil Disimpan")

###!!! Tugas Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Tahap 8 : Membuat Menu Program
#-------------------------------------------------------#

def main():
    buka_data = baca_data_barang(nama_file)

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
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            tambah_data(buka_data)
        elif pilihan == "4":
            update_stock(buka_data)
        elif pilihan == "5":
            hapus_data(buka_data)
        elif pilihan == "6":
            simpan_data(nama_file,buka_data)
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()