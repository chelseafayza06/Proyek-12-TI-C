def simpan_file(linkedlist):

    file = open("data_tahanan.txt", "w")

    sekarang = linkedlist.head

    while sekarang is not None:

        data = sekarang.data

        teks = (
            data.id + "," +
            data.nama + "," +
            data.kasus + "," +
            str(data.hukuman) + "," +
            data.bahaya + "\n"
        )

        file.write(teks)

        sekarang = sekarang.next

    file.close()

    print("Data berhasil disimpan")