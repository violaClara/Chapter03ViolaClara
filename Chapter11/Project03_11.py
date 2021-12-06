#Program pencari data peminjam buku perpustakaan
from datetime import *
from Project01_11 import diffDate

#mengambil data dari file txt
dataPeminjam= open("Downloads/dataPeminjam.txt", "r")
dataIsi= dataPeminjam.read().splitlines()
dataPeminjam.close()
data=[]
for i in range(0, len(dataIsi)):
    data.append(dataIsi[i].split("|"))

#pencarian data
kodeCari= input("Masukkan Kode Member: ")
print("")
for i in range (0, len(data)):
    if data[i][0]==kodeCari:
        selisih= diffDate(data[i][4])*(-1)
        if selisih <=0:
            selisih=0
        print("Data Peminjaman Buku")
        print("Kode Member              : ", data[i][0])
        print("Nama Member              : ", data[i][1])
        print("Judul Buku               : ", data[i][2])
        print("Tanggal Mulai Peminjaman : ", data[i][3])
        print("Tanggal Maks Peminjaman  : ", data[i][4])
        print("Tanggal Pengembalian     : ", datetime.date(datetime.now()))
        print("Terlambat                : ", selisih, " hari" )
        print("Denda                    : Rp", selisih*2000)
    elif i==len(data)-1:
        print("Maaf data tidak ada")



