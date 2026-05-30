# =====================================
# BUBBLE SORT BERDASARKAN NAMA
# Digunakan untuk mengurutkan data
# tahanan secara alfabetis berdasarkan
# atribut nama
# =====================================

def bubble_sort_nama(data):
    # Menentukan jumlah data tahanan
    n = len(data)

    # Perulangan utama Bubble Sort
    for i in range(n):

        # Membandingkan elemen yang bersebelahan pada setiap pass
        for j in range(n - i - 1):

            # Jika nama di posisi sekarang lebih besar dari nama berikutnya
            if data[j].nama > data[j + 1].nama:

                # Menyimpan data sementara
                sementara = data[j]

                # Menukar posisi data
                data[j] = data[j + 1]

                data[j + 1] = sementara

    # Mengembalikan data yang telah diurutkan berdasarkan nama
    return data