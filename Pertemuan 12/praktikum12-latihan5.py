#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# ==========================================
# Studi Kasus dengan Program Shortest Path
# ==========================================

graph = {
    "Bogor": {"Jakarta": 5, "Depok": 2},
    "Depok": {"Jakarta": 2, "Bandung": 6},
    "Jakarta": {"Bandung": 7},
    "Bandung": {}
}

def dijkstra(graph, start):
    # Menyimpan jarak terpendek dari start ke semua node
    distances = {node: float('inf') for node in graph}
    
    # Jarak ke node awal = 0
    distances[start] = 0
    
    # Menyimpan node yang sudah dikunjungi
    visited = set()
    
    while len(visited) < len(graph):
        # Pilih node dengan jarak terkecil yang belum dikunjungi
        current_node = None # Node dengan jarak terkecil
        current_distance = float('inf') # Jarak terkecil saat ini
        
        for node in graph: # Periksa semua node
            if node not in visited and distances[node] < current_distance: # Jika node belum dikunjungi dan jaraknya lebih kecil
                current_node = node # Update node dengan jarak terkecil
                current_distance = distances[node] # Update jarak terkecil
        
        # Jika tidak ada node tersisa, keluar
        if current_node is None:
            break
        
        # Tandai node sebagai sudah dikunjungi
        visited.add(current_node)
        
        # Update jarak ke tetangga
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            
            # Jika jarak baru lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

start_node = "Bogor"
hasil = dijkstra(graph, start_node)
print("Jarak terpendek dari", start_node, ":")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")

'''
Pertanyaan:
1. Node awal yang digunakan apa?
2. Node mana yang memiliki jarak paling kecil dari node awal?
3. Node mana yang memiliki jarak paling besar dari node awal?
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
'''
'''
Jawaban:
1. Node awal yang digunakan adalah "Bogor".
2. Node yang memiliki jarak paling kecil dari node awal adalah "Bogor" dengan jarak 0.
3. Node yang memiliki jarak paling besar dari node awal adalah "Bandung" dengan jarak 7.
4. Algoritma Dijkstra bekerja dengan cara memilih node dengan jarak terkecil yang belum dikunjungi,
kemudian memperbarui jarak ke tetangganya. Proses ini diulang hingga semua node telah dikunjungi,
sehingga menghasilkan jarak terpendek dari node awal ke semua node lainnya dalam graph. Pada kasus ini,
algoritma mulai dari "Bogor", kemudian memperbarui jarak ke "Jakarta" dan "Depok", lalu melanjutkan ke node 
dengan jarak terkecil berikutnya, hingga akhirnya mendapatkan jarak terpendek ke semua node dalam graph.
'''