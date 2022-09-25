usd = 43


def my_function_uah(result):
    new_item = float(input('Введите cумму UAH: '))
    result = new_item / usd
    return result


def my_function_usd(result):
    new_item_price = float(input('Введите сумму USD: '))
    result = new_item_price * usd
    return result


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
        print(round(my_function_uah('result'), 2))
    elif z == '2':
        print(round(my_function_usd('result'), 2))
    elif z == '3':
        break

