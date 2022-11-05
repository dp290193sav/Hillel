import json
from uuid import uuid4

def display_menu():
    print('Інтернет-магазин Tech-shop вітає Вас!')
    print(f'Категорії для пошуку: {menu}')
    print('''
Телевізори
Навушники
''')


menu = ''
display_menu()


def tv_menu():
    print(f'знайдено "скобочки и количество телеков" телевізори')
    print(f'Відфільтрувати чи скинути? {menu_tv}')
    print('''
Фільтр
Скинути
  ''')
menu_tv = ''


def filter_tv_menu():
    print('Шукаючи Телевізори, ви можете фільтрувати за:')
    print('''
    Ціна
    Кількість
    Бренд
    Діагональ дюйми
    SmartTv
                    ''')


data = json.load(open('warehouse.json', mode='r'))


if __name__ == '__main__':
    while True:
        x = input('пошук: ')
        if x.lower() == "телевізори":
            tv_menu()
            y = input('зробіть свій вибір: ')
            if y.lower() == 'фільтр':
                filter_tv_menu()
                z = input('За якими данними фільтруємо?! ')
                if z.lower() == 'ціна':
                    print('фильтр по цене телевизора')
                elif z.lower() == 'кількість':
                    print('фильтр по количеству телевизоров')
                elif z.lower() == 'бренд':
                    print('фильтр по бренду телевизоров')
                elif z.lower() == 'діагональ':
                    print('фильтр по диагонале телевизора')
                elif z.lower() == 'дюйми':
                    print('фильтр по диагонале телевизора')
                elif z.lower() == 'smarttv':
                    print('фильтр по SmartTv телевизора')
                elif z.lower() == 'смарттв':
                    print('фильтр по SmartTv телевизора')
            elif y.lower() == 'скинути':
                display_menu()
        elif x.lower() == 'навушники':
            print('headset')
        else:
            print('оберіть категорію з меню!')
        pass
