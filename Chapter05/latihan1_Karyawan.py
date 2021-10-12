#program perhitungan gaji karyawan
kodeKaryawan =input("Masukkan kode karyawan: " )
namaKaryawan=input("Masukkan nama karyawan: ")
golongan= input("Masukkan golongan: ")


if(golongan=='A')or (golongan=='a'):
	gajiPokok= 10000000
	potongan= 2.5
if(golongan=='B')or (golongan=='b'):
	gajiPokok= 8500000
	potongan= 2.0
if(golongan=='C')or (golongan=='c'):
	gajiPokok= 7000000
	potongan= 1.5
if(golongan=='D')or (golongan=='d'):
	gajiPokok= 5500000
	potongan= 1.0

potonganGaji= gajiPokok*(potongan/100)
gajiBersih= gajiPokok-potonganGaji

print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan		:" ,kodeKaryawan)
print("Golongan				:" + golongan)
print("-----------------------------------------------------------")
print("Gaji Pokok			: Rp"+ "{:,}".format(gajiPokok) ) 
print("Potongan (",potongan,"%)		: Rp"+ "{:,}".format(potonganGaji) ) 
print("------------------------------------------------------------")
print("Gaji Bersih			: Rp"+ "{:,}".format( gajiBersih))


