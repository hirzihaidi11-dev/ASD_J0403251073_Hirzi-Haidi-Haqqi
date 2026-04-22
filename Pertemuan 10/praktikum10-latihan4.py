#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 4: BST
#==============================================

# Class Node untuk menyimpan data BST
class Node: # Class Node digunakan untuk dasar dari tree
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi insert untuk BST
''' Alur Fungsi Insert pada BST diawali dengan membaca apakah root kosong atau tidak, jika kosong maka nilai
yang dimasukkan menjadi node baru dengan nilai (data), lalu node itu dijadikan root. Ketika data yang dimasukkan
lebih kecil dari root maka akan dijadikan sebagai child kiri root (subtree kiri) jika sebaliknya maka data dijadikan sebagai
child kanan root (subtree kanan).
'''
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi preorder untuk melihat bentuk tree
''' Alur Fungsi Preorder pada BST diawali dengan membaca root tidak kosong, kemudian cetak data, 
lalu membaca child kiri, dan membaca child kanan (konsep preorder).
'''
def preorder(root):
    if root is not None: # Jika root tidak kosong
        print(root.data, end=" ") # Mencetak data pada node saat ini
        preorder(root.left) # Baca Child kiri
        preorder(root.right) # Baca Child kanan

# Fungsi sederhana untuk menampilkan struktur tree
''' Alur Fungsi tampil_struktur pada BST diawali dengan membaca root tidak kosong dan level dimulai dari 0,
kemudian cetak posisi(level) dan data, lalu membaca root kiri dengan level bertambah 1 dan posisi "L", dan
membaca root kanan dengan level bertambah 1 dan posisi "R".
'''
def tampil_struktur(root, level=0, posisi="Root"): # Fungsi untuk menampilkan struktur tree dengan indentasi berdasarkan level
    if root is not None: # Jika root tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # Cetak posisi dan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") # Baca Child kiri dengan level bertambah 1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R") # Baca Child kanan dengan level bertambah 1 dan posisi "R"


# -----------------------------
# Program utama
# -----------------------------
root = None
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]
for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

''' Pembahasan:
1. Alasan mengapa tree condong ke kanan adalah karena data dimasukkan secara berurutan naik (10, 20, 30),
sehingga setiap nilai baru lebih besar dari nilai sebelumnya, menyebabkan node baru selalu menjadi child kanan
dari node sebelumnya. Akibatnya, tree menjadi tidak seimbang dan condong ke kanan.
2. Mengapa semakin panjang tree, maka pencarian bisa makin lambat? karena dalam kasus terburuk
(seperti pada tree yang condong ke kanan), struktur tree menyerupai linked list, sehingga pencarian harus 
melewati setiap node satu per satu, yang menyebabkan waktu pencarian menjadi O(n) dibandingkan dengan O(log n) 
pada tree yang seimbang.
3. BST tidak selalu seimbang karena struktur tree tergantung pada urutan data yang dimasukkan. 
Jika data dimasukkan dalam urutan yang sudah terurut (naik atau turun), maka tree akan menjadi tidak seimbang,
dengan semua node berada di satu sisi (kiri atau kanan). Untuk menjaga keseimbangan, diperlukan algoritma khusus
seperti AVL Tree yang melakukan rotasi untuk memastikan tree tetap seimbang setelah setiap operasi
insert atau delete.
'''