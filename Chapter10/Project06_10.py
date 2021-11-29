#program Python untuk melakukan enkripsi menggunakan sandi Caesar, sehingga didapatkan file teks hasil penyandian

namaPath=input("Ketikkan nama file sekaligus pathnya: ")
try:
    #membuka file yang akan disandikan
    fileTeks=open(namaPath, "r")

    n=int(input("ketikkan pergeseran: "))
    container=[]

    #mengubah huruf ke kode ASCII
    while True:
        bacaTeks= fileTeks.read(1)
        if not bacaTeks:
            break
        keOrd= ord(bacaTeks)
        container.append(keOrd)

    #Menggeser huruf
    for i in range(0,len(container)):
        if container[i]!=32:
            if (container[i]>=65) and (container[i]<=90) :
                penambahan=(n-65+container[i])%26+65
            else:
                penambahan=(n-97+container[i])%26+97
            del container[i]
            container.insert(i, chr(penambahan))
        else:
            container.insert(i, chr(container[i]))
            del container[i+1]
            continue
    #menuliskan hasil ke dalam file lain
    hasilAkhir=''.join(container)
    fileEnskripsi= open("Downloads/dataProject6_2.txt", "w")
    fileEnskripsi.write(hasilAkhir)

    fileTeks.close()
    fileEnskripsi.close()
except FileNotFoundError:
    print("maaf file tidak ada")


