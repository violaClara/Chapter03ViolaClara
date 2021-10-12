bil=0
if bil>0:
	print("Bilangan positif")
elif bil<0:
	print("Bilangan negatif")
else:
	print("Bilangan nol")

a= -2
b= -7
if(a>0) and (b>0):
	print("Keduanya positif")
elif((a>0) and (b<0))or((a<0) and (b>0)):
	print("Bilangan positif dan negatif")
elif (a<0) and (b<0):
	print("Keduanya negatif")