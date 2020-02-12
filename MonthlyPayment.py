import math
principle = int(input("Enter the principle:--"))
Year = int(input("Enter the number of years:--"))
Rate = int(input("Enter the Rate Percent:--"))
n = 12 * Year
r = Rate/(12*100)
Payment = principle * Rate/1-(pow(1+r, -n))
print(Payment)
