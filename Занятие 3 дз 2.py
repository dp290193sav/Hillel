while True:
    user_input = input("Бот активовано!")

    if 'привіт' in user_input.lower() or 'хай' in user_input.lower() or 'доброго дня' in user_input.lower():
        print('Доброго вечора, я бот з України!')
    elif 'як справи?' in user_input.lower() or 'що робиш?' in user_input.lower() or 'чим займаєшся?' in user_input.lower():
        print('Вчусь програмувати на Python!')
    elif 'фільм' in user_input.lower() or 'кінотеатр' in user_input.lower() or 'серіал' in user_input.lower():
        print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Життя по виклику", він просто бомба!')
    elif 'бувай' in user_input.lower() or 'надобраніч' in user_input.lower() or 'гудбай' in user_input.lower() or 'до зустрічі' in user_input.lower():
        print('Побачимось у мережі, I"ll be back =)')
        break
    else:
        print('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :(')