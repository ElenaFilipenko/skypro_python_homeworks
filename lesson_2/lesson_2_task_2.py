def is_year_leap (year):
    year = int (year)
    if year % 4 == 0:
        return (True)
    else:
        return (False)

year = input ("Введите год: ")
result = is_year_leap(year)
print ("год", year, ":", result)