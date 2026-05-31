def simpan_file(linkedlist):     # Fungsi untuk menyimpan data ke file

    file = open("data_tahanan.txt", "w")    # Membuka file

    sekarang = linkedlist.head      # Memulai dari node pertama pada linked list

    while sekarang is not None:       # Perulangan selama masih ada node yang dibaca

        data = sekarang.data     # Mengambil data tahanan dari node saat ini


     # Menggabungkan seluruh atribut menjadi satu baris teks dengan pemisah koma (,)
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