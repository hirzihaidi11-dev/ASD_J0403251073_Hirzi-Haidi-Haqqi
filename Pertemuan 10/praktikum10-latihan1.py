#========IDENTITAS MAHASISWA===================
# NAMA : Hirzi Haidi Haqqi
# NIM : J0403251073
# Kelas : TPL-P2
#==============================================

#==============================================
# Latihan 1: BST
#==============================================

class Node: # Class Node digunakan untuk dasar dari tree
    def __init__(self,data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # Child kiri, berawal dari none
        self.right = None # Child kanan, berawal dari none

''' Alur Fungsi Insert pada BST diawali dengan membaca apakah root kosong atau tidak, jika kosong maka nilai
yang dimasukkan menjadi node baru dengan nilai (data), lalu node itu dijadikan root. Ketika data yang dimasukkan
lebih kecil dari root maka akan dijadikan sebagai child kiri root jika sebaliknya maka data dijadikan sebagai
child kanan root.
'''

def insert(root,data): # Fungsi insert
    if root is None: # Jika root kosong, maka menjadi node baru dan root-nya
        return Node(data)
    
    if data < root.data: # Jika data yang dimasukkan lebih kecil, maka data menjadi child kiri root
        root.left = insert(root.left,data) # Rekursi ke child kiri
    elif data > root.data: # Jika data yang dimasukkan lebih besar, maka data menjadi child kanan root
        root.right = insert(root.right,data) # Rekursi ke child kanan
    return root

#  Mengisi Data BST
root = None
data_list = [50,30,70,20,40,60,80]

for data in data_list:
    root = insert(root,data)

print("BST Berhasil dibuat")

#==============================================
# Latihan 2: Traversal Inorder
#==============================================


''' Alur Fungsi Inorder pada BST diawali dengan membaca root tidak kosong, kemudian membaca root kiri lalu
cetak data, dan membaca root kanan.
'''

def inorder(root): # Fungsi Inorder
    if root is not None: # Jika root tidak kosong
        inorder(root.left) # Baca Child kiri
        print(root.data, end = " ") # Mencetak data pada node saat ini
        inorder(root.right) # Baca Child kanan

print("Hasil Inorder:")
inorder(root)

#==============================================
# Latihan 3: Search di BST
#==============================================

''' Alur Fungsi Search pada BST diawali dengan membaca apakah root kosong, jika kosong maka kembalikan nilai false
artinya nilai tidak ditemukan. Ketika nilai yang dicari (key) sama dengan root, maka nilai root akan dicetak
dan berubah menjadi true. Ketika nilai yang dicari lebih kecil dari pada root, maka program akan membaca subtree
kiri secara rekursif. Ketika nilai yang dicari lebih besar dari root, maka program akan membaca subtree kanan
secara rekursif.
'''
def search(root,key): # Fungsi Search
    if root is None: # Jika root kosong, maka nilai yang dicari tidak ada dan langsung false
        return False
    
    if root.data == key: # Ketika nilai yang dicari (key) sama dengan root, maka nilai root akan dicetak dan berubah menjadi true
        return True
    elif key < root.data: # Ketika nilai yang dicari lebih kecil dari pada root, maka program akan membaca subtree kiri secara rekursif
        return search(root.left,key)
    else: # Ketika nilai yang dicari lebih besar dari root, maka program akan membaca subtree kanan secara rekursif.
        return search(root.right,key)

# Uji Pencarian
key = 40

if search(root,key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")