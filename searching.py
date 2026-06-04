def linear_search_nama(linkedlist, target):

    sekarang = linkedlist.head

    while sekarang is not None:

        if sekarang.data.nama == target:

            return sekarang.data

        sekarang = sekarang.next

    return None