# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Materi Rekursif : Menjumlahkan elemen list
# ==============================================

def jumlah_list(data, index=0): # data menunjukkan sebagai list dan mengatur nilai awal index = 0
    # BASE CASE
    if index == len(data): # mengecek apakah index sudah sama dengan panjang list, berarti semua elemen sudah diproses jika sudah semua maka fungsi akan mengembalikan nilai 0.
        return 0
    
    # recursive case # -> mengambil nilai elemen pada posisi index lalu, menjumlahkannya dengan hasil pemanggilan fungsi berikutnya kemudian, pindah ke elemen selanjutnya.
    return data[index] + jumlah_list(data, index+1)

print("===== Program Jumlah Data =====")
print(jumlah_list([2,4,5]))