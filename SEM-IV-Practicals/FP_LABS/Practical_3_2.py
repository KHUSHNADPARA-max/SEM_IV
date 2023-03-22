import datetime


def first_day_of_month(year, first_day_of_year):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
    first_day_of_month = first_day_of_year
    for month in range(1, 13):
        print(
            f"{datetime.date(year, month, 1).strftime('%B %d, %Y')} is {days_of_week[first_day_of_month % 7]}")
        if month in [1, 3, 5, 7, 8, 10, 12]:
            first_day_of_month += 3
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                first_day_of_month += 1
            else:
                first_day_of_month += 0
        else:
            first_day_of_month += 2


year = int(input("Enter the year: "))
first_day_of_year = int(input(
    "Enter the first day of the year (0 for Monday, 1 for Tuesday, ..., 6 for Sunday): "))

first_day_of_month(year, first_day_of_year)
