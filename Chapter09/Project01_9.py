#function ubahHuruf(teks, a, b) 
#digunakan untuk mengubah huruf pada parameter a dengan huruf yang ada di b dari suatu string teks

#fungsi menggunakan replace() untuk mengubah huruf
def ubahHuruf(teks, a, b):
    mengubahHuruf=teks.replace(a,b)
    print(mengubahHuruf)


ubahHuruf("Matematika","t","s")