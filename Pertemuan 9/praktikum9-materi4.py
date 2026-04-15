#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 4: Membuat Traversal Inorder
#==============================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri
        self.right = None # Child kanan'

# Membuat Fungsi Inorder: Left ==> Root ==> Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Membuat Tree
# Membuat sebuah node pada root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal preorder
print("Hasil Travsersal Inorder:")
inorder(root)

"""
Pembahasan :

Dalam membuat node pada heaptree, hal yang harus dilakukan adalah membuat class node-nya.
Kemudian, buat node root dengan suatu nilai. Lalu, dalam menampilkan root, hal yang pertama
kali harus dilakukan adalah memuat data root. Root memiliki cabang yang bernama child,
child bisa berada di sisi kiri dan kanan root dengan memuat root.left dan root.right.

Pada kode ini akan ditampilkan heaptree dengan traversal Inorder. root,child level 1 berupa b dan c, dan child
level 2 berupa d,e,f,g. Dalam menampilkan nya diawali dengan root.left.left yaitu root(D), lalu menampilkan child kiri root 
yaitu B dengan root.left kemudian menampilkan child kanan dari B yaitu E dengan root.left.right. Kemudian menampilkan root yaitu (A) dengan root.data.
Kemudian menampilkan child kiri dari C yaitu F dengan root.right.left, lalu menampilkan child kanan dari root yaitu C dengan root.right lalu menampilkan
G dengan root.right.right.
"""