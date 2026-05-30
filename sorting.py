def bubble_sort_nama(data):

    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if data[j].nama > data[j + 1].nama:

                sementara = data[j]

                data[j] = data[j + 1]

                data[j + 1] = sementara

    return data