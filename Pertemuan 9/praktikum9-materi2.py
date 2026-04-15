#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 2: Membuat Node
#==============================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri
        self.right = None # Child kanan

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

# Menampilkan isi node
print("Data pada root :", root.data)
print("Child kiri root :", root.left.data)
print("Child kanan root :", root.right.data)
print("Child kiri dari B :", root.left.left.data)
print("Child kanan dari B :", root.left.right.data)
print("Child kiri dari C :", root.right.left.data)
print("Child kanan dari C :", root.right.right.data)



"""
Pembahasan :

Dalam membuat node pada heaptree, hal yang harus dilakukan adalah membuat class node-nya.
Kemudian, buat node root dengan suatu nilai. Lalu, dalam menampilkan root, hal yang pertama
kali harus dilakukan adalah memuat data root. Root memiliki cabang yang bernama child,
child bisa berada di sisi kiri dan kanan root dengan memuat root.left dan root.right.

Pada kode ini akan ditampilkan heaptree yakni root,child level 1 berupa b dan c, dan child level 2 berupa d,e,f,g. Dalam
menampilkan nya diawali dengan root.data yaitu root(A), lalu pada child kiri root terdapat B dengan root.left
dan pada child kanan root terdapat C dengan root.right. Kemudian pada B(child level 1) memiliki 
child kiri berupa D dengan root.left.left dan child  kanan berupa E dengan root.left.right
(child level 2). Pada C(child level 1) memiliki child kiri berupa F dengan root.right.left dan 
child kanan berupa root.right.right(child level 2).
"""