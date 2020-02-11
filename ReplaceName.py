Welcome="Hello username , How are you?"
Name=raw_input("Enter Your Beautiful Name :-")
if len(Name) > 3:
	print(Welcome.replace("username",Name))
	
else:
	print(" Please Enter Proper Or Full-Name")
