#program mengurutkan nama mahasiswa beserta menampilkan banyaknya karakter



# input berupa nama mahasiswa (string) sebanyak n data
namaMahasiswa=[]
while True:
    namaInput= input("Masukan nama Mahasiswa: ")
    if namaInput=='':
        break
    namaMahasiswa.append(namaInput)

# menampilkan semua nama mahasiswa yang tersusun secara urut (ascending) 
namaMahasiswa.sort()
for i in range (len(namaMahasiswa)):
    print(namaMahasiswa[i], end=' ')

# serta banyaknya karakter yang menyusun setiap nama mahasiswa tersebut 
    print("({} karakter)".format(len(namaMahasiswa[i])))



