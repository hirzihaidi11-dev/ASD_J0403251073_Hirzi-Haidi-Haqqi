#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
    }

# Fungsi Dijkstra untuk mencari jarak terpendek dari node start ke semua node lainnya
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga
    distances[start] = 0 # Jarak dari start ke start adalah 0
    priority_queue = [(0, start)] # Priority queue menyimpan pasangan (jarak, node)
    while priority_queue: # Selama masih ada node yang belum diproses
        current_distance, current_node = heapq.heappop(priority_queue) # Ambil node dengan jarak terkecil
        if current_distance > distances[current_node]: # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati
            continue
        for neighbor, weight in graph[current_node].items(): # Periksa semua tetangga dari node saat ini
            distance = current_distance + weight # Hitung jarak ke tetangga
            if distance < distances[neighbor]: # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
                distances[neighbor] = distance # Update jarak
                heapq.heappush(priority_queue, (distance, neighbor)) # Masukkan tetangga ke priority queue untuk diproses
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

'''
Pertanyaan:
1. Lokasi mana yang paling dekat dari Gerbang?
2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
'''
'''
Jawaban:
1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
3. Tidak selalu. Dalam kasus ini, jalur langsung dari Gerbang ke Aula tidak ada, sehingga jalur melalui Kantin
dan Lab menghasilkan waktu tempuh yang lebih kecil.
4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graf yang digunakan memiliki bobot
positif (waktu tempuh) dan tidak mungkin memiliki siklus negatif, dan algoritma ini efisien untuk mencari jarak terpendek dari satu titik ke semua titik
lainnya dalam graf berbobot positif.
'''