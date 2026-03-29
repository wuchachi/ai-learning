#Hourly wage pay

hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")
daily_wages = (float(hourly_wage))*(float(hours_worked))

if day_of_week.lower() == "sunday":
    daily_wages = (hourly_wage * 2) * hours_worked
else:
    daily_wages = (hourly_wage) * hours_worked

print(f"Daily wage: {daily_wages} euros")
