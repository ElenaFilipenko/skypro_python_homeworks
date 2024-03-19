def bank (sum, time):
    sum = int (sum)
    time = int (time)
    for time in range (1, time+1):
        sum = sum + sum*0.1
    return (round (sum,2))
    
sum = input ("Введите сумму вклада: ")
time = input ("Введите количество лет: ")
bank (sum, time)
print (f'Сумма, которая будет на счету {bank (sum, time)}')