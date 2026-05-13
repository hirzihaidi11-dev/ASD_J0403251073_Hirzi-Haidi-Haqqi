#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# Membuat Daftar edge: (bobot, node1, node2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
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

print("Total bobot minimum =", total_weight)

'''
Pertanyaan:
1. Kasus apa yang dipilih?
2. Algoritma apa yang digunakan?
3. Edge mana saja yang dipilih dalam MST?
4. Berapa total bobot MST?
5. Mengapa edge tertentu tidak dipilih?

Jawaban:
1. Kasus 1: Jaringan Jalan Antar Kota
2. Algoritma yang digunakan adalah algoritma Kruskal
3. Edge yang dipilih dalam MST adalah: (Bogor, Depok, 2), (Depok, Jakarta, 3), (Jakarta, Bandung, 6)
4. Total bobot MST adalah 11
5. Edge (Depok, Bandung, 4) tidak dipilih karena sudah ada jalan yang lebih minimum (melalui Jakarta)
untuk menghubungkan Depok dan Bandung
'''