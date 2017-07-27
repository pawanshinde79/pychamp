class myclass: # Initialization of Class
    sample = 0 # Global varialble declarations
    white = 0
    black = 0
    gray = 0
    other = 0
    color_list = ['White', 'Black', 'Gray'] # Defining color list

    def __init__(self, name):   # Initial function
        myclass.name = name
        print "Enter your car's color:"
        myclass.color = raw_input()
        myclass.sample = myclass.sample + 1

    def check_color(self):
        if myclass.color in myclass.color_list:
            if myclass.color == myclass.color_list[0]:
                myclass.white = myclass.white + 1
            elif myclass.color == myclass.color_list[1]:
                myclass.black = myclass.black + 1
            else:
                myclass.gray = myclass.gray + 1
        else:
            myclass.other = myclass.other + 1

    def display_result(self):
        print "Hello ", myclass.name
        print "The no of white cars are:", myclass.white
        print "The no of black cars are:", myclass.black
        print "The no of Gray cars are:", myclass.gray
        print "Sample cars are:", myclass.sample
        print "Other cars are:", myclass.other

myobj1 = myclass("Pawan")
myobj1.check_color()
myobj1.display_result()
