#function bintang(n)nantinya akan mencetak formasi bintang sebanyak n baris

#fuction bintang
def bintang(n):
    try:
        for i in range(n):
            print(("*"*(2*i+1)).center(2*n-1))
    except TypeError:
        print("n hanya bilangan bulat")
    
bintang(20)