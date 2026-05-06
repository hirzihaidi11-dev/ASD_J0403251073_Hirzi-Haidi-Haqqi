#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
'A': {'B': 5, 'C': 4},
'B': {},
'C': {'B': -2}
}

# Fungsi Bellman-Ford
def bellman_ford(graph, start):
    '''
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    '''
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0    
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph: 
            for neighbor, weight in graph[node].items():
            # Jika jarak ke node saat ini sudah diketahui,
            # dan ditemukan jarak yang lebih kecil ke neighbor,
            # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: # Update jarak
                    distances[neighbor] = distances[node] + weight 
    return distances
hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)  

'''
Pertanyaan:
1. Berapa bobot langsung dari A ke B?
2. Berapa total bobot jalur A -> C -> B?
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
5. Apa yang dimaksud dengan proses relaksasi edge?
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
'''
'''
Jawaban:
1. Bobot langsung dari A ke B adalah 5.
2. Total bobot jalur A -> C -> B adalah 4 + (-2) = 2.
3. Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B (total 2) dibandingkan jalur langsung A -> B (total 5).
4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini melakukan relaksasi
edge secara berulang, sehingga dapat menangani perubahan jarak yang disebabkan oleh bobot negatif.
5. Proses relaksasi edge adalah proses di mana algoritma memeriksa apakah jarak ke suatu node melalui edge
tertentu lebih kecil daripada jarak yang sudah tercatat. Jika ya, maka jarak tersebut diperbarui.
6. Perbedaan utama Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat mengeksekusi graph dengan bobot
negatif, sedangkan Dijkstra tidak dapat. Selain itu, Dijkstra menggunakan priority queue untuk memilih node
dengan jarak terkecil, sementara Bellman-Ford melakukan relaksasi edge secara berulang tanpa menggunakan
priority queue. Bellman-Ford memiliki kompleksitas waktu O(V * E), sedangkan Dijkstra dengan priority 
queue memiliki kompleksitas O((V + E) log V). Bellman-Ford juga dapat mendeteksi adanya siklus negatif, 
sedangkan Dijkstra tidak dapat. 
'''