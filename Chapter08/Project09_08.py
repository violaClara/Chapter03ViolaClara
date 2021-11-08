#program untuk menentukan banyaknya total harga yang harus dibayar oleh seorang pembeli buah

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

#meminta masukan user berupa nama buah yang dibelinya dan berapa Kg banyaknya
beliBuah= input("Nama buah yang dibeli 	:")
if beliBuah in buah:
    kg=int(input("Berapa Kg		:"))
else:
    print("Maaf buah tidak tersedia")
print('-----------------------------')

# Selanjutnya output dari program adalah total harga pembelian.
print("Total Harga: ", buah[beliBuah]*kg)