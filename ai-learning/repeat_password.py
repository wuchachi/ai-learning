password = input("Enter your password: ")


while True:
  password_two = input("Repeat your password: ")
  if password_two == password:
      print("Password match!")
      break
  else:
      print("Password not match!")
