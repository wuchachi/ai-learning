while True:
    password = '1234'
    psd = str(input("Enter a 4 digit passcode: "))
    if psd == password:
        print("You cracked the passcode!!!!")
        break
    else:
        print("Wrong password!")
