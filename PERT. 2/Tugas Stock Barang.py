###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 1 : Membuat Fungsi Load Data
#-------------------------------------------------------#

nama_file="Stock_barang.txt"

#membuat fungsi bacadata mahasiswa
def baca_data_barang(nama_file):
    data_dict = {} #Insisialisasi Data Dictionary

    with open(nama_file,"r",encoding="utf-8") as file :
         for baris in file:
            baris = baris.strip()
            kode, nama, stock = baris.split(",") #parsing data berdasarkan karakter (,)
            #Simpan Sebagai list "[nim,nama,nilai]"
            data_dict[kode] = {
                "nama" : nama,
                "stock" : int(stock)
            }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
# buka_data = baca_data_mahasiswa(nama_file)
# print("Jumlah data terbaca", len(buka_data))

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 2 : Membuat Fungsi Menampilkan Data
#-------------------------------------------------------#

def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Tidak ada data mahasiswa")
        return

    #membuat Header Tabel
    print("==== Daftar Stock Barang ====")
    print(f"({"Kode" :<10} | {"Nama": <12} | {"Stock": >5}")
    print("-" * 32)
    
    
    #Untuk tampilan yang rapi, atur f-string formatting
        

    for kode in sorted(data_dict.keys()):
        nama=data_dict[kode]["nama"]
        stock=data_dict[kode]["stock"]
        print(f"{kode: <10} | {nama: <12} | {stock: >5}")

#memanggil fungsi tampilkan_data
# tampilkan_data(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 3 : Membuat Fungsi Mencari Data
#-------------------------------------------------------#

def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
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

# cari_data(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 4 : Membuat Fungsi Update Nilai
#-------------------------------------------------------#

def update_stock(data_dict):
    kode = input("Masukkan Kode Barang yang akan diupdate stocknya").strip()
    
    #cari nim yang akan diupdate nilainya
    if kode not in data_dict :
        print("Kode Barang tidak ditemukan, update dibatalkan")
        return
    try:
        stock_baru = int(input("Masukkan Stock baru: ").strip())
    except ValueError: 
        print("Stock harus berupa angka. Update dibatalkan")
        return
    
    #if stock_baru < 0 or stock_baru >100 :
        #print("Nilharus diantara 0 sampai 100. Update dibatalkan")

    stock_lama = data_dict[kode]["stock"]
    #memasukkan nilai update baru ke dictionary
    data_dict[kode]["stock"] = stock_baru

    print(f"Update berhail. nilai {kode} berubah dari {stock_lama} menjadi {stock_baru}")

# update_nilai(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 5 : Membuat Fungsi Menyimpan perubahan data ke file
#-------------------------------------------------------#

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="utf-8") as file :
        for kode in sorted(data_dict.keys()) :
            nama = data_dict[kode]["nama"]
            stock = data_dict[kode]["stock"]
            file.write(f"{kode},{nama},{stock}\n")
            print("Data Berhasil Disimpan")

# simpan_data(nama_file, buka_data)
# print("Data Berhasil Disimpan")

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 6 : Membuat Menu Program
#-------------------------------------------------------#

def main():
    buka_data = baca_data_barang(nama_file)

    while True :
        print("\n=== MENU DATA STOCK BARANG ===")
        print("1. Tampilkan semua data")
        print("2. Cari Data Berdasarkan Kode Barang")
        print("3. Update Stock Barang")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilihan Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_stock(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data Stock Barang Tersimpan")
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()