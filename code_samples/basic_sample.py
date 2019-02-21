# defining a list
# variable needs no declaration before hand - Python is a dynamically typed language => type is determined at runtime
# but the type thereafter is maintained throughout the program
store_address = ["4551", "Roosevelt Way", "NE", "Seattle"]

# defining a dictionary
pins = {"Kushal" : 1212, "Kiran" : 333, "Padma" : 131}


print(store_address[0], store_address[1])

#
pin = int(input("Enter your pin code: "))
#print("Pin code entered: %d" %pin)


# function definition - does not have a start or end indicator
# function parameter 'type' is not defined - judged at runtime
def find_in_file(user_fruit):
    myfile = open("fruits.txt")
    fruits = myfile.read()
    myfile.close()
    fruits = fruits.splitlines()
    if user_fruit in fruits:
        return "Fruit present in the list"
    else:
        return "No such fruit available"

if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
    #fruit = 10;
    print("converted to int value: %s" % fruit)
else:
    print("Incorrect Pin!")
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)

