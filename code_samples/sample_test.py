def calculate_age(year):
    age = 2019 - year
    return age


def ctof(cel):
    return cel*(9/5) + 32

def print_fruits():
    fruits_file = open("fruits.txt")
    fruits = fruits_file.read()
    print(fruits)
    fruits_file.close()

def temperature_conversion_list():
    temperatures = [10, -20, 100]
    for t in temperatures:
        print(ctof(t))

temperature_conversion_list()