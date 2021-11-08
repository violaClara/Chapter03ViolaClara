#program untuk membuat list berupa hasil kuadrat bilangan dalam list lain

def kuadrat(bil):
    try:
        hasilKuadrat=[]
        for i in bil:
            hasilBilangan=i**2
            hasilKuadrat.append(hasilBilangan)
        print(hasilKuadrat)
    except TypeError:
        print("Maaf data ada yang bukan bilangan")

bil=[3,5,7,3,5]
kuadrat(bil)
