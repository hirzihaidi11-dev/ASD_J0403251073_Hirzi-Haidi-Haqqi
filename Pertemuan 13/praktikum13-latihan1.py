#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]
print("Edge pada graph:")
# Menampilkan edge yang ada pada graph
for edge in edges:
    print(edge)
print("\nSpanning Tree:")
# Menampilkan edge yang termasuk dalam spanning tree
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

'''
Pertanyaan:
1. Apa perbedaan graph awal dan spanning tree?
2. Mengapa spanning tree tidak boleh memiliki cycle?
3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

Jawaban:
1. Graph awal memiliki 5 edge yang menghubungkan semua node, sedangkan spanning tree hanya memiliki 
3 edge yang menghubungkan semua node tanpa membentuk cycle.
2. Spanning tree tidak boleh memiliki cycle karena cycle akan menyebabkan pengulangan dalam koneksi
antara node, sehingga tidak efisien dan tidak memenuhi definisi spanning tree yang harus berupa pohon (tree).
3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya menghubungkan semua
node dengan jumlah edge minimum yang diperlukan, yaitu n-1 edge untuk n node, sedangkan graph awal bisa memiliki lebih banyak edge yang menghubungkan node secara langsung atau tidak langsung.
'''