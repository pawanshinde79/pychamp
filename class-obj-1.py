class myclass:
    sample = 0
    white = 0
    red = 0
    green = 0
    gray = 0
    other = 0
    color_list = ['White','Red','Green','Gray']

    def __init__(self, name):
        myclass.name = name
        print "Enter the color of your car:"
        myclass.color = raw_input()
        myclass.sample = myclass.sample + 1

    def check_color(self):
        if myclass.color in myclass.color_list:
            if myclass.color == myclass.color_list[0]:
                myclass.white = myclass.white + 1
            elif myclass.color == myclass.color_list[1]:
                myclass.red = myclass.red + 1
            elif myclass.color == myclass.color_list[1]:
                myclass.green = myclass.green + 1
            else:
                myclass.gray = myclass.gray + 1
        else:
            myclass.other = myclass.other + 1

    def result_print(self):
        print "Hello ", myclass.name
        print "The no of white cars are:", myclass.white
        print "The no of Red cars are:", myclass.red
        print "The no of Green cars are:", myclass.green
        print "The no of Gray cars are:", myclass.gray
        print "Sample cars are:", myclass.sample
        print "Other cars are:", myclass.other


count = 0
name_list = ['John', 'Rafa', 'Dan', 'Sandy', 'Roger']
mylist = []
while count < len(name_list):
    mylist.append(myclass(name_list[count]))
    mylist[count].check_color()
    mylist[count].result_print()
    count = count + 1
    print " "
