# function diffDate(x) untuk menghitung selisih hari dari tanggal hari ini dengan tanggal x
from datetime import *

def diffDate(x):
    try:
        tlDicari= datetime.strptime(x, '%Y-%m-%d')
        tlHariIni= datetime.now()
        selisih= tlDicari-tlHariIni
        selisihHari= selisih.days
        return selisihHari+1
    except TypeError:
        print('Maaf ada yang salah')

