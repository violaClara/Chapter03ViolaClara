#program menampilkan angka ganjil 0/100 dan menghitung banyak angka serta jumlah keseluruhan
p=0
j=0
for i in range(1,100,2):
	p+=1
	print(i)
	j+=i
print("Jumlah: ",p)
print("Jumlah seluruh nilai: ",j)