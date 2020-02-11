import math
Temperature = float(input("Enter  the Temperature in (Fahrenheit):-- "))
Speed = float(input("Enter the Speed of wind in (miles per hour):--"))

if Temperature < 50 and Speed > 120 or Speed < 3:
    windchill = 35.74 + 0.6215 * Temperature + (0.4275 * Temperature - 35.75) * math.pow(Speed, 0.16)
    print(windchill)
else:
    print("Please Enter value in range: ")