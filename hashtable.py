class HashTable:

    def __init__(self, ukuran):      # Constructor yang dijalankan saat objek HashTable dibuat
        self.ukuran = ukuran       # Menyimpan ukuran tabel hash
        self.tabel = [None] * ukuran    # Membuat tabel dengan isi awal None sebanyak ukuran yang ditentukan


    def hash_function(self, key):       # Fungsi hash untuk mengubah key menjadi index tabel
        total = 0           # untuk menyimpan total nilai ASCII

        for huruf in key:    # Melakukan perulangan pada setiap karakter dalam key
            total += ord(huruf)    # Menambahkan nilai ASCII karakter ke total

        return total % self.ukuran  # Mengembalikan index hasil hash menggunakan modulo


    def insert(self, key, value):    #Method untuk menambahkan data ke Hash Table
        index = self.hash_function(key)    # Menentukan index berdasarkan hasil hash key
        self.tabel[index] = value     # Menyimpan value pada index yang diperoleh


    def search(self, key):    # Method untuk mencari data berdasarkan key
        index = self.hash_function(key)  # Menentukan index berdasarkan hasil hash key
        return self.tabel[index]      # Mengembalikan data yang berada pada index tersebut