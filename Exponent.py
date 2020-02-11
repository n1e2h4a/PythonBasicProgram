Exponent=int(input('Enter the Exponent Value:- '))
Number=2
Result = 1
i=1
while(i <= Exponent):
	Result=Result * Number
	i=i+1
	if ((Result%4==0) or ((Result%400==0) and (Result%100!=0))): 				
		print("%d = is a Leap Year" %Result)
	else:
		print("%d = is  not a Leap Year" %Result)
	
