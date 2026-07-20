from datetime import date

birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

year, month, day = map(int, birthday_str.split("-"))
birthday = date(2010, 11, 17)

today = date()

age_in_days = (today - birthday).days

print(f"You are {age_in_days} days old.")
