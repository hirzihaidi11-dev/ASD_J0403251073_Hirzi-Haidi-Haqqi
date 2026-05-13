#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# =============================================
# Implementasi Prim
# =============================================

# Import heapq untuk menggunakan priority queue dalam algoritma Prim
import heapq 
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi untuk mengimplementasikan algoritma Prim untuk mencari Minimum Spanning Tree (MST) dari sebuah graph yang diberikan dengan menggunakan priority queue untuk memilih edge dengan bobot terkecil pada setiap langkahnya
def prim(graph, start):
    # Inisialisasi set visited untuk melacak node yang sudah dikunjungi, dan priority queue untuk menyimpan edge yang akan diproses berdasarkan bobotnya
    visited = set([start])
    # Inisialisasi list untuk menyimpan edge yang termasuk dalam MST dan variabel untuk menghitung total bobot MST
    edges = []

    # Menambahkan semua edge yang terhubung dengan node awal ke dalam priority queue berdasarkan bobotnya
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor)) # Menambahkan edge ke priority queue dengan format (bobot, node1, node2)

    # Proses utama algoritma Prim, mengambil edge dengan bobot terkecil dari priority queue dan menambahkannya ke MST jika node yang terhubung belum dikunjungi, serta menambahkan edge baru yang terhubung dengan node yang baru saja ditambahkan ke MST ke dalam priority queue untuk diproses selanjutnya
    mst = []
    # Variabel untuk menyimpan total bobot MST
    total_weight = 0

    # Loop utama untuk membangun MST dengan terus mengambil edge dengan bobot terkecil dari priority queue hingga semua node terhubung dalam MST
    while edges:
        weight, u, v = heapq.heappop(edges) # Mengambil edge dengan bobot terkecil dari priority queue
        if v not in visited: # Jika node v belum dikunjungi, maka tambahkan edge ke MST dan update total bobot serta tambahkan node v ke set visited
            visited.add(v) # Menambahkan node v ke set visited
            mst.append((u, v, weight)) # Menambahkan edge ke MST dengan format (node1, node2, bobot)
            total_weight += weight # Menambahkan bobot edge ke total bobot MST
            for neighbor, w in graph[v].items(): # Menambahkan semua edge yang terhubung dengan node v ke dalam priority queue untuk diproses selanjutnya
                if neighbor not in visited: # Hanya menambahkan edge yang terhubung dengan node yang belum dikunjungi ke dalam priority queue
                    heapq.heappush(edges, (w, v, neighbor)) # Menambahkan edge ke priority queue dengan format (bobot, node1, node2)
    return mst, total_weight  # Mengembalikan MST yang dibangun dan total bobotnya

# Memanggil fungsi prim dengan graph yang telah didefinisikan dan node awal 'A' untuk mendapatkan MST dan total bobotnya
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

# Menampilkan edge yang termasuk dalam MST beserta total bobotnya
for edge in mst:
    print(edge)

print("Total bobot =", total)