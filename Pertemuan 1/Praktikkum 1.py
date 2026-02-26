#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

###!!! Praktikkum 1 : Konsep ADT dan File Handling !!!###
#Latihan Dasar 1 : Membaca Seluruh Isi File
#-------------------------------------------------------#

#Membuka file dengan mode read ("r")
with open("Data_mahasiswa.txt","r",encoding="utf-8") as file :
    isi_file = file.read() #membaca file dengan satu script
print(isi_file)

print("===Hasil Read===")
print("Type Data", type(isi_file)) #menunjukkan tyoe data isi file
print("Jumlah Karakter", len(isi_file)) #jumlah karakter yang terdapat pada isi file
print("jumlah baris", isi_file.count("\n")+1) #jumlah baris yang terdapat pada isi file

#membuka file per baris
print("===Membaca File Per Baris===")
jumlah_baris = 0
with open("Data_mahasiswa.txt","r",encoding="utf-8") as file :
    for baris in file :
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru agar tidak ada tambahan karakter
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

###!!! Praktikkum 1 : Konsep ADT dan File Handling !!!###
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#-------------------------------------------------------#

with open("Data_mahasiswa.txt","r",encoding="utf-8") as file :
    for baris in file :
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter (,)
        print("NIM :", nim, "| Nama:", nama, "| Nilai:", nilai)

###!!! Praktikkum 1 : Konsep ADT dan File Handling !!!###
#Latihan Dasar 3 : Membaca File dan Menyimpan ke List
#-------------------------------------------------------#

data_list = [] #List untuk menampung data mahasiswa

with open("Data_mahasiswa.txt","r",encoding="utf-8") as file :
    for baris in file :
        baris = baris.strip()

        #Simpan Sebagai list "[nim,nama,nilai]"
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter (,)
        data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalam LIST ===")
print(data_list)

print("=== Jumlah Record dalam LIST ===")
print("Jumlah Record", len(data_list))

print("=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama:", data_list[0])

###!!! Praktikkum 1 : Konsep ADT dan File Handling !!!###
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary
#-------------------------------------------------------#

data_dict = {} #buat variabel untuk dictionary

with open("Data_mahasiswa.txt","r",encoding="utf-8") as file :
    for baris in file :
        baris = baris.strip()

        #Simpan Sebagai list "[nim,nama,nilai]"
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter (,)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai),
        }
print("===Data Mahasiswa dalam Dictionary")
print(data_dict)