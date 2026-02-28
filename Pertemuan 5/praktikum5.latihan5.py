#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""): # -> panjang merupakan jumlah digit pin dan hasil merupakan string kosong yang akan menampung pin per digit
    if len(hasil) == panjang: # -> jika jumlah string == jumlah digit pin yang ditentukan maka akan dicetak satu kombinasi pin
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]: # -> perulangan untuk setiap kemungkinan digit 0,1,2
        buat_pin(panjang, hasil + angka) # -> menambahkan satu digit (angka) ke string hasil dan menjelajahi(backtracing) semua kemungkinan pin yang diawali digit tersebut

buat_pin(3) # -> membuat pin sebanyak 3 digit pada setiap kombinasi
