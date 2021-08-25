import random
import string 


def menu():
    print("***** SELAMAT DATANG DI NF BANK *****")
    print("Menu : ")
    print("[1] Buka Rekening")
    print("[2] Setoran Tunai")
    print("[3] Tarik Tunai") 
    print("[4] Transfer")
    print("[5] Lihat Daftar Transfer")    
    print("[6] Keluar")
    while True:
        pilihan = input('Masukkan Pilihan Anda : ')
        if pilihan == "1":
            Rekening()
        elif pilihan == "2":
            Setoran()
        elif pilihan == "3":
            Tunai()
        elif pilihan == "4":
            Transfer()
        elif pilihan == "5":
            Detail()
        elif pilihan == "6":
            print("Terimakasih atas kunjungan anda")
            exit()
        else:
            print("Pilihan Anda Salah Ulangi")


def Rekening():
    print(" *** BUKA REKENING *** ")#mencetak menu buka rekening 
    nama = input("Masukkan Nama : ") #untuk memasukkan nam user buat buka rekening
    saldo = eval(input("Masukkan setoran awal : ")) #buat masukkan setoran awalnya dan fungsi eval digunakan 
    #untuk mengubah nilai string ke nilai bil bulat atau bilangan desimal
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3)) #untuk mengambil kode rek secara random
    # dan dibatasi angka randomnya sebanyak 3 angka dari for_in range(3)
    print("Pembukaan rekening dengan nomor",
          norek, "atas nama", nama, "Berhasil, Saldo Awal Anda Rp. ", saldo)
    myfile = open('nasabah.txt', 'a+')  # append
    list_nasabah = [norek, nama, saldo]
    for element in list_nasabah:  # mengecek
        myfile.writelines(str(element) + ",")
    myfile.write("\n")
    myfile.close()
    print("\n")
    menu()


def Setoran():
    print("*** SETORAN TUNAI ***")
    list_nasabah = []
    f = open('nasabah.txt', 'r')
    for target in f:
        data = target.split(",")
        list_nasabah.append(data)
    f.close()
    norek = input("Masukkan nomor rekening : ")
    test = False
    for a in range(len(list_nasabah)):
        if (norek.upper() == list_nasabah[a][0]):
            print("No rekening ditemukan")
            test = True
            nominal = eval(input("Masukkan nominal yang akan disetor : "))
            saldo = int(list_nasabah[a][2])
            jumlah = nominal + saldo
            list_nasabah[a][2] = jumlah
            print("Setoran tunai sebesar", nominal,
                  "atas rekening", norek, "berhasil")
    if (test == True):
        print()
    elif (test == False):
        print("No rekening tidak ditemukan")
    f = open('nasabah.txt', 'w+')
    for b in range(len(list_nasabah)):
        data_nasabah = [list_nasabah[b][0],
                        list_nasabah[b][1], list_nasabah[b][2]]
        for target in data_nasabah:
            f.writelines(str(target) + ",")
        f.write("\n")
    f.close()
    print("\n")
    menu()


def Tunai():
    print("*** TARIK TUNAI ***")
    list_nasabah = []
    f = open('nasabah.txt', 'r')
    for target in f:
        data = target.split(",")
        list_nasabah.append(data)
    f.close()
    norek = input("Masukkan nomor rekening : ")
    test = False
    for a in range(len(list_nasabah)):
        if (norek.upper() == list_nasabah[a][0]):
            print("No rekening ditemukan")
            test = True
            nominal = eval(input("Masukkan nominal yang akan ditarik : "))
            saldo = int(list_nasabah[a][2])
            if (saldo < nominal):
                print("Saldo Anda tidak mencukupi,tarik tunai gagal")
            elif (saldo > nominal):
                jumlah = saldo - nominal
                list_nasabah[a][2] = jumlah
                print("Tarik tunai sebesar ", nominal,
                      "dari rekening ", norek, "berhasil")
    if (test == True):
        print()
    elif (test == False):
        print("No rekening tidak ditemukan")
        print("\n")
    f = open('nasabah.txt', 'w+')
    for b in range(len(list_nasabah)):
        data_nasabah = [list_nasabah[b][0],
                        list_nasabah[b][1], list_nasabah[b][2]]
        for target in data_nasabah:
            f.writelines(str(target) + ",")
        f.write("\n")
    f.close()
    menu()


def Transfer():
    print("*** TRANSFER ***")
    list_nasabah = []
    f = open('nasabah.txt', 'r')
    for target in f:
        # rek099,amien,saldo -> [rek099,amien,80000],[....,...,...]
        data = target.split(",")
        list_nasabah.append(data)  # [[rek099,amien,80000],[....,...,...]]
    f.close()
    no_sum = input("Masukkan nomor rekening sumber : ")
    no_tujuan = input("Masukkan nomor rekening tujuan : ")
    trans = eval(input("Masukkan nominal yang akan ditransfer : "))
    if (no_sum.upper() == no_tujuan.upper()):  # rek555 rek555
        print("No rekening sumber dan tujuan tidak boleh sama ")
        print("\n")
        menu()
    # valiadasi rekening sumber
    coba = False
    for a in range(len(list_nasabah)):
        if (no_sum.upper() == list_nasabah[a][0]):
            coba = True
            saldo1 = int(list_nasabah[a][2])
    coba2 = False
    # validasi rekening tujuan
    for b in range(len(list_nasabah)):
        if (no_tujuan.upper() == list_nasabah[b][0]):
            coba2 = True

    # validasi transfer
    if (coba2 == True and coba == False):
        print("No rekening sumber tidak ditemukan,Transfer gagal ")
        print("\n")
        menu()
    elif (coba2 == False and coba == True):
        print("No rekening tujuan tidak ditemukan,Transfer gagal ")
        print("\n")
        menu()
    elif (coba == True and coba2 == True):
        if (saldo1 < trans):
            print("Saldo tidak mencukupi,Transfer gagal")
        elif (saldo1 > trans):
            # untuk Mengecek saldo rekening sumber atau pengirim
            for c in range(len(list_nasabah)):
                if (no_sum.upper() == list_nasabah[c][0]):
                    saldo3 = int(list_nasabah[c][2])
                    jumlah1 = saldo3 - trans
                    list_nasabah[c][2] = jumlah1
            # untuk Mengecek saldo rekening tujuan atau pengirim
            for d in range(len(list_nasabah)):
                if (no_tujuan.upper() == list_nasabah[d][0]):
                    saldo4 = int(list_nasabah[d][2])
                    jumlah2 = saldo4 + trans
                    list_nasabah[d][2] = jumlah2
            print("Transfer sebesar", trans, "dari rekening",
                  no_sum, "ke rekening", no_tujuan, "berhasil")
    f = open('nasabah.txt', 'w+')
    for e in range(len(list_nasabah)):
        data_nasabah = [list_nasabah[e][0],
                        list_nasabah[e][1], list_nasabah[e][2]]
        for target in data_nasabah:
            f.writelines(str(target) + ",")
        f.write("\n")
    f.close()
    no_transfer = "TRF" + \
        ''.join(random.choice(string.digits) for _ in range(3))
    tf = open('transfer.txt', 'a+')
    data_transfer = [no_transfer, no_sum.upper(), no_tujuan.upper(), trans]
    for target in data_transfer:
        tf.writelines(str(target) + ",")
    tf.write("\n")
    tf.close()
    print("\n")
    menu()


def Detail():
    print(" *** LIHAT DAFTAR TRANSFER *** ")
    list_nasabah = []
    f = open('nasabah.txt', 'r')
    for target in f:
        data = target.split(",")
        list_nasabah.append(data)
    f.close()
    norek = input("Masukkan nomor rekening sumber transfer : ")
    test = False
    for a in range(len(list_nasabah)):
        if (norek.upper() == list_nasabah[a][0]):
            test = True
    daftar_transfer = []
    tf = open('transfer.txt', 'r')
    for satu in tf:
        data1 = satu.split(",")
        daftar_transfer.append(data1)
    f.close()
    if (test == True):
        for b in range(len(daftar_transfer)):
            if (norek.upper() == daftar_transfer[b][1]):
                ("Daftar transfer dari rekening", norek, ":")
                no_transfer = str(daftar_transfer[b][0])
                no_rekening = str(daftar_transfer[b][1])
                rek_tujuan = str(daftar_transfer[b][2])
                saldo1 = str(daftar_transfer[b][3])
                print(no_transfer, no_rekening, rek_tujuan,
                      saldo1)  # TRF000 REK555 REK988
        if (norek.upper() not in daftar_transfer[b][1]):
            print("Tidak ada data yang ditampilkan. ")

    elif (test == False):
        print("No rekening tidak ditemukan")
        print("\n")
        menu()
    print("\n")
    menu()


def Bonus():
    print("*** TOP UP *** ")
    print("[1] Pulsa Seluler ")
    print("[2] Pulsa Listrik ")
    list_nasabah = []
    f = open('nasabah.txt', 'r')
    for target in f:
        data = target.split(",")
        list_nasabah.append(data)
    f.close()
    pilih = input("Masukkan Pilihan Top Up Anda : ")
    rekening = input("Masukkan no rekening anda : ")
    test = False
    for a in range(len(list_nasabah)):
        if (rekening.upper() == list_nasabah[a][0]):
            print("No rekening ditemukan")
            test = True
            if (pilih == "1"):
                print("*** Top Up Pulsa Seluler ***")
                pulsa = input("Masukkan nomor handphone anda : ")
                jumlah = eval(input("Masukkan jumlah pulsa anda : "))
                saldo = int(list_nasabah[a][2])
                if (saldo < jumlah):
                    print("Saldo anda tidak mencukupi,Top Up pulsa gagal !! ")
                elif (saldo > jumlah):
                    total = saldo - jumlah
                    list_nasabah[a][2] = total
                    print("Top Up pulsa seluler atas nomor", pulsa,
                          "dengan jumlah ", jumlah, "berhasil ")
            elif (pilih == "2"):
                print("*** Top Up Pulsa Listrik ***")
                pulsa1 = input("Masukkan nomor Listrik anda : ")
                jumlah = eval(input("Masukkan jumlah pulsa Listrik anda : "))
                saldo1 = int(list_nasabah[a][2])
                if (saldo1 < jumlah):
                    print("Saldo anda tidak mencukupi,Top Up pulsa gagal !! ")
                elif (saldo1 > jumlah):
                    total1 = saldo1 - jumlah
                    list_nasabah[a][2] = total1
                    print("Top Up pulsa Listrik atas nomor", pulsa1,
                          "dengan jumlah ", jumlah, "berhasil ")
    if (test == True):
        print()
    elif (test == False):
        print("No rekening tidak ditemukan")
        print("\n")
    f = open('nasabah.txt', 'w+')
    for b in range(len(list_nasabah)):
        data_nasabah = [list_nasabah[b][0],
                        list_nasabah[b][1], list_nasabah[b][2]]
        for target in data_nasabah:
            f.writelines(str(target) + ",")
        f.write("\n")
    f.close()
    no_top = "TOP" + \
        ''.join(random.choice(string.digits) for _ in range(3))
    tp = open('topup.txt', 'a+')
    data_topup = [no_top, pilih, rekening, jumlah]
    for target in data_topup:
        tp.writelines(str(target) + ",")
    tp.write("\n")
    tp.close()
    print("\n")
    menu()


if __name__ == "__main__":
    menu()
