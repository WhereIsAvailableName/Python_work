def leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
def maxdays(m, y):
    if m == 2:
        return 29 if leap(y) else 28
    elif ((m==4) or (m==6) or (m==9) or (m==11)):
        return 30
    else:
        return 31
def days_in_full_years_before(y):
    total = 0
    i = 1900
    while i != y:
        if leap(i):
            total = total+366
        else:
            total = total+365
        i = i+1
    return total
def days_in_full_months_before(m,y):
    total = 0
    i = 1
    while i != m:
        total = total + maxdays(i, y)
        i = i+1
    return total
def days_since_1_1_1900(d,m,y):
    return days_in_full_years_before(y) + days_in_full_months_before(m,y) + d
def what_day_was_it(d,m,y):
    return days_since_1_1_1900(d,m,y)%7
def blank(m,y,n): #Print blank spaces to align the days of the week.
    starting_day = what_day_was_it(1, m, y)
    if starting_day > n :
        print("   ", end=" ")
def identical_weekday(m,y,n): #Print all the dates of the specified week.
    blank(m,y,n)
    starting_day = what_day_was_it(1, m, y)
    current_day = (n - starting_day + 7) % 7 + 1
    while current_day <= maxdays(m,y):
        print(f"{current_day:2}", end="  ")
        current_day += 7
    print()
def calendar(m,y):
    starting_day = what_day_was_it(1, m, y)
    days_in_month = maxdays(m, y)
    print("Mon",end=" ")
    identical_weekday(m,y,1)
    print("Tue",end=" ")
    identical_weekday(m,y,2)
    print("Wed",end=" ")
    identical_weekday(m,y,3)
    print("Thu",end=" ")
    identical_weekday(m,y,4)
    print("Fri",end=" ")
    identical_weekday(m,y,5)
    print("Sat",end=" ")
    identical_weekday(m,y,6)
    print("Sun",end=" ")
    identical_weekday(m,y,7)
user_input = input()
m,y = map(int, user_input.split(','))
calendar(m,y)
