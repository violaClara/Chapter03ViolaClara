a = [1, 5, 6, 3, 6, 9, 11, 20, 12] 
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)

#Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b
a.append(4)
b.append(8)
print(a)
print(b)

#sorting secara ascending pada list a dan b
a.sort()
b.sort()
print(a)
print(b)

#list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), 
#dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)
c= a[:8]
d= a[2:10]
print(c)
print(d)

#list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya
e=[]
for i in range(len(c)):
    e.append(c[i]+d[i])
print(e)

#Ubah list e ke dalam tuple
tupleE=tuple(e)
print(tupleE)

#nilai min, maks, dan jumlahan seluruh elemen dari e
print(min(e))
print(max(e))
print(sum(e))

#Buat sebuah string myString 
myString = "python adalah bahasa pemrograman yang menyenangkan"
hurufMyString=set(myString)
print(hurufMyString)

#Urutan secara alfabet himpunan karakter huruf myString
listHurufMyString= list(hurufMyString)
print(listHurufMyString)
listHurufMyString.sort()
print(listHurufMyString)

