# program tebak angka
from random import randint
print("Hai.. nama saya Mrs. Pupi, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
angkaRandom= randint(0,100)

while True:
    answer= int(input("angka tebakan:" ))
    if answer<angkaRandom:
        print("Salah nih, harusnya lebih ke atas ")
    elif answer>angkaRandom:
        print("Salah nih, harusnya lebih ke bawah")
    else:
        print("Wah kamu berhasil")
        break

