Temperature = int(input("Enter the temperature "))
Degree = input('(F) or (C)')
if Degree.upper() == "F":
   Fahrenheit = 9.0/5.0 * Temperature + 32
   print(f"temperature converted in {Fahrenheit} Fahrenheit degree")
else:
    Celsius = (Temperature - 32) * 5.0/9.0
    print(f"temperature converted in {Celsius} Celsius Degree")
