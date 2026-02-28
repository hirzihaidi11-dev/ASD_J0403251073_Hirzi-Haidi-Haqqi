#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ========================================================== 
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ========================================================== 

def biner_batas(n, batas, hasil="", jumlah_1=0): # -> n merupakan panjang biner, batas merupakan jumlah maks angka 1 yang boleh muncul, hasil merupakan string kosong yang akan menampung, jumlah_1 merupakan jumlah angka 1 yang muncul diawal = 0
    # Pruning -> jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: 
        return 
    # Base case 
    if len(hasil) == n: # jika panjang string biner hasil sudah sama dengan n maka kombinasi biner akan diprint
        print(hasil) 
        return 
    # Pilih '0' -> menambahkan string '0' dan jumlah_1 tidak akan bertambah (tetap)
    biner_batas(n, batas, hasil + "0", jumlah_1)
    # Pilih '1' -> menambahkan string '1' dan jumlah_1 akan bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) 

biner_batas(4, 2) # -> menentukan panjang biner = 4 dan maks muncul string '1' adalah 2