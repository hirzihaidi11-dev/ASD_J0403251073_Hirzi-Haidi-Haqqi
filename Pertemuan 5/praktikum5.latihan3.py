#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0): # -> data merupakan list yang berisi angka dan index dimulai dari 0
    # Base case -> jika index sudah sama dengan panjang list - 1 (sudah di elemen terakhir), fungsi mengembalikan nilai elemen tersebut sebagai nilai maksimum sementara
    if index == len(data) - 1:
        return data[index]
    # Recursive case -> memanggil fungsi secara rekursif untuk mencari nilai maksimum dari sisa elemen (mulai dari index berikutnya sampai index = panjang list - 1)
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa: # -> membandingkan nilai pada posisi index saat ini dengan nilai maksimum dari sisa list. jika nilai saat ini lebih besar, maka nilai ini dikembalikan sebagai maksimum. jika lebih kecil,maka mengembalikan nilai maksimum dari sisa elemen list
        return data[index]
    else:
        return maks_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
