<<<<<<< HEAD
count=0
name=str("Pawan Shinde")
for letter in name:
	if(letter in ["A","E","I","O","U"]):
		count=count+1
print "No of vowels in your name is :",count		
=======
#Program to check how many no.of Vowels present in the entered string
count=0
name=str(raw_input("Enter the name: "))
for letter in name:
	if letter in ['A','E','I','O','U','a','e','i','o','u']:
		count=count+1

print "You have", count,"Vowels"
>>>>>>> b6bc3ac399fc6bd2ebb67e943341861ed82d4bdf
