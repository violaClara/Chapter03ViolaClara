#program menambahkan data buah dan membeli buah

#data buah
buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
while True:
    print("Menu: ")
    print("A. Tambah data buah")
    print("B. Beli buah")
    print("C. exit")
    pilihan= input("Pilihan Anda: ")

#Menu A
    if pilihan=='A' or pilihan=='a':
        namaBuah=input("Masukkan nama buah :")
        if namaBuah in buah.keys():
            print("buah sudah ada")
            break
        try:
            hargaSatuan= int(input("Masukkan harga satuan :"))
            buah[namaBuah]=hargaSatuan

            #keys dan value dijadikan list
            keys= list(buah.keys())
            valu= list(buah.values())

            #menampilkan data buah
            print("Data buah: ")
            for i in range(len(buah)):
                print ("- {} (Harga Rp {}) " .format(keys[i], valu[i]))
        except ValueError:
            print("Maaf hanya masukan angka")
        
#Menu B
    elif pilihan=='B' or pilihan=='b':
        hargaSemua=[]
        def belanjaBuah(buah):
            try:
                beliBuah= input("Nama buah yang dibeli 	:")
                if beliBuah in buah:
                    kg=int(input("Berapa Kg		:"))
                    print('-----------------------------')
                hargaSemua.append(buah[beliBuah]*kg)
            except KeyError:
                print("maaf buah tidak tersedia")
            except ValueError:
                print("Maaf hanya masukan angka")

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
            #bila jawaban user selain y atau n
            elif jawaban!='y' and jawaban!='n':
                print("Hanya masukan y/n")
                tambahlagi()
                if jawaban=='y':
                    continue
                elif jawaban =='n':
                    break
        total= sum(hargaSemua)
        print("Total Harga: ", total)
    elif pilihan=='C' or pilihan=='c':
        break
