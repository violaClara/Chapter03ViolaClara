#program kelullusan siswa disertai penyebab ketidaklulusan
nilaiBhsIndo =int(input("Masukkan nilai Bhs Indonesia: "))
nilaiIPA=int(input("Masukkan nilai IPA: "))
nilaiMate= int(input("Masukkan nilai Matematika: "))
if(nilaiMate>100 or nilaiMate<0) or (nilaiIPA>100 or nilaiIPA<0) or (nilaiBhsIndo>100 or nilaiBhsIndo<0):
    print("Maaf input ada yang tidak valid")

elif nilaiMate>70:
    if(nilaiBhsIndo>=60 and nilaiIPA>=60 ):
        status="LULUS"

    else:
        status="TIDAK LULUS"

    print("Status kelulusan: "+ status)


else:
    status= "TIDAK LULUS"
    print("Status kelulusan: "+ status)

if(status=="TIDAK LULUS"):
    print("Sebab: ")
    if(nilaiBhsIndo<60):
        print("Nilai bahasa Indonesia kurang dari 60")
    if(nilaiIPA<60):
        print("Nilai IPA kurang dari 60")
    if(nilaiMate<=70):
        print("Nilai matematika kurang dari/sama dengan 70")
    
    