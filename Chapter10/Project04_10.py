#program Python untuk mencari data mahasiswa berdasarkan nim nya
try:
    #membuka dan membaca file data
    dataMahasiswa=open("Downloads/dataProject2.txt", "r")
    isiData=dataMahasiswa.read().splitlines()
    dataMahasiswa.close()
    #memisahkan data
    data=[]
    for i in range(0,len(isiData)):
        data.append(isiData[i].split("|"))
    #mencari data berdasarkan nim    
    cari=input("Masukkan NIM yang mau dicari:")
    for i in range(0,len(data)):
        if cari==data[i][0]:
            print("Data Mahasiswa")
            print("NIM      :",data[i][0])
            print("Nama     :",data[i][1])
            print("Alamat   :",data[i][2])
        elif i==len(data)-1:
            print("Maaf data tidak ada")
except FileNotFoundError:
    print("maaf file tidak ada")

