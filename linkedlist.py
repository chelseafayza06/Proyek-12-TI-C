# =====================================
# SINGLE LINKED LIST
# Digunakan sebagai struktur utama
# untuk menyimpan seluruh data tahanan
# secara dinamis.
# =====================================

class Node:
    
    def __init__(self, data):
        # Menyimpan objek tahanan
        self.data = data

        # Pointer ke node berikutnya
        self.next = None


class LinkedList:

    def __init__(self):
        # Head menunjuk ke tahanan pertama dalam sistem penjara digital
        self.head = None
        
    # =====================================
    # TAMBAH TAHANAN
    # Menyisipkan data tahanan baru
    # ke bagian akhir Linked List
    # =====================================

    def tambah_tahanan(self, data):
        # Membuat node baru yang berisi data tahanan
        node_baru = Node(data)

        # Jika belum ada tahanan, node baru menjadi head
        if self.head is None:

            self.head = node_baru

        else:

            # Menelusuri sampai node terakhir
            sekarang = self.head

            while sekarang.next is not None:

                sekarang = sekarang.next

            # Menambahkan tahanan baru di akhir daftar
            sekarang.next = node_baru


    # =====================================
    # TAMPILKAN DATA
    # Menampilkan seluruh data tahanan
    # yang tersimpan dalam Linked List
    # =====================================

    def tampilkan(self):
        # Mulai dari node pertama
        sekarang = self.head

        # Jika tidak ada data tahanan
        if sekarang is None:

            print("Data tahanan kosong")
            return

        # Traversal seluruh node
        while sekarang is not None:

            data = sekarang.data

            print("========================")
            print("ID       :", data.id)
            print("Nama     :", data.nama)
            print("Kasus    :", data.kasus)
            print("Hukuman  :", data.hukuman, "tahun")
            print("Bahaya   :", data.bahaya)

            # Pindah ke tahanan berikutnya
            sekarang = sekarang.next


    # =====================================
    # UBAH KE LIST UNTUK SORTING
    # Mengonversi data dari Linked List
    # menjadi Python List agar dapat
    # diproses oleh algoritma Bubble Sort
    # =====================================

    def ambil_ke_list(self):
        # Menampung seluruh data tahanan
        hasil = []

        # Mulai traversal dari head
        sekarang = self.head

        while sekarang is not None:

            # Memasukkan objek tahanan ke dalam list sementara
            hasil += [sekarang.data]

            sekarang = sekarang.next

        # Mengembalikan list untuk proses pengurutan berdasarkan nama
        return hasil