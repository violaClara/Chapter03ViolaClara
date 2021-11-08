#program menambahkan data buah dan membeli buah

#data buah
buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
while True:
    print("Menu: ")
    print("A. Tambah data buah")
    print("B. Beli buah")
    print("C. Hapus buah")
    print("D. exit")
    pilihan= input("Pilihan Anda: ")

#Menu A
    if pilihan=='A' or pilihan=='a':
        namaBuah=input("Masukkan nama buah :")
        if namaBuah in buah.keys():
            print("buah sudah ada")
            break
        hargaSatuan= int(input("Masukkan harga satuan :"))
        buah[namaBuah]=hargaSatuan

        #keys dan value dijadikan list
        keys= list(buah.keys())
        valu= list(buah.values())

        #menampilkan data buah
        print("Data buah: ")
        for i in range(len(buah)):
            print ("- {} (Harga Rp {}) " .format(keys[i], valu[i]))
        
#Menu B
    elif pilihan=='B' or pilihan=='b':
        hargaSemua=[]
        def belanjaBuah(buah):
            beliBuah= input("Nama buah yang dibeli 	:")
            if beliBuah in buah:
                kg=int(input("Berapa Kg		:"))
            else:
                print("Maaf buah tidak tersedia")
            print('-----------------------------')
            hargaSemua.append(buah[beliBuah]*kg)

        def tambahlagi():
            global jawaban
            jawaban= input("Lagi (y/n)? : ")
        while True:
            belanjaBuah(buah)
            tambahlagi()
            if jawaban=='y':
                continue
            elif jawaban =='n':
                    break
        total= sum(hargaSemua)
        print("Total Harga: ", total)
    elif pilihan=='C' or pilihan=='c':
        dihapus=input("Masukan nama buah yang ingin dihapus: ")
        if dihapus not in buah:
            print("Maaf buah tersebut tidak ada")
            break
        del buah[dihapus]
    elif pilihan=='D' or pilihan=='d':
        break
