#Modifikasi function yang ada dari hasil nomor 2, formasi berbentuk wajik
import math

#fungsi formasi bintang berbentuk wajik untuk bilangan ganjil
def bintang(n):
    try:
        #bila yang dimasukan genap 
        if(n%2==0):
            print("Hanya masukan bilangan ganjil")

        else:
            #formasi bintang dari sedikit ke banyak
            listFormasi= []
            for i in range(math.ceil(n/2)):
                formasi=("*"*(2*i+1)).center(2*n-1)
                listFormasi.append(formasi)
                print(formasi)
            #formasi bintang dari banyak ke sedikit
            for i in range(len(listFormasi)):
                indexFormasi=len(listFormasi)-1-i
                if (indexFormasi==len(listFormasi)-1):
                    continue
                print(listFormasi[indexFormasi])
    except TypeError:
        print("Hanya masukan bilangan bulat ganjil")

    
bintang(13)

