#program Python yang dapat digunakan untuk mengubah kembali suatu file teks berisi teks hasil penyandian 
# menggunakan Sandi Caesar menjadi file teks aslinya
try:
    fileEnskripsi= open("Downloads/dataProject6_2.txt", "r")
    n=2
    #mengubah huruf ke kode ASCII
    container=[]
    while True:
        bacaTeks= fileEnskripsi.read(1)
        if not bacaTeks:
            break
        keOrd= ord(bacaTeks)
        container.append(keOrd)

    #Menggeser huruf kembali seperti semula
    for i in range(0,len(container)):
        if container[i]!=32:
            if (container[i]>=65) and (container[i]<=90) :
                penambahan=(container[i]-n+65)%26+65
            else:
                penambahan=(container[i]-n+97)%26+97
            del container[i]
            container.insert(i, chr(penambahan))
        else:
            container.insert(i, chr(container[i]))
            del container[i+1]
            continue

    #membuat file hasil pemecahan sandi
    hasilAkhir=''.join(container)
    fileAsli= open("Downloads/dataProject7.txt", "w")
    fileAsli.write(hasilAkhir)

    #menutup file
    fileAsli.close()
    fileEnskripsi.close()
except FileNotFoundError:
    print("maaf file tidak ada")