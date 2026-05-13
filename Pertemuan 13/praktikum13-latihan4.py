#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# Membuat Daftar edge: (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil hingga bobot terbesar
edges.sort()

# Inisialisasi MST dan total bobot, untuk menyimpan edge yang dipilih dan menghitung total bobot MST
mst = []
# Inisialisasi total bobot MST
total_weight = 0
# Set sederhana untuk node yang sudah terhubung dalam MST
connected = set()

# Iterasi melalui edge yang sudah diurutkan menggunakan algoritma Kruskal
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: # Jika salah satu node belum terhubung, maka edge ini dapat dipilih untuk MST
        mst.append((u, v, weight)) # Menambahkan edge ke MST dengan format (node1, node2, bobot)
        total_weight += weight # Menambahkan bobot edge ke total bobot MST

        connected.add(u) # Menambahkan node u ke set connected
        connected.add(v) # Menambahkan node v ke set connected

print("Minimum Spanning Tree:")
# Menampilkan edge yang termasuk dalam MST beserta total bobotnya
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)

'''
Pertanyaan:
1. Algoritma apa yang digunakan?
2. Edge mana saja yang dipilih?
3. Berapa total biaya minimum?
4. Mengapa MST cocok digunakan pada kasus ini?

Jawaban:
1. Algoritma yang digunakan adalah algoritma Kruskal.
2. Edge yang dipilih adalah (GedungC, GedungD, 1), (GedungA, GedungC, 2), dan (GedungB, GedungD, 3).
3. Total biaya minimum adalah 6, yang merupakan jumlah dari bobot edge (GedungC, GedungD) = 1,
(GedungA, GedungC) = 2, dan (GedungB, GedungD) = 3.
4. MST cocok digunakan pada kasus ini karena kita ingin menghubungkan semua gedung dengan biaya
minimum tanpa membentuk siklus, sehingga MST memberikan solusi optimal untuk masalah ini.
'''