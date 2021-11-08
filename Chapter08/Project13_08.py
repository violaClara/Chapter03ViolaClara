#program untuk menampilkan nilai akhir mahasiswa yang tertinggi

#function untuk mendapatkan nim dan nama mahasiswa yang memiliki nilai akhir tertinggi
def tertinggiAkhir(nilaiMhs):
    nimLi=[]
    nilaiMid=[]
    namaLi=[]
    nilaiUas=[]
    nilaiAkhir=[]
    for i in range(len(nilaiMhs)):
        nilaiMid.append(nilaiMhs[i]['mid'])
        nimLi.append(nilaiMhs[i]['nim'])
        namaLi.append(nilaiMhs[i]['nama'])
        nilaiUas.append(nilaiMhs[i]['uas'])

    # Nilai Akhir = (nilai MID + 2 Nilai UAS)/3
    for i in range (len(nimLi)):
        nilaiAkhir.append((nilaiMid[i]+2*nilaiUas[i])/3)

    tertinggi= max(nilaiAkhir)
    posisi=nilaiAkhir.index(tertinggi)
    print("Nilai tertinggi adalah {} nim ({}) dengan nilai akhir {} " .format(namaLi[posisi],nimLi[posisi],nilaiAkhir[posisi]))

nilaiMhs= [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 
	        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

tertinggiAkhir(nilaiMhs)


