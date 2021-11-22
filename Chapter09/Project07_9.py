#Program untuk menghasilkan tampilan tabel dari sebuah list

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
#header
print("=====================================================================================")
print("NIM		NAMA MAHASISWA		TGL LAHIR		TEMPAT LAHIR")
print("-------------------------------------------------------------------------------------")

#list container untuk menampung data2
data=[]
ttl=[]
ttlFIX=[]

#loop untuk memisahkan
for i in range (len(mhs)):
    data.append(mhs[i].split(":"))
    ttl.append((data[i][2]).split("-"))
    
#loop untuk membentuk ttl yang diinginkan
for i in range(len(ttl)):
    ttlFIX.append('/'.join(ttl[i][::-1]))

#menampilkan data
for i in range(len(data)):
    print(data[i][0].ljust(16), end='')
    print(data[i][1].ljust(24),end='')
    print(ttlFIX[i].ljust(24),end='')
    print(data[i][3].ljust(5))

print("-------------------------------------------------------------------------------------")
