#Ahmed Rahman PSID:1820239
import datetime

print("Welcome to Ahmed's Birthday Calculator")


current_day = int(input("Enter Current Day: "))
current_month = int(input("Enter Current Month: "))
current_year = int(input("Enter Current Year: "))
current_date = datetime.date(current_year,current_month, current_day)
print("Current Date: ", current_date)

birth_day= int(input("Enter Birth Day: "))
birth_month = int(input("Enter Birth Month: "))
birth_year = int(input("Enter Birth Year: "))
birth_date = datetime.date(birth_year, birth_month, birth_day)
print("Birth Date: ", birth_date)

age_in_days = current_date - birth_date
age_in_days2 = age_in_days.days
print("age is:",age_in_days2,"days")
age_in_years = age_in_days2/365
print("or:",int(age_in_years),"years")

if current_day-birth_day == 0:
    if current_month-birth_month == 0:
        print("Happy Birthday")
else:
    print("Goodbye")