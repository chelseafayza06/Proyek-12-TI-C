# =====================================
# QUEUE MANUAL
# Digunakan untuk mengelola antrean
# layanan dalam sistem penjara digital
# dengan prinsip FIFO (First In First Out)
# =====================================

class QueueNode:

    def __init__(self, data):
        # Menyimpan data antrean
        #(nama tahanan atau pengunjung)
        self.data = data

        # Pointer ke node berikutnya
        self.next = None


class Queue:

    def __init__(self):
        # Menunjuk elemen pertama yang akan dilayani
        self.front = None

        # Menunjuk elemen terakhir dalam antrean
        self.rear = None


    # =====================================
    # ENQUEUE
    # Menambahkan data ke bagian belakang antrean
    # =====================================

    def enqueue(self, data):
        # Membuat node antrean baru
        node_baru = QueueNode(data)

        # Jika antrean masih kosong
        if self.rear is None:

            # Node baru menjadi elemen pertama sekaligus elemen terakhir
            self.front = node_baru
            self.rear = node_baru

        else:

            # Menghubungkan node terakhir dengan node baru
            self.rear.next = node_baru

            # Memperbarui posisi rear ke node baru
            self.rear = node_baru


    # =====================================
    # DEQUEUE
    # Mengambil dan menghapus data yang
    # berada di depan antrean
    # =====================================

    def dequeue(self):
        # Jika antrean kosong
        if self.front is None:

            return None

        # Menyimpan data yang akan dilayani
        data = self.front.data

        # Memindahkan front ke node berikutnya
        self.front = self.front.next

        # Jika setelah penghapusan antrean kosong
        if self.front is None:

            # Rear juga dikosongkan
            self.rear = None

        # Mengembalikan data yang telah dilayani
        return data