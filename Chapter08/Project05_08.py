#program untuk membuat list berupa hasil kuadrat bilangan dalam list lain

def kuadrat(bil):
    hasilKuadrat=[]
    for i in bil:
        hasilBilangan=i**2
        hasilKuadrat.append(hasilBilangan)
    print(hasilKuadrat)

bil=[3,5,7,3]
kuadrat(bil)
