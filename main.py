number_float = float(input("Please type in a decimal number: "))

integer_part = int(number_float)
decimal_part = number_float - integer_part

print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part:.10g}")