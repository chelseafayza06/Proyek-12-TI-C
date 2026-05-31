# =========================================
# IMPORT SEMUA MODULE DAN STRUKTUR DATA
# =========================================

from tahanan import Tahanan              # Class objek tahanan
from helper import *                     # Fungsi bantuan (hukuman & tingkat bahaya)
from linkedlist import LinkedList        # Single Linked List
from stack import Stack                  # Stack
from queue import Queue                  # Queue
from sorting import bubble_sort_nama     # Bubble Sort
from hashtable import HashTable          # Hash Table
from graph import Graph                  # Graph
from tree import *                       # Tree
from filehandler import simpan_file      # Simpan data ke file


# =========================================
# INISIALISASI STRUKTUR DATA
# =========================================

data_tahanan = LinkedList()      # Menyimpan seluruh data tahanan

riwayat = Stack()                # Menyimpan riwayat aktivitas

antrean = Queue()                # Menyimpan antrean pengunjung

hash_table = HashTable(1000)       # Mempercepat pencarian tahanan berdasarkan ID

graph = Graph()                  # Menyimpan hubungan antar tahanan


# =========================================
# PROGRAM UTAMA
# =========================================

while True:

    # Menampilkan menu utama
    print("\n===== SISTEM SIMULASI PENJARA DIGITAL =====")
    print("1. Tambah Tahanan")
    print("2. Tampilkan Tahanan")
    print("3. Cari Tahanan")
    print("4. Urutkan Nama")
    print("5. Tambah Antrean")
    print("6. Layani Antrean")
    print("7. Riwayat Aktivitas")
    print("8. Tambah Hubungan")
    print("9. Tampilkan Graph")
    print("10. Simpan File")
    print("11. Tree Penjara")
    print("12. Tambah Pelanggaran")
    print("13. Lihat Pelanggaran")
    print("14. Lihat Identitas Tetap")
    print("15. Keluar")

    pilih = input("Pilih menu : ")

    # ===================================================
    # MENU 1 - MENAMBAHKAN DATA TAHANAN
    # ===================================================
    if pilih == "1":

        # Validasi ID tahanan harus 4 digit angka
        while True:

            id_tahanan = input("ID Tahanan : ")

            valid = True

            # Cek panjang ID
            if len(id_tahanan) != 4:
                valid = False

            # Cek apakah semua karakter berupa angka
            for huruf in id_tahanan:

                if huruf < "0" or huruf > "9":
                    valid = False

            if valid == True:
                break
            else:
                print("ID harus berupa 4 digit angka")

        # Input nama tahanan
        nama = input("Nama Tahanan : ")

        # Menampilkan daftar kasus
        print("\n=== DAFTAR KASUS ===")
        print("1. Pencurian")
        print("2. Narkoba")
        print("3. Pembunuhan")
        print("4. Penipuan")
        print("5. Korupsi")
        print("6. Pencemaran Nama Baik secara langsung")
        print("7. Pencemaran Nama Baik di Media Sosial")
        print("8. KDRT")
        print("9. Bullying")

        pilihan_kasus = input("Pilih kasus : ")

        # Menentukan kasus berdasarkan pilihan pengguna
        if pilihan_kasus == "1":
            kasus = "Pencurian"

        elif pilihan_kasus == "2":
            kasus = "Narkoba"

        elif pilihan_kasus == "3":
            kasus = "Pembunuhan"

        elif pilihan_kasus == "4":
            kasus = "Penipuan"

        elif pilihan_kasus == "5":
            kasus = "Korupsi"

        elif pilihan_kasus == "6":
            kasus = "Pencemaran Nama Baik secara langsung"

        elif pilihan_kasus == "7":
            kasus = "Pencemaran Nama Baik di Media Sosial"

        elif pilihan_kasus == "8":
            kasus = "KDRT"

        elif pilihan_kasus == "9":
            kasus = "Bullying"

        else:
            kasus = "Tidak diketahui"

        # Menentukan lama hukuman berdasarkan kasus
        hukuman = tentukan_hukuman(kasus)

        # Menentukan tingkat bahaya tahanan
        bahaya = tentukan_bahaya(hukuman)

        # Membuat objek tahanan
        tahanan = Tahanan(
            id_tahanan,
            nama,
            kasus,
            hukuman,
            bahaya
        )

        # Menyimpan ke Linked List
        data_tahanan.tambah_tahanan(tahanan)

        # Menyimpan ke Hash Table
        hash_table.insert(id_tahanan, tahanan)

        # Menambah vertex ke Graph
        graph.tambah_vertex(nama)

        # Menyimpan aktivitas ke Stack
        riwayat.push("Tambah tahanan " + nama)

        print("Tahanan berhasil ditambahkan")

    # ===================================================
    # MENU 2 - MENAMPILKAN DATA TAHANAN
    # ===================================================
    elif pilih == "2":

        # Menampilkan seluruh data tahanan
        data_tahanan.tampilkan()

    # ===================================================
    # MENU 3 - MENCARI TAHANAN DENGAN HASH TABLE
    # ===================================================
    elif pilih == "3":

        target = input("Masukkan ID : ")

        # Pencarian menggunakan Hash Table
        hasil = hash_table.search(target)

        if hasil is not None:

            print("\n=== DATA DITEMUKAN ===")
            print("Nama      :", hasil.nama)
            print("Kasus     :", hasil.kasus)
            print("Hukuman   :", hasil.hukuman)
            print("Bahaya    :", hasil.bahaya)

        else:

            print("Data tidak ditemukan")

    # ===================================================
    # MENU 4 - SORTING NAMA TAHANAN
    # ===================================================
    elif pilih == "4":

        # Linked List diubah menjadi list biasa
        data = data_tahanan.ubah_jadi_list()

        # Bubble Sort berdasarkan nama
        bubble_sort_nama(data)

        print("\n=== HASIL SORTING ===")

        for i in range(len(data)):
            print(data[i].nama)

    # ===================================================
    # MENU 5 - MENAMBAH ANTREAN PENGUNJUNG
    # ===================================================
    elif pilih == "5":

        nama = input("Nama antrean : ")

        # Menambahkan ke Queue
        antrean.enqueue(nama)

        print("Antrean berhasil ditambahkan")

    # ===================================================
    # MENU 6 - MELAYANI ANTREAN
    # ===================================================
    elif pilih == "6":

        # Mengambil antrean pertama (FIFO)
        hasil = antrean.dequeue()

        if hasil is not None:
            print(hasil, "dilayani")
        else:
            print("Antrean kosong")

    # ===================================================
    # MENU 7 - MENAMPILKAN RIWAYAT AKTIVITAS
    # ===================================================
    elif pilih == "7":

        # Menampilkan isi Stack
        riwayat.tampilkan()

    # ===================================================
    # MENU 8 - MENAMBAHKAN HUBUNGAN ANTAR TAHANAN
    # ===================================================
    elif pilih == "8":

        a = input("Tahanan 1 : ")
        b = input("Tahanan 2 : ")

        # Menambahkan edge pada Graph
        graph.tambah_hubungan(a, b)

        print("Hubungan berhasil ditambahkan")

    # ===================================================
    # MENU 9 - MENAMPILKAN GRAPH
    # ===================================================
    elif pilih == "9":

        # Menampilkan hubungan antar tahanan
        graph.tampilkan()

    # ===================================================
    # MENU 10 - MENYIMPAN DATA KE FILE TXT
    # ===================================================
    elif pilih == "10":

        simpan_file(data_tahanan)

    # ===================================================
    # MENU 11 - MENAMPILKAN TREE PENJARA
    # ===================================================
    elif pilih == "11":

        # Root Tree
        root = TreeNode("Penjara")

        # Level 1
        root.child1 = TreeNode("Blok A")
        root.child2 = TreeNode("Blok B")

        # Level 2
        root.child1.child1 = TreeNode("Sel A1")
        root.child1.child2 = TreeNode("Sel A2")

        root.child2.child1 = TreeNode("Sel B1")
        root.child2.child2 = TreeNode("Sel B2")

        # Menampilkan Tree
        tampil_tree(root)

    # ===================================================
    # MENU 12 - MENAMBAHKAN PELANGGARAN (SET)
    # ===================================================
    elif pilih == "12":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            pelanggaran = input("Masukkan Pelanggaran : ")

            # Menambahkan ke Set
            tahanan.pelanggaran.add(pelanggaran)

            print("Pelanggaran berhasil ditambahkan")

        else:

            print("Tahanan tidak ditemukan")

    # ===================================================
    # MENU 13 - MENAMPILKAN PELANGGARAN
    # ===================================================
    elif pilih == "13":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            print("\n=== DAFTAR PELANGGARAN ===")

            # Jika Set kosong
            if len(tahanan.pelanggaran) == 0:

                print("Belum ada pelanggaran")

            else:

                # Menampilkan seluruh pelanggaran
                for data in tahanan.pelanggaran:
                    print("-", data)

        else:

            print("Tahanan tidak ditemukan")

    # ===================================================
    # MENU 14 - MENAMPILKAN IDENTITAS TETAP (TUPLE)
    # ===================================================
    elif pilih == "14":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            print("\n=== IDENTITAS TETAP ===")

            # Tuple tidak dapat diubah setelah dibuat
            print("ID   :", tahanan.identitas[0])
            print("Nama :", tahanan.identitas[1])

        else:

            print("Tahanan tidak ditemukan")

    # ===================================================
    # MENU 15 - KELUAR PROGRAM
    # ===================================================
    elif pilih == "15":

        print("Program selesai")
        break

    # ===================================================
    # JIKA MENU TIDAK TERSEDIA
    # ===================================================
    else:

        print("Menu tidak tersedia")