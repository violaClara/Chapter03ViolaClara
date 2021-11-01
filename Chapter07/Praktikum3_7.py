file= open("d:/data_2.txt", "r")
sum=0
try:
    for data in file:
        sum=sum+int(data)
    print(sum)
except ValueError:
    print("Ada data yang bukan integer")