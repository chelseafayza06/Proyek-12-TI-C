def linear_search_nama(linkedlist, target):

    # Mulai pencarian dari node pertama (head)
    sekarang = linkedlist.head

    # Menelusuri seluruh node sampai akhir linked list
    while sekarang is not None:

        # Membandingkan nama tahanan pada node saat ini
        # dengan nama yang dicari
        if sekarang.data.nama == target:

            # Jika ditemukan, kembalikan objek tahanan
            return sekarang.data

        # Pindah ke node berikutnya
        sekarang = sekarang.next

    # Jika seluruh data sudah dicek tetapi tidak ditemukan
    return None