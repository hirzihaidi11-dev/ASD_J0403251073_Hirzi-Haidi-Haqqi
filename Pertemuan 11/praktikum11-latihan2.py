#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# Representasi Graph
graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': []
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph menggunakan DFS
    # Graph: Dictionary yang menyimpan graph
    # Node: Menyimpan node yang sedang dikunjungi
    # Visited: Menyimpan node yang sudah dikunjungi 

    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")
    
    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

         # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Set Visited
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

'''
Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
2. Apa yang terjadi jika urutan neighbor diubah?
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

Jawaban:
1. DFS masuk ke node terdalam terlebih dahulu karena ia menggunakan pendekatan rekursif atau stack untuk
menyimpan node yang akan dikunjungi selanjutnya, sehingga ia akan terus menjelajahi satu jalur hingga
mencapai ujungnya 'E' sebelum kembali dan menjelajahi jalur lainnya 'C'.
2. Jika urutan neighbor diubah, maka urutan kunjungan node dalam DFS juga akan berubah. 
Misalnya, jika kita mengubah urutan neighbor 'B' dan 'C' pada node 'A', maka DFS akan mengunjungi 'C'
terlebih dahulu sebelum 'B', lalu ia akan ke 'F' sehingga menghasilkan urutan kunjungan yang berbeda.
3. Hasil DFS dan BFS pada graph yang sama akan berbeda karena DFS menjelajahi satu jalur hingga selesai
sebelum kembali, sedangkan BFS menjelajahi semua tetangga pada level yang sama sebelum melanjutkan
ke tingkat berikutnya. Misalnya, pada graph di atas, DFS akan menghasilkan urutan kunjungan
A -> B -> D -> E -> C -> F, sedangkan BFS akan menghasilkan urutan kunjungan A -> B -> C -> D -> E -> F.
'''