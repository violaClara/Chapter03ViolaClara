#function shuffleString(x, n) untuk melakukan pengacakan huruf-huruf pada sebuah kata.
import random

def suffleString(x,n):
    banyakKemungkinan=1
    for i in range(1,len(x)+1):
        banyakKemungkinan=i*banyakKemungkinan

    # apakah permintaan user melebihi kemungkinan
    if n>banyakKemungkinan:
        print("Maaf permintaan terlalu banyak")
    
    #bila permintaan user tidak melebihi kemungkinan perintah pengacakan akan dijalankan
    else:
        listHasil=[]
        while True:
            if len(listHasil)==n:
                break
            hasilPengacakan= ''.join(random.sample(x,len(x)))
            if hasilPengacakan in listHasil:
                continue
            listHasil.append(hasilPengacakan)
        print(listHasil)
    

suffleString("akui",24)