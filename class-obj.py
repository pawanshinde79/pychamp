class myclass:
	sample	=	0
	white	=	0
	black	=	0
	gray	=	0
	other	=	0
	color_list	= ['White','Black','Gray']

	def __init__(self, name):
		myclass.name = name
		print "Enter the Color name: "
		myclass.color = raw_input()
		myclass.sample = myclass.sample + 1

	def check_color(self):
		if myclass.color in myclass.color_list:
			if myclass.color == myclass.color_list[0]:
				myclass.white = myclass.white + 1
			elif myclass.color == myclass.color_list[1]:
				myclass.black = myclass.black + 1
			else :
				myclass.gray = myclass.gray + 1
		else:
			myclass.other = myclass.other + 1

	def display_result(self):
		print "Hay ", myclass.name," What's up?"
		print "Total White cars: ", myclass.white
		print "Total Black cars: ", myclass.black
		print "Total Gray cars: ", myclass.gray
		print "Sample Cars:", myclass.sample
		print "Other Cars:", myclass.other
		print ""
myobj1 = myclass("John")
myobj1.check_color()
myobj1.display_result()

myobj2 = myclass("Pawan")
myobj2.check_color()
myobj2.display_result()