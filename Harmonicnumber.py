HarmonicNumber=int(input("Enter the Number:-"))
if HarmonicNumber<=0:
 print("Please Enter Valid Number")
else:
        number = 1
	for i in range(2,HarmonicNumber+1):
		number=number+(1+i)
	print("Nth Harmonic Number:-", (number))


