#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Algoritma Bellman Ford
#==============================================

# Representasi graph dengan bobot negatif
graph = {
'A': {'B': 5, 'C': 4},
'B': {},
'C': {'B': -2},
}

# Fungsi Bellman-Ford
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga
    distances[start] = 0 # Jarak dari start ke start adalah 0
    
    # Relaksasi berulang
    for _ in range(len(graph) - 1): # Lakukan relaksasi sebanyak jumlah node - 1
        for node in graph: # Periksa semua edge
            for neighbor, weight in graph[node].items(): # Jika jarak ke node saat ini sudah diketahui, dan ditemukan jarak yang lebih kecil ke neighbor, maka lakukan update jarak
                if distances[node] + weight < distances[neighbor]: # Update jarak
                    distances[neighbor] = distances[node] + weight # Update jarak
    return distances # Kembalikan jarak minimum ke semua node

hasil = bellman_ford(graph, 'A')
print(hasil)