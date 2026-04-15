#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 6: Struktur Organisasi Perusahaan
#==============================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri
        self.right = None # Child kanan'

# Fungsi Preorder : Root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Membuat tree struktur organisasi
root = Node("Direktur")

# Membuat child level 1
root.left = Node("Manager A")
root.right = Node("Manager B")

# Membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

# Membuat child level 2
root.right.left = Node("Staff 3")
root.right.right = Node("Staff 4")

# Menjalankan traversal preorder
print("Struktur Organisasi (preorder):")
preorder(root)

"""
Pembahasan :

Dalam membuat node pada heaptree, hal yang harus dilakukan adalah membuat class node-nya.
Kemudian, buat node root dengan suatu nilai. Lalu, dalam menampilkan root, hal yang pertama
kali harus dilakukan adalah memuat data root. Root memiliki cabang yang bernama child,
child bisa berada di sisi kiri dan kanan root dengan memuat root.left dan root.right.

Pada kode ini akan ditampilkan Struktur Organisasi Perusahaan dengan traversal preoder. Direktur,child level 1 berupa Manajer A dan B,
dan child level 2 berupa staff 1,2,3, dan 4. Dalam menampilkan nya diawali dengan root.data yaitu Direktur, lalu child kiri root 
terdapat Manajer A dengan root.left kemudian child kiri dari Manajer A yaitu Staf 1 dengan root.left.left dan Staf 2 dengan root.left.right(kanan).
Kemudian menampilkan child kanan root yaitu Manajer B dengan root.right, lalu menampilkan child kiri dari Manajer B yaitu Staf 3 dengan 
root.right.left dan Staf 4 dengan root.right.right(kanan).
"""