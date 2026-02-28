#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n): # -> n adalah angka awal hitung mundur
    if n == 0: # -> jika n sama dengan 0 akan menampilkan pesan selesai 
        print("Selesai")
        return
    print("Masuk:", n) # -> menampilkan nilai n saat fungsi dipanggil
    countdown(n - 1) # -> recursive case -> memanggil fungsi nya sendiri dan akan mengurangi nilai n sebelumnya sebanyak 1. rekursi disimpan di call stack sehingga akan menggunakan konsep LIFO. setiap pemanggilan fungsi disimpan ke stack (push). saat fungsi selesai, ia dikeluarkan dari stack (pop)
    print("Keluar:", n)
countdown(3) # -> countdown dimulai dari angka 3
