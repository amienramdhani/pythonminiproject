def Transfer():
    print("*** TRANSFER ***")
    list_nasabah = [] #list kosong untuk menyimpan data nasabah.txt kedalam multiple list
    f = open('nasabah.txt', 'r') #membuka file nasabah dan membacanya (r)
    for target in f:    
        data = target.split(",") #membuat data menjadi list dengan fungsi spilt dan dipisahkan dengan ,
        list_nasabah.append(data)  # menambahkan list data ke dalam list_nasabah
    f.close() #tutup file
    no_sum = input("Masukkan nomor rekening sumber : ") 
    no_tujuan = input("Masukkan nomor rekening tujuan : ")
    trans = eval(input("Masukkan nominal yang akan ditransfer : "))
    if (no_sum.upper() == no_tujuan.upper()):  #jika no rek sumber dijadikan besar(upper) sama dengan no rek tujuan dijadikan besar(upper)
        print("No rekening sumber dan tujuan tidak boleh sama ") 
        print("\n")
        menu() #balik lagi ke menu
    # valiadasi rekening sumber
    coba = False #false untuk syarat 
    for a in range(len(list_nasabah)): #membaca dan mengecek list nasabah berdasarkan panjangnya
        if (no_sum.upper() == list_nasabah[a][0]): 
            coba = True #jika syaratnya terpenuhi maka coba tadi yang nilai nya false menjadi nilai true
            saldo1 = int(list_nasabah[a][2]) #kemudian ambil saldo nya di index ke 2
    coba2 = False #kalau syaratnya tidak memenuhi maka cobanya tetap false
    # validasi rekening tujuan
    for b in range(len(list_nasabah)): #sama yang diatas untuk membaca dan mengecek list nasabah untuk mencari rekening tujuan
        if (no_tujuan.upper() == list_nasabah[b][0]):
            coba2 = True

    # validasi transfer
    if (coba2 == True and coba == False): #jika no sumber ditemukan dan no tujuan tidak ditemukan maka 
        print("No rekening sumber tidak ditemukan,Transfer gagal ") #cetak
        print("\n") #enter 
        menu() #kembali ke menu
    elif (coba2 == False and coba == True): #jika no tujuan salah dan no sumber benar ditemukan maka
        print("No rekening tujuan tidak ditemukan,Transfer gagal ") #cetak
        print("\n")
        menu()
    elif (coba == True and coba2 == True): #jika no sumber dan no tujuan ditemukan maka 
        if (saldo1 < trans): #cek saldo pengirim atau rekening sumber kurang dari jumlah yang ingin ditrasfer 
            print("Saldo tidak mencukupi,Transfer gagal") #jika iya cetak
        elif (saldo1 > trans): #jika saldonya lebih dari jumlah transfer maka
            # untuk Mengecek saldo rekening sumber atau pengirim
            for c in range(len(list_nasabah)): #mengambil data rek sumber
                if (no_sum.upper() == list_nasabah[c][0]):
                    saldo3 = int(list_nasabah[c][2]) #mengambil saldo rek sumber 
                    jumlah1 = saldo3 - trans #saldo pengirim dikurang jumlah transfer
                    list_nasabah[c][2] = jumlah1 #ganti saldo pengirim jadi jumlah tadi setalh dilakukan penguarangn
            # untuk Mengecek saldo rekening tujuan atau pengirim
            for d in range(len(list_nasabah)): #sama sperti yang diatas kalau yang ini saldo penerima ditambah dengan jumlah transfernya
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
            f.writelines(str(target) + ",") #mengganti data nasabah yang lama dengan data nasabah yang baru dari list nasabah tadi yang sudah di proses
        f.write("\n")
    f.close()
    no_transfer = "TRF" + \
        ''.join(random.choice(string.digits) for _ in range(3)) #membuat kode transfer random 
    tf = open('transfer.txt', 'a+')
    data_transfer = [no_transfer, no_sum.upper(), no_tujuan.upper(), trans] #list yang menyimpan no transfer no rekening sumber rek tujuan dan jumlah transfer
    for target in data_transfer:
        tf.writelines(str(target) + ",") #menuliskan list nasabah tadi kedalam transfer,txt
    tf.write("\n")
    tf.close()
    print("\n")
    menu()

