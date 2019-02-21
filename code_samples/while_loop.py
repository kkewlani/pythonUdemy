def sample_while_loop():
    x = 0
    while x < 5:
        print("smaller")
        x +=1

def another_sample():
    correct_password = "python123"
    name = input("Enter name: ")
    password = input("Enter Password: ")

    while correct_password !=password:
        password = input("Wrong Password. Try Again!")

    print("hi %s, You are Logged In!" % name)


