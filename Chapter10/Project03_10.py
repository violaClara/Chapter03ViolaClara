#program Python untuk membaca data file text yang dihasilkan dan menampilkannya dalam bentuk list

try:
    #membuka file data
    dataTextMahasiswa= open("Downloads/dataProject2.txt", "r")
    dataMhs=[]
    isiDataMahasiswa= dataTextMahasiswa.read().splitlines()
    data=[]
    for i in range(0,len(isiDataMahasiswa)):
        data.append(isiDataMahasiswa[i].split("|"))
        
    #membuat dictionary dan memasukkannya ke list
    for i in range(0,len(data)):
        conSementara= {}
        conSementara['nim']=data[i][0]
        conSementara['nama']=data[i][1]
        conSementara['alamat']=data[i][2]
        dataMhs.append(conSementara)
    print(dataMhs)
except FileNotFoundError:
    print("maaf file tidak ada")
