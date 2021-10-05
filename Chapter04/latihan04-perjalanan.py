#mengetahui perkiraan waktu sampai Pak Amir menempuh perjalanan dari kota A ke B ke C
import math
lamaperjalananAkeBMenit=125/62*60
lamaperjalananBkeCMenit=256/70*60
totalLamaPerjalananJam=(lamaperjalananAkeBMenit + lamaperjalananBkeCMenit + 45)/60
tambahanJam= math.floor(totalLamaPerjalananJam)
tambahanMenit=round((totalLamaPerjalananJam - tambahanJam)*60)
print("Pak Amir sampai di kota C kira-kira pukul ",6+tambahanJam, ".",0+tambahanMenit)
