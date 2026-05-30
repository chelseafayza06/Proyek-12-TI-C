from tahanan import Tahanan
from helper import *
from linkedlist import LinkedList
from stack import Stack
from queue import Queue
from sorting import bubble_sort_nama
from hashtable import HashTable
from graph import Graph
from tree import *
from filehandler import simpan_file


data_tahanan = LinkedList()

riwayat = Stack()

antrean = Queue()

hash_table = HashTable(10)

graph = Graph()


while True:

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

    # =====================================
    # INPUT DATA TAHANAN 
    # =====================================
    if pilih == "1":

        while True:

            id_tahanan = input("ID Tahanan : ")

            valid = True

            if len(id_tahanan) != 4:

                valid = False

            for huruf in id_tahanan:

                if huruf < "0" or huruf > "9":

                    valid = False

            if valid == True:

                break

            else:

                print("ID harus berupa 4 digit angka")


        nama = input("Nama Tahanan : ")

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



        hukuman = tentukan_hukuman(kasus)

        bahaya = tentukan_bahaya(hukuman)


        tahanan = Tahanan(
            id_tahanan,
            nama,
            kasus,
            hukuman,
            bahaya
        )


        data_tahanan.tambah_tahanan(tahanan)

        hash_table.insert(id_tahanan, tahanan)

        graph.tambah_vertex(nama)

        riwayat.push("Tambah tahanan " + nama)

        print("Tahanan berhasil ditambahkan")

    # =====================================
    # MENAMPILKAN DATA TAHANAN
    # =====================================
    elif pilih == "2":

        data_tahanan.tampilkan()


    # =====================================
    # CARI TAHANAN
    # =====================================
    elif pilih == "3":

        target = input("Masukkan ID : ")

        hasil = hash_table.search(target)

        if hasil is not None:

            print("\n=== DATA DITEMUKAN ===")
            print("Nama      :", hasil.nama)
            print("Kasus     :", hasil.kasus)
            print("Hukuman   :", hasil.hukuman)
            print("Bahaya    :", hasil.bahaya)

        else:

            print("Data tidak ditemukan")

    # =====================================
    # SORTING - URUTKAN DATA TAHANAN
    # =====================================
    elif pilih == "4":

        data = data_tahanan.ubah_jadi_list() # ubah single linked list jd list biasa

        bubble_sort_nama(data)

        print("\n=== HASIL SORTING ===")

        for i in range(len(data)):

            print(data[i].nama)

    # =====================================
    # QUEUE - INPUT ANTRIAN
    # =====================================
    elif pilih == "5":

        nama = input("Nama antrean : ")

        antrean.enqueue(nama)

        print("Antrean berhasil ditambahkan")

    # =====================================
    # QUEUE - ANTRIAN PELAYANAN PENGUNJUNG
    # =====================================
    elif pilih == "6":

        hasil = antrean.dequeue()

        if hasil is not None:

            print(hasil, "dilayani")

        else:

            print("Antrean kosong")

    # =====================================
    # SET - TAMBAH PELANGGARAN
    # =====================================
    elif pilih == "7":

        riwayat.tampilkan()

    # =====================================
    # GRAPH - INPUT HUB ANTAR TAHANAN
    # =====================================
    elif pilih == "8":

        a = input("Tahanan 1 : ")

        b = input("Tahanan 2 : ")

        graph.tambah_hubungan(a, b)

        print("Hubungan berhasil ditambahkan")

    # =====================================
    # GRAPH - MENAMPILKAN HUB ANTAR TAHANAN
    # =====================================
    elif pilih == "9":

        graph.tampilkan()

    # =====================================
    # FILE HANDLER - MENYIMPAN FILE KE TXT
    # =====================================
    elif pilih == "10":

        simpan_file(data_tahanan)

    # =====================================
    # TREE - PEMBAGIAN BLOK DAN SEL PENJARA
    # =====================================
    elif pilih == "11":

        root = TreeNode("Penjara")

        root.child1 = TreeNode("Blok A")
        root.child2 = TreeNode("Blok B")

        root.child1.child1 = TreeNode("Sel A1")
        root.child1.child2 = TreeNode("Sel A2")

        root.child2.child1 = TreeNode("Sel B1")
        root.child2.child2 = TreeNode("Sel B2")

        tampil_tree(root)



    # =====================================
    # SET - TAMBAH PELANGGARAN
    # =====================================

    elif pilih == "12":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            pelanggaran = input("Masukkan Pelanggaran : ")

            tahanan.pelanggaran.add(pelanggaran)

            print("Pelanggaran berhasil ditambahkan")

        else:

            print("Tahanan tidak ditemukan")


    # =====================================
    # SET - LIHAT PELANGGARAN
    # =====================================

    elif pilih == "13":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            print("\n=== DAFTAR PELANGGARAN ===")

            if len(tahanan.pelanggaran) == 0:

                print("Belum ada pelanggaran")

            else:

                for data in tahanan.pelanggaran:

                    print("-", data)

        else:

            print("Tahanan tidak ditemukan")


    # =====================================
    # TUPLE - IDENTITAS TETAP
    # =====================================

    elif pilih == "14":

        target = input("Masukkan ID Tahanan : ")

        tahanan = hash_table.search(target)

        if tahanan is not None:

            print("\n=== IDENTITAS TETAP ===")

            print("ID   :", tahanan.identitas[0])
            print("Nama :", tahanan.identitas[1])

        else:

            print("Tahanan tidak ditemukan")


    # =====================================
    # KELUAR
    # =====================================

    elif pilih == "15":

        print("Program selesai")
        break


    else:

        print("Menu tidak tersedia")