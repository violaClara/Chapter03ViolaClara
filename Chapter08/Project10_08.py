# pembelian beberapa jenis buah sekaligus
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

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

while True:
    belanjaBuah(buah)
    tambahlagi()
    if jawaban=='y':
        continue
    elif jawaban =='n':
            break
total= sum(hargaSemua)
print("Total Harga: ", total)