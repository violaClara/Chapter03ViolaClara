#program untuk memberi tambahan data pada suatu file, bila tidak ada akan membuat file baru
def tambahlagi():
    global jawaban
    jawaban= input("Lagi (y/n)? : ")

try:
    # input sebagai isi variabel namaFile 
    namaFileDrtr= str(input("Masukkan nama file (termasuk pathnya): "))

    #membuka file
    fileDibuka= open(namaFileDrtr , "a")

    #input data yang akan ditambah
    while True:
        tambahan= input("Data yang mau ditambahkan: ")
        fileDibuka.write(tambahan)
        tambahlagi()
        if jawaban=='y':
            continue
        elif jawaban =='n':
            break
        
    #bila jawaban user selain y atau n
        elif jawaban!='y' and jawaban!='n':
            print("Hanya masukan y/n")
            tambahlagi()
            if jawaban=='y':
                continue
            elif jawaban =='n':
                break
    fileDibuka.close()
except FileNotFoundError:
    print("Maaf nama file dan/atau path salah")


