print("It's first statement of if-elif")
print("Enter the character")
char=raw_input()
if ord(char)>=65 and ord(char)<=90:
	if char in ['A','E','I','O','U']:
		print("You enter the Capital letter Vowel")
	else:
		print("You enter the Consonent")	
elif ord(char)>=97 and ord(char)<=122:
	if char in ['a','e','i','o','u']:
		print("You enter the Small letter Vowel")
	else:
		print("You enter the Consonent")
else:
	print("You have not enterd character")		
print("")
print("EOF IF-ELIF Statement")