# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Materi Rekursif : Faktorial
# recursive case 3! = 3x2x1
# base case => 0 berhenti
# ==============================================

def faktorial(n):
    # BASE CASE -> ketika n bernilai == 0, rekursif dihentikan dan dikembalikan n bernilai == 1
    if n == 0:
        return 1
    # recursive case -> ketika n != 0 maka rekursif akan berlanjut dan bilangan n yang muncul akan disimpan dimemori, lalu dikalikan dengan dengan fungsi (n-1) begitu seterusnya hingga n == 0 maka akan kembali ke base case. jadi di memori tersimpan 3*2*1*1 sehingga menghasilkan output == 6
    return n*faktorial(n-1) # n*n-1*n-2*n-3.......n-?
print("===== Program Faktorial =====")
print("Hasil Faktorial :", faktorial(3)) 