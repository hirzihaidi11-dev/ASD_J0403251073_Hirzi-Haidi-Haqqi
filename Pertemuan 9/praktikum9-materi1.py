#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 1: Membuat Node
#==============================================

# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri
        self.right = None # Child kanan
        
# Membuat sebuah node root
root = Node("A") # Membuat node root dengan nilai "A"

# Menampilkan isi node
print("Data pada root :", root.data)
print("Data Child kiri root :", root.left)
print("Data Child kanan root :", root.right)


"""
Pembahasan : 

Dalam membuat node pada heaptree, hal yang harus dilakukan adalah membuat class node-nya.
Kemudian, buat node root dengan suatu nilai. Lalu, dalam menampilkan root hal yang pertama
kali harus dilakukan adalah memuat data root. Root memiliki cabang yang bernama child,
child bisa berada di sisi kiri dan kanan root dengan memuat root.left dan root.right.
"""