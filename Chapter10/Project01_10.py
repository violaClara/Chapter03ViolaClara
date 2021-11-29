#program Python untuk membaca sebuah file text berisi beberapa data bilangan yang akan dihitung jumlah bilangan genap dan ganjilnya
try:
    #membuka dan membaca file
    dataBilangan= open("Downloads/dataProject1.txt","r")
    angka=dataBilangan.readlines()
    dataBilangan.close()

    #menghitung banyaknya angka ganjil dan genap
    bilanganGenap=0
    bilanganGanjil=0
    for i in range(0,len(angka)):
        if int(angka[i])%2==0:
            bilanganGenap+=1
        else:
            bilanganGanjil+=1
            
    #menampilkan banyaknya bilangan
    print("Banyaknya bilangan genap: ",bilanganGenap)
    print("Banyaknya bilangan ganjil: ",bilanganGanjil)
except FileNotFoundError:
    print("Maaf file tidak ditemukan")