import json
from uuid import uuid4


def display_boxer_data(d):
    """
    фрмирует полную строку с полной информацией о каждом боксере
    :param d: полные данные об одном боксере
    :return: возвращает полную сфрмированную сроку с каждым боксером
    """
    return f'{d["name"]} by version {d["category"]} takes the place of {d["rating"]}'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    функция выводит на экран в читабельном виде боксеров, разделенных по признакам:
    index_name (в index_to_view)
    :param index_name: название нашего индекса для отображения
    :param index_to_view: сам индекс
        ключи словаря - уникальные значения в индексе
        значения словаря - списки уникальных айдишников боксеров (ссылки на полные данные)
    :param source_uid_data: полные данные боксеров с айдишниками
    :return: ничего
    """
    print(f'version by {index_name}')
    for key, values in index_to_view.items():
        print(f'display boxers by version {key} :')
        for uid in values:
            print(f'  {display_boxer_data(source_uid_data[uid])}')


data = json.load(open('data_base.json', mode='r'))
uid_index = dict()
category_index = dict()

# Проходимся по данным каждоого боксера, что-бы привоить каждому уникальный id
for boxer_data in data['rating_of_boxers_by_version']:
    # присваиваем каждому боксеру id
    boxer_data['uid'] = str(uuid4())
    # заполняем имя боксера
    boxer_data['rating'] = f"{boxer_data['rating']} "
    # добавляем ссылку на полные данные боксера в индекс айдишников
    uid_index[boxer_data['uid']] = boxer_data
    # проверяем если версия уже есть, добавляем из этой версии боксеров
    if boxer_data['category'] in category_index:
        category_index[boxer_data['category']].append(boxer_data['uid'])
    # если версии еще нет, создаем и добавляем туда боксеров подпадащих под эту версию
    else:
        category_index[boxer_data['category']] = list()
        category_index[boxer_data['category']].append(boxer_data['uid'])

# вывод в по категориям
view_index('category', category_index, uid_index)





