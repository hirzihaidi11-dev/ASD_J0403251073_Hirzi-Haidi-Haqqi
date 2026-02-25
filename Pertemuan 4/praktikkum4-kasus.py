# =====================================
# Nama  : Hirzi Haidi Haqqi
# NIM   : J0403251073
# Kelas : TPL-B2
# =====================================

# ==============================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : Memindahkan pointer rear (nambah data baru dari belakang)
# Dequeue : Memindahkan pointer front (menghapus data dari depan)
# Stack ==> Front -> C -> B -> A -> None
# Queue ==> Front -> A -> B-> C -> Rear
# ==============================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim # Menyimpan NIM Mahasiswa
        self.nama = nama # Menyimpan Nama Mahasiswa 
        self.next = None # Pointer ke Node Berikutnya (tidak menuju kemanapun)

#2) Mendefiniskan Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # Menambahkan Data Baru ke bagian belakang(rear)
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        # Jika data baru masuk dari queue yang kosong, maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return 
        
        # Jika Queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru 

    # Menghapus data paling depan (Memberikan Layanan Akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada mahasiswa yang dilayani")
            return None
        
        # Lihat data bagian Front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        # Geser pointer front ke next front
        self.front = self.front.next

        # jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None :
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear) :")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

# Program Utama 

def main():

    # Instantiasi queue
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) :").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM :").strip()
            nama = input("Masukkan Nama :").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan ke Antrian")
         
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print('Program Selesai. Terima Kasih')
            break
        else :
            print("Pilihan Tidak Valid, Silahkan Coba Lagi (1-4)")

if __name__ == "__main__":
    main()