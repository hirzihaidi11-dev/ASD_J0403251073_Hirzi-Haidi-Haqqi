#################################
# LATIHAN PRAKTIKKUM PERTEMUAN 3 
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
#################################

#Latihan 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

    def delete_node(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        print("Elemen", key, "Telah dihapus")

        if temp is None:
            return
    # Jika node adalah head
        if temp.prev is None:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    # Jika node adalah tail
        elif temp.next is None:
            self.tail = temp.prev
            self.tail.next = None

    # Jika node di tengah
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


dll = DoublyLinkedList()
data_input = input("Masukkan elemen ke dalam DoublyLinkedlist(Pisahkan dengan Spasi): ")
data = data_input.strip().split()
for elemen in data :
    dll.insert_at_end(int(elemen))
print("Sebelum dihapus: \n")
dll.display_forward()
dll.display_backward()

hapus = input("Masukkan elemen yang ingin dihapus: ")
dll.delete_node(int(hapus))
print("Setelah dihapus: \n")
dll.display_forward()
dll.display_backward()
