class Graph:
    def __init__(self):    # Constructor yang akan dijalankan saat objek Graph dibuat
        self.vertex = {}     # Membuat dictionary kosong untuk menyimpan vertex dan hubungannya


    def tambah_vertex(self, nama): # Method untuk menambahkan vertex (simpul) baru ke graph
        if nama not in self.vertex:      # Memeriksa apakah vertex sudah ada atau belum
            self.vertex[nama] = []


    def tambah_hubungan(self, a, b):    # Method untuk menambahkan hubungan antara dua vertex
        if a not in self.vertex:       # Jika vertex asal belum ada di graph
            self.vertex[a] = []     # Buat vertex tersebut terlebih dahulu
        self.vertex[a] += [b]     # Menambahkan vertex tujuan ke daftar hubungan


    def tampilkan(self):    # Method untuk menampilkan seluruh isi graph
        print("=== HUBUNGAN TAHANAN ===")    # Menampilkan judul output
        for key in self.vertex:     # Melakukan perulangan pada setiap vertex
            print(key, "->", self.vertex[key])     # Menampilkan nama vertex dan daftar