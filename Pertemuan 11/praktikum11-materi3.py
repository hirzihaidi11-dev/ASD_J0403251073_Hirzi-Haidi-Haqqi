#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Implementasi DFS
#==============================================

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

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph menggunakan DFS
    # Graph: Dictionary yang menyimpan graph
    # Node: Menyimpan node yang sedang dikunjungi
    # Visited: Menyimpan node yang sudah dikunjungi 

    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end = " ")
    
    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
            
            # Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                    # Lakukan dfs secara rekursif ke tetangga tersebut
                    dfs(graph, neighbor, visited)

# Set Visited
visited = set()

# Menjalankan DFS mulai dari node A
dfs(graph, "A", visited)