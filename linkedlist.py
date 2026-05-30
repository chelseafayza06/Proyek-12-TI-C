class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None


    def tambah_tahanan(self, data):

        node_baru = Node(data)

        if self.head is None:

            self.head = node_baru

        else:

            sekarang = self.head

            while sekarang.next is not None:

                sekarang = sekarang.next

            sekarang.next = node_baru


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


    def ubah_jadi_list(self):

        hasil = []

        sekarang = self.head

        while sekarang is not None:

            hasil += [sekarang.data]

            sekarang = sekarang.next

        return hasil