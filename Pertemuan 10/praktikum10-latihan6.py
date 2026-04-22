#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

# =============================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
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
def tampil_struktur(root, level=0, posisi="Root", max_level=5): 
    if root is not None: # Jika root tidak kosong
        indent = " " * (max_level - level) # Indentasi untuk visualisasi tree
        print(indent + f"{posisi}: {root.data}") # Cetak posisi dan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L", max_level) # Baca Child kiri dengan level bertambah 1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R", max_level) # Baca Child kanan dengan level bertambah 1 dan posisi "R"

# Fungsi rotasi kanan
''' Alur Fungsi rotate_right pada BST diawali dengan menyimpan node y sebagai root lama, menyimpan node x sebagai
child kiri y, dan menyimpan subtree kanan milik x (T2) sementara. Kemudian proses rotasi dilakukan dengan
menjadikan y sebagai child kanan dari x, dan child kiri y diganti dengan T2. Akhirnya x menjadi root baru setelah rotasi kanan.
'''
def rotate_right(y):
    # y adalah root lama
    x = y.left  # x adalah child kiri y
    T2 = x.right  # subtree kanan milik x disimpan sementara

    # Proses rotasi
    x.right = y # y menjadi child kanan dari x
    y.left = T2 # child kiri y diganti dengan T2

    # x menjadi root baru
    return x

# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)
print("\nPreorder sesudah rotasi kanan:")
preorder(root)
print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)