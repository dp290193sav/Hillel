add_my_list = []
"""add_my_list - пустоq список"""


def load_file():
    '''fp открывает файл с заметками, print выводит их на экран'''
    fp = open('note_file.txt')
    print('Нотатки завантажено з файлу!')
    print(fp.read())


def clear_file():
    '''fp открывает файл с заметками в режиме write и перезаписывает его
     удаляя всю предыдущую информацию'''
    with open('note_file.txt', mode='w') as fp:
        fp.write('')
    print('Нотатки видалено з файлу!')


def save_file(add_my_list):
    '''fp открывает файл с заметками в режиме append и сохраняет все ранее добавленные заметки из списка
    add_my_list в файл note_file.txt'''
    with open('note_file.txt', mode='a') as fp:
        for element in add_my_list:
            fp.write(element+'\n')
    print('Нотатки збережено')



def add_menu(add_my_list):
    """функция принимает в себя пустой список add_my_list,
    y переменная принимающиая введенные заметки пользователем
    add_my_list.append(y) добавляет полуенне заметки из y в пустой список add_my_list
    return возвращает сохраненные данные в список add_my_list"""
    y = input('Введіть нотатку: ')
    add_my_list.append(y)
    return add_my_list

def earliest(add_my_list):
    """функция выводит сохраненные заметки в хронологическом порядке, от раннего к более позднему,
    принимает в себя список add_my_list
    for i in add_my_list проходимся по элементно по каждой заметки из списка add.my.list
    print  выводим отсортированные заметки от раннего к более позднему на экран пользователю"""
    for i in add_my_list:
        print(i)


def latest(add_my_list):
    """функция выводит сохраненные заметки в хронологическом порядке, от позднего к более раннему,
    принимает в себя список add_my_list
    for i in add_my_list[::-1] проходимся по элементно по каждой заметки из конца списка  add.my.list
    print  выводим отсортированные заметки от позднего к более раннему на экран пользователю"""
    for i in add_my_list[::-1]:
        print(i)

def shortest(add_my_list):
    """функция выводит сохраненные заметки в порядке их длинны, от длинного к короткому,
         принимает в себя список add_my_list
        x - отсортированная переменная из списка add_my_list,
        key - len сортируем по длинне строк
        for element in x проходимся по элементно по каждому значени в перемемнной х
        print выводим поэлементно отсортированные данные"""
    x = sorted(add_my_list, key=len)
    for element in x:
        print(element)



def longest(add_my_list):
    """функция выводит сохраненные заметки в порядке их длинны, от короткого к длинному,
     принимает в себя список add_my_list
    x - отсортированная переменная из списка add_my_list,
    key - len сортируем по длинне строк
    reverse = True сортировка в обратном порядке от короткого к длинному
    for element in x проходимся по элементно по каждому значени в перемемнной х
    print выводим поэлементно отсортированные данные"""
    x = sorted(add_my_list, key=len, reverse=True)
    for element in x:
        print(element)


def display_menu():
    """
    функция выводит на экран весь функционал программы
    """
    print(f'\nБот приймає наступні команди: {menu}')
    print('''
add - додати нотатку
earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
save - зберігає всі активні нотатки у службовий файл
load - завантаження збережених нотаток зі службового файла
clear - видалити всі збережені нотатки та видалити файл зберігання нотаток
exit - завершення программи.\n
Почніть роботу:''')


menu = ''
display_menu()
if __name__ == '__main__':
    while True:
        """
            Считывает ввод пользователя и сравнивает веденные данные с заготовленными фразами меню
            Если ввод - что-то из предложенного функционала, то вызывает соответсвующую функцию,
            если 100% совпадения с предложенным функционала нет, сообщает об этом.
            если введен 'exit' программа прекращает свою работу)
            """
        x = input()
        if x.lower() == "add":
            add_menu(add_my_list)
        elif x.lower() == 'earliest':
            earliest(add_my_list)
        elif x.lower() == 'latest':
            latest(add_my_list)
        elif x.lower() == 'longest':
            longest(add_my_list)
        elif x.lower() == 'shortest':
            shortest(add_my_list)
        elif x.lower() == 'save':
            save_file(add_my_list)
        elif x.lower() == 'load':
            load_file()
        elif x.lower() == 'clear':
            clear_file()
        elif x.lower() == 'exit':
            print('программа деактивована! усього найкращого =) ')
            break
        else:
            print('оберіть команду з меню!')
        pass
