#========IDENTITAS MAHASISWA===================
#NAMA : Hirzi Haidi Haqqi
#NIM : J0403251073
#Kelas : TPL-P2
#==============================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,no,nama,servis):
        self.no = no # Menyimpan No Antrian
        self.nama = nama # Menyimpan Nama Mahasiswa 
        self.servis = servis # Menyimpan Jenis servis
        self.next = None # Pointer ke Node Berikutnya (tidak menuju kemanapun)

#2) Mendefiniskan Queue, terdiri dari front dan rear
class queueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # Menambahkan Data Baru ke bagian belakang(rear)
    def enqueue(self,no,nama,servis):
        nodeBaru = Node(no,nama,servis)
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
            print("Antrian Kosong. Tidak ada Pelanggan yang dilayani")
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
        print("Daftar Antrian Pelanggan Bengkel :")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.no} - {current.nama} - {current.servis}")
            current = current.next
            no += 1

# Program Utama 

def main():

    # Instantiasi queue
    q = queueBengkel()

    while True:
        print("===== Sistem Antrian Bengkel =====")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) :").strip()

        if pilihan == "1":
            try:
                no= int(input("Masukkan No. Antrian : ").strip())
            except ValueError: 
                print("No. Antrian harus berupa angka. Penambahan dibatalkan")
                return
    
            nama = input("Masukkan Nama :").strip()
            servis = input("Masukkan Jenis Servis yang diinginkan :")

            q.enqueue(no,nama,servis)
            print("Pelanggan Berhasil Ditambahkan ke Antrian")
         
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Pelanggan Dilayani : {dilayani.no} - {dilayani.nama} - {dilayani.servis}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print('Program Selesai. Terima Kasih')
            break
        else :
            print("Pilihan Tidak Valid, Silahkan Coba Lagi (1-4)")

if __name__ == "__main__":
    main()