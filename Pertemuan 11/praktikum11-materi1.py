#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Implementasi Graph
#==============================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections
from collections import deque

# Representasi Graph
graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C'],
}

for node in graph:
    print(node, '->', graph[node])