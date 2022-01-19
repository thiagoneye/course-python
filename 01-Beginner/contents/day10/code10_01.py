# Days in Month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                output = True
            else:
                output = False
        else:
            output = True
    else:
        output = False
        
    return output

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and (month == 2):
        output = 29
    else:
        output = month_days[month-1]

    return output

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
