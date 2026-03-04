#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 5. Melengkapi Fungsi Merge
#==============================================

def merge_sort(data):

    if len(data) <= 1:
        return data

    # Divide : membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data[:mid] # slicing bagian kiri
    right = data[mid:] # slicing bagian kanan

    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):

    result = []
    i = 0
    j = 0

    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result
angka = [1,8,4,3,5,2]
print("Hasil Sorting Ascending: ", merge_sort(angka))

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().
'''

'''
Jawaban:
2. Menambahkan sisa elemen yang ada setelah dipecah sehingga digabungkan menjadi 1 list yang sudah terurut dan memastikan agar tidak eleneb yang tertinggal
'''