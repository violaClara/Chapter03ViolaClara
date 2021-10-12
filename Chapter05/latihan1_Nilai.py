#program kelulusan siswa
nilaiBhsIndo =int(input("Masukkan nilai Bhs Indonesia: "))
nilaiIPA=int(input("Masukkan nilai IPA: "))
nilaiMate= int(input("Masukkan nilai Matematika: "))

if(nilaiMate>70):
    if(nilaiBhsIndo>=60) and (nilaiIPA>=60):
        status="LULUS"
    else:
        status="TIDAK LULUS"
else:
    status= "TIDAK LULUS"

print("Status kelulusan: " + status)
