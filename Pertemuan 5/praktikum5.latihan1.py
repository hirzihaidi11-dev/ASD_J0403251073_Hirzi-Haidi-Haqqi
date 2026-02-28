#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n): # -> a merupakan basis dan b merupakan eksponen (jumlah pangkat)
 # Base case -> jika pangkat == 0 maka dikembalikan nilai 1
    if n == 0:
        return 1
 # Recursive case -> mengalikan nilai a dengan hasil fungsi pangkat(a, n-1) maka pangkat dihitung berulang kali secara rekursif
    return a * pangkat(a, n - 1) 
print(pangkat(2, 4))