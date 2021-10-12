#program perhitungan gaji karyawan beserta tunjangan
kodeKaryawan =input("Masukkan kode karyawan: " )
namaKaryawan=input("Masukkan nama karyawan: ")
golongan= input("Masukkan golongan: ")
status= int(input("Masukkan status (1: menikah 2: belum): "))
if status==1:
	jumlahAnak= int(input("Masukkan jumlah anak: "))



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

if status== 1:
	tunjanganStatus= 10/100*gajiPokok
	tunjanganAnak= (5/100*jumlahAnak)*gajiPokok
else:
	tunjanganStatus=0
	tunjanganAnak= 0

gajiKotor= gajiPokok+tunjanganAnak+tunjanganStatus
potonganGaji= gajiKotor*(potongan/100)
gajiBersih= gajiKotor-potonganGaji

print("==========================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan		:" ,kodeKaryawan)
print("Golongan				:" + golongan)
print("-----------------------------------------------------------")
print("Gaji Pokok			: Rp"+ "{:,}".format(gajiPokok) ) 
print("Tunjangan istri/suami: Rp" + "{:,}".format(tunjanganStatus))
print("Tunjangan anak		: Rp"+ "{:,}".format(tunjanganAnak))
print("-------------------------------------------------------------")
print("Gai kotor		: Rp"+ "{:,}".format(gajiKotor) ) 
print("Potongan (",potongan,"%)		: Rp"+ "{:,}".format(potonganGaji) ) 
print("------------------------------------------------------------")
print("Gaji Bersih			: Rp"+ "{:,}".format( gajiBersih))
