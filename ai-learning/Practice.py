def say_hello():
    print("Hello, how are you doing!!!")

def confess_love():
    print("I love you with all of my heart!")

while True:
    print("1 = say hello")
    print("2 = confess love")
    print("3 = quit program")
    choice = input(print("Input 1, 2, or 3: "))

    if choice == "1":
        say_hello()
    elif choice == "2":
        confess_love()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please input 1, 2, or 3.")