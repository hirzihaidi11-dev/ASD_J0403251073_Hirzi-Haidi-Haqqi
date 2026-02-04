###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 1 : Membuat Fungsi Load Data 
#-------------------------------------------------------#

nama_file="Data_mahasiswa.txt"

#membuat fungsi bacadata mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} #Insisialisasi Data Dictionary

    with open(nama_file,"r",encoding="utf-8") as file :
         for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter (,)
            #Simpan Sebagai list "[nim,nama,nilai]"
            data_dict[nim] = {
                "nama" : nama,
                "nilai" : int(nilai)
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
    print("==== Daftar Mahasiswa====")
    print(f"({"NIM" :<10} | {"Nama": <12} | {"Nilai": >5}")
    print("-" * 32)
    
    
    #Untuk tampilan yang rapi, atur f-string formatting
        

    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

#memanggil fungsi tampilkan_data
# tampilkan_data(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 3 : Membuat Fungsi Mencari Data
#-------------------------------------------------------#

def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang dicari:").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"Nim : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else :
        print("\n Data Tidak Ditemukan")

# cari_data(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 4 : Membuat Fungsi Update Nilai
#-------------------------------------------------------#

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya").strip()
    
    #cari nim yang akan diupdate nilainya
    if nim not in data_dict :
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError: 
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru >100 :
        print("Nilai harus diantara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    #memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhail. nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(buka_data)

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 5 : Membuat Fungsi Menyimpan perubahan data ke file
#-------------------------------------------------------#

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w", encoding="utf-8") as file :
        for nim in sorted(data_dict.keys()) :
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
            print("Data Berhasil Disimpan")

# simpan_data(nama_file, buka_data)
# print("Data Berhasil Disimpan")

###!!! Praktikkum 2 : Konsep ADT dan File Handling(Studi Kasus) !!!###
#Latihan Dasar 6 : Membuat Menu Program
#-------------------------------------------------------#

def main():
    buka_data = baca_data_mahasiswa(nama_file)

    while True :
        print("\n=== MENU DATA MAHASISWA ")
        print("1. Tampilkan semua data")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilihan Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data Mahasiswa Tersimpan")
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()