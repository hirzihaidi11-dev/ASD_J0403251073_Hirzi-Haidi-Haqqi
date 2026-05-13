#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# =============================================
# Implementasi Sederhana Algoritma Kruskal
# =============================================

# Membuat Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
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

print("Total bobot =", total_weight)

'''
Pertanyaan :
1. Edge mana yang dipilih pertama kali?
2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
3. Berapa total bobot MST yang dihasilkan?
4. Mengapa edge tertentu tidak dipilih?

Jawaban :
1. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil, yaitu (C, D) dengan bobot 1.
2. Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma Kruskal bertujuan untuk
membangun MST dengan total bobot minimum, sehingga memilih edge dengan bobot terkecil pada setiap
langkahnya membantu mencapai tujuan tersebut.
3. Total bobot MST yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge (C, D) = 1, (A, C) = 2, 
dan (B, D) = 3.
4. Edge tertentu tidak dipilih karena sudah membentuk cycle sederhana dengan edge yang sudah 
dipilih sebelumnya, sehingga tidak sesuai dengan prinsip pembentukan MST.
'''