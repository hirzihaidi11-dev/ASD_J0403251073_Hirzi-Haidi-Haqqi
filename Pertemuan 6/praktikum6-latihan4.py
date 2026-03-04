#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 4. Memahami Kode Program (Merge Sort)
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
'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''

'''
Jawaban:
1. Jika panjang data kurang dari sama dengan 1, maka nilai data di return karena dianggap sudah terurut dan rekursif akan dihentikan
2. Fungsi rekursif adalah untuk memecah menjadi bagian-bagian kecil, diawali dengan membagi 2 sebuah list, kemudian memecahnya kembali hingga ke dalam bentuk base case. singkatnya data dibagi menjadi 2 kemudian diurutkan dan terakhir digabungkan
3. Untuk menggabungkan bagian list kiri dan kanan yang sudah dipecah dan sudah diurutkan hingga menjadi 1 list kembali dan sudah ke dalam bentuk terurut
'''