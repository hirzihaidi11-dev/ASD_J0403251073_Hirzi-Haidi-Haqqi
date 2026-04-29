#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections
from collections import deque

# Representasi Graph
graph = {
'Rumah': ['Sekolah', 'Toko'],
'Sekolah': ['Perpustakaan'],
'Toko': ['Pasar'],
'Perpustakaan': [],
'Pasar': []
}

# Fungsi untuk melakukan penelusuran graph menggunakan BFS
def bfs(graph, start):
    # Menyimpan node yang sudah dikunjungi
    visited = set() 

    # Menyimpan node yang sudah dikunjungi
    queue = deque([start])

    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    # Lakukan BFS hingga antrian kosong
    while queue:
        # Ambil node dari antrian
        node = queue.popleft()
        print(node, end=" ")

        # Periksa semua tetangga dari node saat ini
        for neighbor in graph[node]:
            # Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                # Tandai tetangga sebagai node yang sudah dikunjungi
                visited.add(neighbor)
                # Tambahkan tetangga ke antrian untuk dikunjungi selanjutnya
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

'''
Pertanyaan Analisis
1. Node mana yang dikunjungi pertama?
2. Mengapa BFS cocok untuk mencari jalur terdekat?
3. Apa perbedaan urutan BFS jika struktur graph diubah?

Jawaban:
1. Node yang dikunjungi pertama adalah 'Rumah', karena itulah titik awal dari penelusuran
BFS ketika queue masih kosong.
2. BFS cocok untuk mencari jalur terdekat karena ia menjelajahi semua tetangga pada tingkat
yang sama sebelum melanjutkan ke tingkat berikutnya, sehingga memastikan bahwa jalur terdekat
ditemukan terlebih dahulu.
3. Jika struktur graph diubah, urutan BFS dapat berubah tergantung pada bagaimana node dan tetangga diatur.
Misalnya, jika 'Sekolah' dan 'Toko' ditukar dalam daftar tetangga 'Rumah', maka BFS akan mengunjungi
'Toko' sebelum 'Sekolah', sehingga mengubah urutan kunjungan node.
'''