my_list = 0

while True:
    try:
        x = input('Введите число: ')
        if x == 'sum':
            break
        else:
            x = float(x)
            my_list = my_list + x
    except:
        print('Введите число, или-же sum! ')
        continue

print(my_list)