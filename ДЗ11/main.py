import json
from class_project import Product, TV, Headset
from pprint import pprint
from uuid import uuid4

warehouse = json.load(open('warehouse.json', mode='r'))
uid_index = dict()
category_index = dict()
name_index = dict()
price_index = dict()

menu = list()
for row in warehouse:
    if row['category'] == 'TV':
        obj = TV
    elif row['category'] == 'Headset':
        obj = Headset
    menu.append(obj)
pprint(menu)


def warehouse_index():
    for warehouse_data in warehouse['warehouse']:
        warehouse_data['uid'] = str(uuid4())
        warehouse_data['category'] = f"{warehouse_data['category']} {warehouse_data['name']} {warehouse_data['price']}"
        uid_index[warehouse_data['uid']] = warehouse_data
        if warehouse_data['category'] in category_index:
            category_index[warehouse_data['category']].append(warehouse_data['uid'])
        else:
            category_index[warehouse_data['category']] = list()
            category_index[warehouse_data['category']].append(warehouse_data['uid'])

        if warehouse_data['name'] in name_index:
            name_index[warehouse_data['name']].append(warehouse_data['uid'])
        else:
            name_index[warehouse_data['name']] = list()
            name_index[warehouse_data['name']].append(warehouse_data['uid'])

        if warehouse_data['price'] in price_index:
            price_index[warehouse_data['price']].append(warehouse_data['uid'])
        else:
            price_index[warehouse_data['price']] = list()
            price_index[warehouse_data['price']].append(warehouse_data['uid'])

warehouse_index()


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
    print(f'знайдено "количество телеков" телевізори')
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


def headset_menu():
    print(f'знайдено "количество наушников" навушники')
    print(f'Відфільтрувати чи скинути? {headset_menu}')
    print('''
Фільтр
Скинути
  ''')


headset_menu = ''


def filter_headset_menu():
    print('Шукаючи Навушники, ви можете фільтрувати за:')
    print('''
    Ціна
    Кількість
    Бренд
    Тип
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
            headset_menu()
            y = input('зробіть свій вибір: ')
            if y.lower() == 'фільтр':
                filter_headset_menu()
                z = input('За якими данними фільтруємо?! ')
                if z.lower() == 'ціна':
                    print('фильтр по цене навушників')
                elif z.lower() == 'кількість':
                    print('фильтр по количеству навушників')
                elif z.lower() == 'бренд':
                    print('фильтр по бренду навушників')
                elif z.lower() == 'тип':
                    print('фильтр по типу навушників')
        else:
            print('оберіть категорію з меню!')
        pass



