#program Python untuk membaca data sebuah file text yang berisi serangkaian bilangan dengan format: bil1|bil2
#outputnya adalah sebuah file text lain yang isinya merupakan hasil penjumlahan bil1 dan bil2 pada setiap barisnya

try:
    #membuka dan membaca file
    data5r=open("Downloads/dataProject5_1.txt","r")
    isiData5r=data5r.read().splitlines()
    data5r.close()

    #memisahkan bilangan 1 dan 2 
    for i in range(0,len(isiData5r)):
        pemisah=isiData5r[i].split("|")
        del isiData5r[i]
        isiData5r.insert(i, pemisah)

    #membuat file baru dengan hasil penjumlahan
    data5w=open("Downloads/dataProject5_2.txt", "w")
    for i in range(0, len(isiData5r)):
        data5w.write("{}\n".format((int(isiData5r[i][0])+int(isiData5r[i][1]))))
    data5w.close()
except FileNotFoundError:
    print("maaf file tidak ada")
