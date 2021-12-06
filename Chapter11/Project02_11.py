#Program pencatat peminjaman buku perpustakaan
from datetime import *

dataPeminjam= open("Downloads/dataPeminjam.txt", "a")
def data():
#pencatatan data peminjam
    kodeMember= input("Masukkan Kode Member : ")
    namaMember= input("Masukkan Nama Member : ")
    judulBuku= input("Masukkan Judul Buku   : ")
    hariIni=datetime.now()
    hariPengembalian= hariIni+timedelta(days=7)
    dataPeminjam.write("{}|{}|{}|{}|{}\n".format(kodeMember,namaMember,judulBuku,datetime.date(hariIni), datetime.date(hariPengembalian)))

while True:
    data()
    lanjut= input("Lagi? (y/n)")
    if lanjut in ('n', 'no', 'N', 'NO'):
        break

dataPeminjam.close()

