while True:
    number = int(input("Enter a number, 0 quits."))
    if number == 0:
        break
    if number > 0:
        if number % 2 == 0:
            print(number, "is even")
        elif number % 2 != 0:
            print(number, "is odd")
        else:
            print(number, "is zero")

print("Done! Good work.")