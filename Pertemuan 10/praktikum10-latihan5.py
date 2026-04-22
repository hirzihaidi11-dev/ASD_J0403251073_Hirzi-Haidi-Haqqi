#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# =============================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# =============================================

# Class Node untuk menyimpan data BST
class Node: # Class Node digunakan untuk dasar dari tree
    def __init__(self, data): 
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan
        
# Fungsi preorder untuk melihat isi tree
''' Alur Fungsi Preorder pada BST diawali dengan membaca root tidak kosong, kemudian cetak data, 
lalu membaca child kiri, dan membaca child kanan (konsep preorder).
'''
def preorder(root):
    if root is not None: # Jika root tidak kosong
        print(root.data, end=" ") # Mencetak data pada node saat ini
        preorder(root.left) # Baca Child kiri
        preorder(root.right) # Baca Child kanan

# Fungsi untuk menampilkan struktur tree
''' Alur Fungsi tampil_struktur pada BST diawali dengan membaca root tidak kosong dan level dimulai dari 0,
kemudian cetak posisi(level) dan data, lalu membaca root kiri dengan level bertambah 1 dan posisi "L", dan
membaca root kanan dengan level bertambah 1 dan posisi "R".
'''
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # Jika root tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # Cetak posisi dan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") # Baca Child kiri dengan level bertambah 1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R") # Baca Child kanan dengan level bertambah 1 dan posisi "R"

# Fungsi rotasi kiri
''' Alur Fungsi rotate_left pada BST diawali dengan menyimpan node x sebagai root lama, menyimpan node y sebagai
child kanan x, dan menyimpan subtree kiri milik y (T2) sementara. Kemudian proses rotasi dilakukan dengan
menjadikan x sebagai child kiri dari y, dan child kanan x diganti dengan T2. Akhirnya y menjadi root baru
setelah rotasi kiri.
'''
def rotate_left(x):
    # x adalah root lama
    y = x.right  # y adalah child kanan x
    T2 = y.left  # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)
print("\nPreorder sesudah rotasi kiri:")
preorder(root)
print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)