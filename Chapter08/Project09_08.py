#program untuk menentukan banyaknya total harga yang harus dibayar oleh seorang pembeli buah

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

try: 
    #meminta masukan user berupa nama buah yang dibelinya dan berapa Kg banyaknya
    beliBuah= input("Nama buah yang dibeli 	:")
    if beliBuah in buah:
        kg=int(input("Berapa Kg		:"))
        print('-----------------------------')

    # Selanjutnya output dari program adalah total harga pembelian.
    print("Total Harga: ", buah[beliBuah]*kg)
except KeyError:
    print("maaf buah tidak tersedia")
except ValueError:
    print("Maaf hanya masukan angka")