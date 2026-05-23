# =========================================
# SISTEM SIMULASI PENJARA DIGITAL
# IMPLEMENTASI STRUKTUR DATA MANUAL
# =========================================


# =========================================
# CLASS TAHANAN
# =========================================

class Tahanan: # membuat class  tahanan
    # memberi nilai awal pada object saat object dibuat
    def __init__(self, id_tahanan, nama, kasus, hukuman, bahaya): # constructor

        self.id = id_tahanan
        self.nama = nama
        self.kasus = kasus
        self.hukuman = hukuman
        self.bahaya = bahaya


# =========================================
# MENENTUKAN HUKUMAN BERDASARKAN KASUS
# =========================================
# fungsi baru menentukan kasus
def tentukan_hukuman(kasus):

    if kasus == "Pencurian":

        return 5

    elif kasus == "Narkoba":

        return 12

    elif kasus == "Pembunuhan":

        return 20

    elif kasus == "Penipuan":

        return 4

    elif kasus == "Korupsi":

        return 15

    elif kasus == "Pelecehan":

        return 10

    elif kasus == "KDRT":

        return 3

    elif kasus == "Pencemaran Nama Baik secara langsung":

        return 1

    elif kasus == "Pencemaran Nama Baik di Media Sosial":

        return 6

    elif kasus == "Bullying":

        return 4

    else:

        return 1


# =========================================
# MENENTUKAN TINGKAT BAHAYA
# =========================================

def tentukan_bahaya(hukuman):

    if hukuman >= 15:

        return "Tinggi"

    elif hukuman >= 5:

        return "Sedang"

    else:

        return "Rendah"


# =========================================
# SINGLE LINKED LIST
# =========================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    # fungsi output pertama
    def tambah_tahanan(self, data):

        node_baru = Node(data)

        if self.head is None:

            self.head = node_baru

        else:

            sekarang = self.head

            while sekarang.next is not None:

                sekarang = sekarang.next

            sekarang.next = node_baru

    # fungsi output kedua
    def tampilkan(self):

        sekarang = self.head

        if sekarang is None:

            print("Data tahanan kosong")
            return

        while sekarang is not None:

            data = sekarang.data

            print("========================")
            print("ID       :", data.id)
            print("Nama     :", data.nama)
            print("Kasus    :", data.kasus)
            print("Hukuman  :", data.hukuman, "tahun")
            print("Bahaya   :", data.bahaya)

            sekarang = sekarang.next


    def ubah_jadi_list(self): # digunakan untuk mengubah data pada single linked list menjadi list biasa
        # agar data dapat diproses lebih mudah, terutama saat melakukan sorting.

        hasil = []

        sekarang = self.head

        while sekarang is not None:

            hasil += [sekarang.data] #masukin data tahanan ke list

            sekarang = sekarang.next

        return hasil


# =========================================
# STACK 
# =========================================

class StackNode: # penyimpan riwayat aktivitas terakhir

    def __init__(self, data):

        self.data = data
        self.next = None


class Stack:

    def __init__(self):

        self.top = None


    def push(self, data):

        node_baru = StackNode(data)

        node_baru.next = self.top

        self.top = node_baru


    def tampilkan(self):

        sekarang = self.top

        print("=== RIWAYAT AKTIVITAS ===")

        while sekarang is not None:

            print(sekarang.data)

            sekarang = sekarang.next

# =========================================
# QUEUE MANUAL
# =========================================

class QueueNode:

    def __init__(self, data):

        self.data = data
        self.next = None


class Queue:

    def __init__(self):

        self.front = None
        self.rear = None


    def enqueue(self, data):

        node_baru = QueueNode(data)

        if self.rear is None:

            self.front = node_baru
            self.rear = node_baru

        else:

            self.rear.next = node_baru
            self.rear = node_baru


    def dequeue(self):

        if self.front is None:

            return None

        data = self.front.data

        self.front = self.front.next

        if self.front is None:

            self.rear = None

        return data




