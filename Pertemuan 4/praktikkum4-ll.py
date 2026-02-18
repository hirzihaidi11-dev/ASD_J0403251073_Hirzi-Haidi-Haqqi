# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# =========================================
# Implementasi Dasar: Node Pada Linked List
# =========================================

# Membuat class Node(merupakan unit dasar dari LinkedList)
class Node:
    def __init__(self, data): # Konstruktor
        self.data = data # Menyimpan nilai/data
        self.next = None # Pointer ke note berikutnya

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelusuri dari head sampai none
current = head
while current is not None :
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya
    
# =============================================
# Implementasi Dasar: Linked List + Insert Awal
# =============================================

class LinkedList: # Class Implementasi Stack
    def __init__(self) :
        self.head = None # Awalnya Kosong

    def insert_awal(self, data) : # push dalam stack
        # 1) Buat node baru
        nodeBaru = Node(data) #panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self) : # pop dalam stack
        data_terhapus = self.head.data # peek dalam stack
        # Menggeser headke node berikutnya
        self.head = self.head.next 
        print("Node yang dihapus adalah:", data_terhapus)

    def tampilkan(self) :
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next

print("=====List Baru=====")
ll = LinkedList() # Instantiasi objek ke class Linked List

ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()