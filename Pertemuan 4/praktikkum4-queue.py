# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Implementasi Dasar: Queue Berbasis Linked List
# ==============================================

# Membuat class Node(merupakan unit dasar dari LinkedList)
class Node:
    def __init__(self, data): # Konstruktor
        self.data = data # Menyimpan nilai/data
        self.next = None # Pointer ke note berikutnya

# Queue dengan 2 pointer : front and rear
class QueueLL :
    def __init__(self) :
        self.front = None # node paling depan
        self.rear = None # node paling belakang

    def is_empty(self) :
        # Queue kosong jika front = None
        return self.front is None
    
    def enqueue(self, data) :
        # Menambah data di belakang (rear)
        nodeBaru = Node(data)

        # Jika queue kosong front and rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika queue tidak kosong:
        # Rearr lama menunjuk ke node baru
        self.rear.next = nodeBaru 
        # Rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self) :
        # Menghapus data dari depan

        # 1) Ambil data yang paling depan
        data_terhapus = self.front.data
        
        # 2) geser front ke node berikutnya
        self.front = self.front.next

        # 3) Jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self) :

        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

# Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()

q.dequeue()
q.tampilkan()