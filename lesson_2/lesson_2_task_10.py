def bank (x, y):
    x = int (x)
    y = int (y)
    for y in range (1, y+1):
        x = x + x*0.1
    return (round (x,2))
    
x = input ("Введите сумму вклада: ")
y = input ("Введите количество лет: ")
bank (x, y)
print (f'Сумма, которая будет на счету {bank (x, y)}')