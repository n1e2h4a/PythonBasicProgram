import cmath
a = int(input("Enter  First value to find roots:-"))
b = int(input("Enter Second value to find roots:-"))
c = int(input("Enter Third value to find roots:-"))

#Equation= ax**2+bx+c
Discriminant = (b**2) - (4*a*c)
FirstRoot = (-b-cmath.sqrt(Discriminant))/(2*a)
SecondRoot = (+b-cmath.sqrt(Discriminant))/(2*a)
print("The Roots of equation are {0} and {1}".format(FirstRoot, SecondRoot))
