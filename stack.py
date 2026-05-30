class StackNode:

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