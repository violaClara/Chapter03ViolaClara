from random import randint

i=0
while i<10:
	print("Hello world")
	i+=1
print("---------------------------")
i=2
while i<=20:
	print("yuo")
	i+=2

print("------------------------")
i=0
while True:
	print("yes")
	i+=1
	if i==10:
		break
print("----------------")
#kotak bintang ajaib
kolom = 5
baris = 5

i=0
while (i<baris):
	j=0
	while(j<kolom):
		print('*', end='')
		j+=1
	print('')
	i+=1
print("----------------")
baris = 5
i=1
while (i<=baris):
	print('*'*i)
	i+=1

print("-----------------------")

i=0
while True:
	bil= randint(0,10) #0 dan 10 termasuk
	print(bil)
	i+=1
	if bil == 5:
		print("jumlah perulangan:", i)
		break
	
