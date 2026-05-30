class Tahanan: #class untuk menyimpan data setiap tahanan

    # sebagai constructor otomatis dijalankan saat object dibuat
    def __init__(self, id_tahanan, nama, kasus, hukuman, bahaya):

        self.id = id_tahanan # menyimpan ID tahanan
        self.nama = nama     # menyimpan nama tahanan
        self.kasus = kasus   # menyimpan jenis kasus
        self.hukuman = hukuman # menyimpan lama hukuman tahanan
        self.bahaya = bahaya   # menyimpan tingkat bahaya tahanan
        