class Graph:

    def __init__(self):

        self.vertex = {}


    def tambah_vertex(self, nama):

        if nama not in self.vertex:

            self.vertex[nama] = []


    def tambah_hubungan(self, a, b):

        if a not in self.vertex:

            self.vertex[a] = []

        self.vertex[a] += [b]


    def tampilkan(self):

        print("=== HUBUNGAN TAHANAN ===")

        for key in self.vertex:

            print(key, "->", self.vertex[key])