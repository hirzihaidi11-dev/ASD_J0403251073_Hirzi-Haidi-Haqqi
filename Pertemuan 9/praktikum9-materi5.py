#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 5: Membuat Traversal Postorder
#==============================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri
        self.right = None # Child kanan'

# Membuat Fungsi Postorder: Left ==> Right ==> Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

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
print("Hasil Travsersal postorder:")
postorder(root)

"""
Pembahasan :

Dalam membuat node pada heaptree, hal yang harus dilakukan adalah membuat class node-nya.
Kemudian, buat node root dengan suatu nilai. Lalu, dalam menampilkan root, hal yang pertama
kali harus dilakukan adalah memuat data root. Root memiliki cabang yang bernama child,
child bisa berada di sisi kiri dan kanan root dengan memuat root.left dan root.right.

Pada kode ini akan ditampilkan heaptree dengan traversal Postorder. root,child level 1 berupa b dan c, dan child
level 2 berupa d,e,f,g. Dalam menampilkan nya diawali dengan root.left.left yaitu root(D), lalu menampilkan child kanan dari B
yaitu E dengan root.left.right kemudian menampilkan child kiri root yaitu B dengan root.left. Kemudian menampilkan child kiri C yaitu
F dengan root.right.left dan menampilkan child kanan dari C yaitu G dengan root.right.right, kemudian menampilkan child kanan root
yaitu C dengan root.right, dan kembali ke root yaitu A.
"""