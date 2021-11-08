#Function yang berfungsi untuk mengurutkan data string tersebut  berdasarkan jumlah karakter
def sortStringByChar(kata):
    kata.sort(reverse=True , key=len)
    return kata

kata=['apel', 'rambutan', 'jeruk']
print(sortStringByChar(kata))












