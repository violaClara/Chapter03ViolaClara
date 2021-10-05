#kode untuk mengetahui biaya total dari penggunaan sewa mobil

selisihJamDalamMenit= (23-6)*60
selisihMenit=50-0
selisihTotal=selisihJamDalamMenit + selisihMenit
tarif12Jam=200000 
duaBelasJamDalamMenit=12*60
biayaTambahanperjam=10000
jamTambahanDalamMenit=selisihTotal-duaBelasJamDalamMenit 
biayadenda= 10000*jamTambahanDalamMenit/60
print("Biaya total penggunaan sewa mobil adalah Rp%.2f" %(biayadenda+tarif12Jam))