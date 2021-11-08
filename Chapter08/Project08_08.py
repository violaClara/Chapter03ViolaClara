#program untuk mencari rata-rata dari harga buah

#function untuk menentukan rata-rata harga satuan dari keseluruhan buah yang ada
def rataHargaBuah(buah):
    hargaBuah= list(buah.values())
    return sum(hargaBuah)/len(hargaBuah)

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(rataHargaBuah(buah))