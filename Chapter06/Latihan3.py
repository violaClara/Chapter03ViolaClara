#program menggunakan fungsi faktorial untuk mencari kombinasi dan permutasi
def faktorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p  
#fungsi Kombinasi
def C(a,b):
    hasilKombinasi= faktorial(a)/(faktorial(b)*faktorial(a-b))
    print(hasilKombinasi)

#fungsi Permutasi
def P(a,b):
    hasilPermutasi= faktorial(a)/faktorial(a-b)
    print(hasilPermutasi)

C(5,3)
P(10,7)

