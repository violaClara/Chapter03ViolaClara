#program Python untuk membaca input berupa: nim, nama mhs, alamat
#disimpan ke dalam file text, dengan format: nim|nama|alamat

#membuat dictionary untuk container data
dataMahasiswa={'nim':[],'nama':[],'alamat':[]}

#memasukkan data
while True: 
    nimInput=input("Masukan NIM: ")
    namaInput=input("Masukan Nama Mhs: ")
    alamatInput=input("Masukan Alamat: ")
    dataMahasiswa['nim'].append(nimInput)
    dataMahasiswa['nama'].append(namaInput)
    dataMahasiswa['alamat'].append(alamatInput)
    masukanLagi=input("Tambahkan input? (y/n): ")
    if masukanLagi in ('n','N'):
        break
#membuat file text
dataText=open("Downloads/dataProject2.txt", "w")
for i in range (0, len(dataMahasiswa['nim'])):
    dataText.write("{}|{}|{}\n".format(dataMahasiswa['nim'][i],dataMahasiswa['nama'][i],dataMahasiswa['alamat'][i]))
dataText.close()