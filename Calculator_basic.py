number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
operator_answer = input("What operator would you like to use? Addition, subtraction, multiplication, division, or exponent")

added = number_1 + number_2
subtracted = number_1 - number_2
multiplied = number_1 * number_2
divided = number_1 / number_2
exponent = number_1 ** number_2

if operator_answer.lower() == "addition":
    print(f"{added:.10g}")
elif operator_answer.lower() == "subtraction":
    print(subtracted)
elif operator_answer.lower() == "multiplication":
    print(multiplied)
elif operator_answer.lower() == "division":
    print(divided)
elif operator_answer.lower() == "exponent":
    print(exponent)