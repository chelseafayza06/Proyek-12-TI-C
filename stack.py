# Digunakan untuk menyimpan riwayat aktivitas.
# Prinsip kerja: LIFO (Last In First Out)
# Data yang terakhir masuk akan ditampilkan lebih dulu.

# Node untuk menyimpan satu data aktivitas
class StackNode:

    def __init__(self, data):

        self.data = data # menyimpan isi aktivitas atau datanya 
        self.next = None # menunjuk ke node berikutnya

class Stack: # membuat struktur data Stack.

    def __init__(self):

        self.top = None # penunjuk ke data paling atas pada stack yang awalnya ksoong

     # Menambahkan data ke bagian atas stack
    def push(self, data): # menambahkan aktivitas baru ke Stack.

        node_baru = StackNode(data)  # membuat node baru

        node_baru.next = self.top    # node baru menunjuk ke top lama

        self.top = node_baru         # top dipindahkan ke node baru

     # Menampilkan seluruh isi stack
    def tampilkan(self):

        sekarang = self.top  # mulai dari data paling atas
 
        print("=== RIWAYAT AKTIVITAS ===")

        while sekarang is not None: # selama masih ada data maka dilanjutkan 

            print(sekarang.data) # tampilkan aktivitas

            sekarang = sekarang.next # pindah ke node berikutnya