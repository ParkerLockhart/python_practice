user_age = int(input("Enter your age: "))

months = user_age * 12
weeks = user_age * 52
days = user_age * 365.25
hours = 24 * days
minutes = 60 * hours
seconds = 60 * minutes

print(f"Your age, {user_age}, is equal to {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, or {seconds} seconds.")
