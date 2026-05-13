#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# =============================================
# Implementasi Kruskal
# =============================================

# Membuat Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot yang telah ditentukan, urutkan berdasarkan bobot terkecil hingga terbesar
edges.sort()

# Inisialisasi MST dan total bobot, untuk menyimpan edge yang dipilih dan menghitung total bobot MST
mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()

# Iterasi melalui edge yang sudah diurutkan menggunakan algoritma Kruskal 
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana atau jika kedua node belum terhubung, maka tambahkan edge ke MST
    if u not in connected or v not in connected:
        mst.append((weight, u, v)) # Menambahkan edge ke MST
        total_weight += weight # Menambahkan bobot edge ke total bobot
        connected.add(u) # Menambahkan node u ke set connected
        connected.add(v) # Menambahkan node v ke set connected

print("Minimum Spanning Tree:")
# Menampilkan edge yang termasuk dalam MST beserta total bobotnya
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)