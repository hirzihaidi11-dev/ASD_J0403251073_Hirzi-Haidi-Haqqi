#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Implementasi BFS
#==============================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections
from collections import deque

# Representasi Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # Graph: Dictionary yang menyimpan struktur dari graph
    # Start: Node awal untuk memulai penelusuran

    # Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque() 

    # Variabel yang digunakan untuk menyimpan node yang sudah diproses / dikunjungi
    visited = set()

    # Masukkan node awal ke dalam queue 
    queue.append(start)

    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan dari queue
        node = queue.popleft()

        # Tampilkan node yang sedang dikunjungi
        print(node, end = " ")

        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai tetangga sebagai node yang sudah dikunjungi
                visited.add(neighbor)
                 # Masukkan tetangga ke dalam queue 
                queue.append(neighbor)

# Menjalankan BFS mulai dari node 'A'
bfs(graph, 'A')