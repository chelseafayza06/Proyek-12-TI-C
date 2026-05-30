class HashTable:

    def __init__(self, ukuran):

        self.ukuran = ukuran

        self.tabel = [None] * ukuran


    def hash_function(self, key):

        total = 0

        for huruf in key:

            total += ord(huruf)

        return total % self.ukuran


    def insert(self, key, value):

        index = self.hash_function(key)

        self.tabel[index] = value


    def search(self, key):

        index = self.hash_function(key)

        return self.tabel[index]