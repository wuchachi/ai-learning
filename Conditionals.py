word_one = input("Enter word 1: ")
word_two = input("Enter word 2: ")

word_one = word_one.lower()
word_two = word_two.lower()

if word_one < word_two:
    print(f"{word_two} is last")
elif word_one > word_two:
    print(f"{word_one} is last")
else:
    print("The words are the same...")