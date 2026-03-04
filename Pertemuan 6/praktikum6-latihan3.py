#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 3. Tracing Insertion Sort
#==============================================

def insertion_sort(data):

    # Melihat data awal
    print("Data Awal:", data)
    print("="*50)

    # Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # Simpan nilai yang disisipkan
        j = i-1 # Index elemen terakhir di bagian kiri

        print("Iterasi ke-",i)
        print("Nilai key=", key)
        print("Bagian Kiri (terurut):", data[:i])
        print("Bagian Kanan (Belum terurut):", data[i:])

        # Geser 
        while j >=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # Sisipkan key ke posisi yang benar
        data[j+1] = key
        print("Setelah disisipkan :", data)
        print("-"*50)

    return data

angka = [5, 2, 4, 6, 1, 3]
print("Hasil Sorting :", insertion_sort(angka))

'''
Soal:
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]
Soal:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
'''

'''
1. isi list setelah iterasi i = 1 -> [2, 5, 4, 6, 1, 3]
2. isi list setelah iterasi i = 3 -> [2, 4, 5, 6, 1, 3]
3. terjadi 4 kali pergeseran pada i = 4, karena ada 4 angka di kiri yang lebih besar dari 1
'''