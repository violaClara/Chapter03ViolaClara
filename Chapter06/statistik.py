#fungsi penjumlahan
def sum(*n):
    hasilJumlah=0
    for m in n:
        hasilJumlah+=m
    return hasilJumlah

#fungsi rata-rata
def average(*n):
    p= sum(*n)    #jumlah nilai
    return p/len(n)

#fungsi nilai maksimal
def maks(*n):
    #mengeset nilai terbesar adalah angka yg pertama 
    nilaiTerbesar= n[0]
    for m in n:
        if m>nilaiTerbesar:
            nilaiTerbesar=m
    return nilaiTerbesar

#fungsi nilai minimal
def min(*n):
    nilaiTerkecil= n[0]
    for m in n:
        if m<nilaiTerkecil:
            nilaiTerkecil=m
    return nilaiTerkecil




        