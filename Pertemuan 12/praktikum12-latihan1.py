#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
'A': {'B': 4, 'C': 2},
'B': {'D': 5},
'C': {'D': 1},
'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
if jalur_1 < jalur_2: # Jika jalur 1 lebih pendek
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

'''
Pertanyaan:
1. Berapa total bobot jalur A -> B -> D? 
2. Berapa total bobot jalur A -> C -> D?
3. Jalur mana yang dipilih sebagai jalur terpendek?
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
'''

'''
jawaban:
1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
3. Jalur terpendek adalah A -> C -> D karena memiliki total bobot yang lebih kecil (3) dibandingkan dengan jalur
A -> B -> D yaitu total bobot 9.
4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena bobot pada setiap edge
dapat berbeda. Sebuah jalur dengan lebih banyak edge bisa memiliki total bobot yang lebih kecil jika bobot
pada edge tersebut lebih kecil dibandingkan dengan jalur yang memiliki lebih sedikit edge tetapi bobotnya
lebih besar.
'''