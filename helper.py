def tentukan_hukuman(kasus): # Fungsi untuk menentukan kasus kejahatan dan lama tahun hukuman 

    if kasus == "Pencurian": 
        return 5 # jika pelaku melakukan pencurian maka akan dihukum selama 5 tahun

    elif kasus == "Narkoba":
        return 12 # jika pelaku melakukan narkoba maka akan dihukum selama 12 tahun

    elif kasus == "Pembunuhan":
        return 20 # jika pelaku melakukan pembunuhan maka akan dihukum selama 20 tahun

    elif kasus == "Penipuan":
        return 4 # jika pelaku melakukan penipuan maka akan dihukum selama 4 tahun

    elif kasus == "Korupsi":
        return 15 # jika pelaku melakukan korupsi maka akan dihukum selama 15 tahun

    elif kasus == "Pelecehan":
        return 10 # jika pelaku melakukan pelecehan maka akan dihukum selama 10 tahun

    elif kasus == "KDRT":
        return 3 # jika pelaku melakukan KDRT maka akan dihukum selama 3 tahun

    elif kasus == "Pencemaran Nama Baik secara langsung":
        return 2 # jika pelaku melakukan pencemaran nama baik langsung maka akan dihukum selama 1 tahun

    elif kasus == "Pencemaran Nama Baik di Media Sosial":
        return 6 # jika pelaku melakukan pencemaran nama baik di sosmed maka akan dihukum selama 6 tahun

    elif kasus == "Bullying":
        return 4 # jika pelaku melakukan Bullying maka akan dihukum selama 4 tahun

    else:
        return 0 # jika selain kasus diatas maka 0 tahun


def tentukan_bahaya(hukuman): # fungsi untuk mengetahui tingkat bahaya hukuman sesuai tahun

    if hukuman >= 15: # jika hukuman lebih sama dari 15 tahun maka tingkat hukuman tinggi 
        return "Tinggi"

    elif hukuman >= 5: # jika hukuman lebih sama dari 5 tahun maka tingkat hukuman sedang
        return "Sedang"

    elif hukuman > 1 and hukuman < 5:
        return "Rendah" # jika kurang dari 5 tapi lebih dari 1 maka rendah
    
    else:
        return "Tidak diketahui"