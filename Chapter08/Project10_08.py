# pembelian beberapa jenis buah sekaligus
hargaSemua=[]

#fungsi untuk mengihitung total harga belanjaan
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

#fungsi menanyakan barang tambahan
def tambahlagi():
    global jawaban
    jawaban= input("Lagi (y/n)? : ")

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

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