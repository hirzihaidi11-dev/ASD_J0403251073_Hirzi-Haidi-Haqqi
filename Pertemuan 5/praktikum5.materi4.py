#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 

def biner(n, hasil=""): # -> n adalah panjang biner, hasil string kosong yang akan menampung
    # Base case -> jika panjang string sudah sama dengan n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) # -> jika kondisi terpenuhi, program mencetak satu kombinasi biner dengan konsep 2^n
        return
    
    # Choose + Explore -> tambah '0' 
    biner(n, hasil + "0") # -> memanggil fungsi biner kembali dengan menambahkan karakter '0' ke string hasil
    
    # Choose + Explore -> tambah '1' 
    biner(n, hasil + "1") # -> memanggil fungsi biner kembali dengan menambahkan karakter '1' ke string hasil
    
biner(3) # -> menentukan panjang biner