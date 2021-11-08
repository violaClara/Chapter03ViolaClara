#program untuk menampilkan data sayur, menambah, dan menghapusnya

# data sayur sebagai berikut: bayam, kangkung, wortel, selada
dataSayur=['bayam','kangkung','wortel','selada']
# Pilihan Menu
while True:
    print("Menu: ")
    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur")
    print("D. exit")
    pilihan= input("Pilihan Anda: ")

    if pilihan=='A' or pilihan=='a':
        tambahanSayur= input("Masukan nama sayur: ")
        dataSayur.append(tambahanSayur)
    elif pilihan=='B' or pilihan=='b':
        hapusSayur=input("Masukan sayur yang akan dihapus: ")
        if hapusSayur in dataSayur:
            dataSayur.remove(hapusSayur)
        else:
            print("Maaf nama sayur tidak ada")
    elif pilihan=='C' or pilihan=='c':
        print("----------------------")
        print("Data sayur saat ini: ")
        for i in range(len(dataSayur)):
            print(dataSayur[i])
        print("----------------------")
    elif pilihan=='D' or pilihan=='d':
        break

