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
        while jawaban!='y' and jawaban!='n':
            print("Hanya masukan y/n")
            tambahlagi()
    fileDibuka.close()
except FileNotFoundError:
    print("Maaf nama file dan/atau path salah")


