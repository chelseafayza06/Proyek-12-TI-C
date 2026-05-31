def simpan_file(linkedlist):     # Fungsi untuk menyimpan data ke file

    file = open("data_tahanan.txt", "w")    # Membuka file

    sekarang = linkedlist.head      # Memulai dari node pertama pada linked list

    while sekarang is not None:       # Perulangan selama masih ada node yang dibaca

        data = sekarang.data     # Mengambil data tahanan dari node saat ini


<<<<<<< Hgit add filehandler.pyEAD
     # Menggabungkan seluruh atribut menjadi satu baris teks dengan pemisah koma (,)
=======
    # Menggabungkan seluruh atribut menjadi satu baris teks
    # dengan pemisah koma (,)
>>>>>>> 184dfe3f257b6bfeaf0a43c087a8d71c011aef61
        teks = (
            data.id + "," +
            data.nama + "," +
            data.kasus + "," +
            str(data.hukuman) + "," +
            data.bahaya + "\n"
        )

        file.write(teks)      # Menulis data ke dalam file

        sekarang = sekarang.next      # Berpindah ke node berikutnya

    file.close()     # Menutup file setelah semua data selesai disimpan

    print("Data berhasil disimpan")      # Menampilkan pesan bahwa proses penyimpanan berhasil