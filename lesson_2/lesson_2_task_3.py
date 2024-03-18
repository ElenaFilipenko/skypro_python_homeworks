from math import ceil

def square (side):
    side = float (side)
    area_square = side*side
    return ceil(area_square)
    
side = input ("Введите сторону квадрата: ")
print (f'Площадь квадрата: {square(side)}')