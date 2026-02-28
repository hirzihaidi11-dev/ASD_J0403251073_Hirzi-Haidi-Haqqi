#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""): # -> n merupakan jumlah huruf pada setiap kombinasi dan hasil merupakan string kosong yang akan menampung
    if len(hasil) == n: # -> jika jumlah string == jumlah kombinasi huruf maka akan di print hasil
        print(hasil)
        return
    kombinasi(n, hasil + "A") # -> menambahkan huruf "A" ke string hasil dan menjelajahi(backtracing) semua kemungkinan yang diawali dengan "A"
    kombinasi(n, hasil + "B") # -> menambahkan huruf "B" ke string hasil dan menjelajahi(backtracing) semua kemungkinan yang diawali dengan "B"

kombinasi(2) # -> jumlah huruf pada setiap kombinasi adalah 2