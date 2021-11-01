#program untuk menampilkan isi file dari input user
try:
    # input sebagai isi variabel namaFile 
    namaFile= str(input("Masukkan nama file (termasuk pathnya): "))
    file= open(namaFile , "r")

    #output berupa isi file
    print("Isi file "+namaFile+" adalah:")
    print(file.read())

#exception handling bila file tidak ditemukan
except FileNotFoundError:
    print("Maaf nama file dan/atau path salah")

