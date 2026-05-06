#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Algoritma Dijkstra
#==============================================

import heapq
# Weighted graph dengan bobot positif
graph = {
'A': {'B': 4, 'C': 2},
'B': {'D': 5},
'C': {'D': 1},
'D': {}
}

# Fungsi Dijkstra
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)] 
    while pq: # Selama masih ada node yang belum diproses
        current_distance, current_node = heapq.heappop(pq) # Ambil node dengan jarak terkecil
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight # Hitung jarak ke tetangga
            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]: # Update jarak dan masukkan ke priority queue
                distances[neighbor] = distance # Update jarak
                heapq.heappush(pq, (distance, neighbor)) # Masukkan ke priority queue
    return distances # Kembalikan jarak minimum ke semua node

hasil = dijkstra(graph, 'A')
print(hasil)