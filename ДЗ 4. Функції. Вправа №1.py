usd = 43


def function_uah_to_usd():
    user_input = float(input('Введите cумму UAH: '))
    return user_input / usd


def function_usd_to_uah():
    user_input = float(input('Введите сумму USD: '))
    return user_input * usd


def display_menu():
    print(f'Меню:{menu}')
    print('''
1. Конвертировать UAH в USD
2. Конвертировать USD в UAH
3. Exit''')


menu = ''


while True:
    display_menu()
    z = input()
    if z == "1":
        print(round(function_uah_to_usd(), 2))
    elif z == '2':
        print(round(function_usd_to_uah(), 2))
    elif z == '3':
        break

