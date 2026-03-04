#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 2. Melengkapi Potongan Kode
#==============================================

# ascending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] 
            j -= 1

        data[j+1] = key
    return data

angka = [1,4,7,3,2]
print("Hasil Sorting Ascending ->", insertion_sort(angka))

'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending.
'''

# descending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j] 
            j -= 1

        data[j+1] = key
    return data

angka = [1,4,7,3,2]
print("Hasil Sorting Descending ->", insertion_sort(angka))