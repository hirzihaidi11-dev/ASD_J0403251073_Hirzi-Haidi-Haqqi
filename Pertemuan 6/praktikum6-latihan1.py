#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 1. Memahami Kode Program (Insertion Sort)
#==============================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key:
           data[j + 1] = data[j]
           j -= 1

        data[j + 1] = key

    return data

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

'''

'''
Jawaban:
1. Dikarenakan untuk pembandingan pertama kali adalah indeks ke-0 dan ke-1, jadi dapat dikatakan bahwasanya indeks ke-0 elemen yang akan dijadikan bahan perbandingan pertama kali dengan indeks ke-1 dan indeks ke-0 dianggap sudah terurut(kiri)
2. Dikarenakan key digunakan sebagai penyisipan angka yang ingin dimasukkan ke posisi(index) yang benar
3. Dikarenakan kita belum bisa mengetahui secara pasti jumlah perulangan yang akan dilakukan, jika menggunakan for kita harus mengetahui terlebih dahulu batas perulangan yang akan dilakukan
4. Pada operasi ini ketika kita ingin menempati key di index tertentu maka kita harus membandingkan key dengan index index sebelumnya, contoh ketika key pada index = 1 maka ia harus dibandingkan dengan index ke-0, jika key pada index = 2 maka ia harus dibandingkan dengan index ke 1 dan index ke 0 juga..
'''