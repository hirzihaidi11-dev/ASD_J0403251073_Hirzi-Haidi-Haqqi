#################################
# LATIHAN PRAKTIKKUM PERTEMUAN 3 
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
#################################

#Latihan 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next #simpan next
            current.next = prev #balik arah pointer
            prev = current #geser prev
            current = next_node #geser current

        self.head = prev 

ll = LinkedList()
data_input = input("Masukkan elemen ke dalam Linkedlist(Pisahkan dengan Spasi): ")
data = data_input.strip().split()
for elemen in data :
    ll.insert_at_end(int(elemen))
print("Sebelum di reverse: \n")
ll.display()
ll.reverse()
print("Setelah di reverse: \n")
ll.display()