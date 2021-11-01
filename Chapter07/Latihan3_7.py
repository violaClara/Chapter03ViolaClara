#program untuk menhitung rata-rata yang ada exception handlingnya
#fungsi untuk menanyakan apakah user ingin menambah bilangan lagi
def tambahBilangan():
    global jawaban
    jawaban= input("Lagi (y/n)? : ")
#header
print("-----------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("-----------------------------")

#perintah untuk menghitung 
sum=0
banyakdata=0
while True:
    try:
        angka= int(input("Masukkan bilangan bulat: "))
        sum+=angka
        banyakdata+=1
        tambahBilangan()
        if jawaban=='y':
            continue
        elif jawaban =='n':
            break
        
        #bila jawaban user selain y atau n
        while jawaban!='y' and jawaban!='n':
            print("Hanya masukan y/n")
            tambahBilangan()

    except ValueError:
        print("Hanya masukan bilangan bulat")

print("Rata-ratanya adalah ", sum/banyakdata)