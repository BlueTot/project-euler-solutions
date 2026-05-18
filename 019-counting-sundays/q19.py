days_in_a_month = {0: 31, 1: (28, 29), 2: 31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

day_of_the_week = 1
day = 1
year = 1900
month = 0
num_sundays = 0

while year <= 2000:

    if month == 1:
        days = 29 if year % 4 == 0 else 28
    else:
        days = days_in_a_month[month]
    
    day = (day + days) % days
    month = (month + 1) % 12
    if month == 0:
        year += 1
    day_of_the_week = (day_of_the_week + days) % 7
    if day_of_the_week == 0 and year >= 1901 and day == 1:
        num_sundays += 1
        print(day, month, year, day_of_the_week)

    # day
    # if month == 1:
    #     days = 29 if year % 4 == 0 else 28
    # else:
    #     days = days_in_a_month[month]

    # day_of_the_week = (day_of_the_week + days) % 7
    # if day_of_the_week == 0 and year >= 1901:
    #     num_sundays += 1
    #     print(month, year)
    
    # month = (month + 1) % 12
    # if month == 0:
    #     year += 1

print(num_sundays)
        
    
    