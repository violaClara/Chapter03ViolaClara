#Function yang berfungsi untuk mengurutkan data string tersebut  berdasarkan jumlah karakter
def sortStringByChar(kata):
    kata.sort(reverse=True , key=len)
    return kata
try:
    kata=['apel', 'rambutan', 'jeruk']
    print(sortStringByChar(kata))
except TypeError:
    print("Maaf ada data yang bukan string")












