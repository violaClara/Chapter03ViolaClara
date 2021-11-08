#program untuk mengetahui harga buah termahal dari dictionary

# function untuk menampilkan nama buah yang harga satuannya paling mahal
def hargaTermahal(buah):
    termahal=max(buah.values())
    #buat list dari keys dan valuesnya agar keys dapat ditampilkan
    keys = list(buah.keys())
    valus = list(buah.values())
    print(keys[valus.index(termahal)])

buah= {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
hargaTermahal(buah)