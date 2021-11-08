#program untuk mencari rata-rata, nilai minimal, dan maksimal dalam list

# function dataStat(x) dengan sebuah parameter x berupa list bilangan
def dataStat(x):
    #rata-rata
    a= sum(x)/len(x)
    #nilai tertinggi dari list x
    b= max(x)
    #nilai terendah dari list x
    c= min(x)
# nilai balikan (return value) berupa list juga yang berisi [a, b, c]
# a adalah nilai rata-rata dari list bilangan x, b adalah nilai tertinggi dari list x, dan c adalah nilai terendah dari list x
    listABC=[a,b,c]
    return listABC

listKu=[9,8,9]
print(dataStat(listKu))
