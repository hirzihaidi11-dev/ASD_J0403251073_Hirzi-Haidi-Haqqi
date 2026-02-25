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
    # BASE CASE
    if n == 0:
        return 1
    # recursive case
    return n*faktorial(n-1) # n*n-1*n-2*n-3.......n-?
print("===== Program Faktorial =====")
print("Hasil Faktorial :", faktorial(3)) 