#program mengurutkan secara descending input dari user

try:
    # user diminta menentukan dulu nilai n nya sebelum melakukan input bilangan bulatnya
    banyakBilangan= int(input("Berapa banyak bilangan yang akan diurutkan :"))

    # menerima input berupa bilangan bulat sebanyak n buah
    i=1
    semuaBilangan=[]
    while i<=banyakBilangan:
        bilanganBulat= int(input("Masukan bilangan ke-{} :" .format(i)))
        semuaBilangan.append(bilanganBulat)
        i+=1

    # Selanjutnya program dapat menampilkan semua bilangan bulat tersebut secara terurut descending)
    semuaBilangan.sort(reverse=True)
    print(semuaBilangan)
except ValueError:
    print("hanya masukan bilangan bulat")
