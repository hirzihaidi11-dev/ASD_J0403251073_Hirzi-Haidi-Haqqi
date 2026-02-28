# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# Masuk 1 - 2 - 3
# Keluar 
# ==============================================

def hitung(n):

    # BASE CASE -> ketika n bernilai == 0, maka rekursif akan berhenti dan mengirim pesan selesai 
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n) # -> menampilkan nilai n saat fungsi dipanggil 
    hitung(n-1) # recursive case -> memanggil fungsi nya sendiri dan akan mengurangi nilai n sebelumnya sebanyak 1. rekursi disimpan di call stack sehingga akan menggunakan konsep LIFO. setiap pemanggilan fungsi disimpan ke stack (push). saat fungsi selesai, ia dikeluarkan dari stack (pop)
    print("Keluar", n) 

print("===== Program Tracing =====")
hitung(5)