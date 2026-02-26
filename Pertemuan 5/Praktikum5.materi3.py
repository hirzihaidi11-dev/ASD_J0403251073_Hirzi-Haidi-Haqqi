# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Materi Rekursif : Menjumlahkan elemen list
# ==============================================

def jumlah_list(data, index=0):
    # BASE CASE
    if index == len(data):
        return 0
    
    # recursive case
    return data[index] + jumlah_list(data, index+1)

print("===== Program Jumlah Data =====")
print(jumlah_list([2,4,5]))