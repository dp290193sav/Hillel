class Triangle:
    def __init__(self, a: float, b: float, c: float):
        '''
        Метод init принимает атрибуты сторон треугольника в float
        :param a: - сторона треугольника
        :param b: - сторона треугольника
        :param c: - сторона треугольника
        '''
        self.a = a
        self.b = b
        self.c = c

    def exist(self):
        '''
        Метод exist - проверяет существует ли треугольник в Евклидовом пространстве
        if сравнивает сумму двух сторон треугольника больше третьей?!, если да, то треугольник существует
        :return: возвращает правду (треугольник существует)
        else в противном случае треугольник не может существовать.
        :return: возвращает ложь (треугольник не существует)
        '''
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print('#'*20)
            print('Треугольник существует!')
            return True
        else:
            print('#'*20)
            return False

    def perimeter(self):
        '''
        метод perimeter считает периметр треугольника
        :return: возвращает сумму сторон треугольника
        '''
        return self.a + self.b + self.c

#точка входа
if __name__ == '__main__':
    # вызываем класс Triangle подставляем в поля значения сторон треугольника
    my_triangle_number_one = Triangle(a=10, b=10, c=10)
    # вызываем метод exist
    if my_triangle_number_one.exist():
        # если метод exist возвращает True (треугольник существует)
        my_triangle_number_one.exist = True
        # print - выводим на экран площадь треугольника
        print(f'Площадь треугольника number_one: {my_triangle_number_one.perimeter()}\n')
        #если треугольник не существует сообщает эту информацию
    elif print(f'Треугольник number_one не существует, следовательно у него нет периметра\n'):
        pass
    # вызываем класс Triangle подставляем в поля значения сторон треугольника
    my_triangle_number_two = Triangle(a=-10, b=10, c=10)
    # вызываем метод exist
    if my_triangle_number_two.exist():
        # если метод exist возвращает True (треугольник существует)
        my_triangle_number_two.exist = True
        # print - выводим на экран площадь треугольника
        print(f'Площадь треугольника number_two: {my_triangle_number_two.perimeter()}\n')
        # если треугольник не существует сообщает эту информацию
    elif print(f'Треугольник number_two не существует, следовательно у него нет периметра\n'):
        pass

    # вызываем класс Triangle подставляем в поля значения сторон треугольника
    my_triangle_number_three = Triangle(a=7, b=10, c=11)
    # вызываем метод exist
    if my_triangle_number_three.exist():
        # если метод exist возвращает True (треугольник существует)
        my_triangle_number_three.exist = True
        # print - выводим на экран площадь треугольника
        print(f'Площадь треугольника number_three: {my_triangle_number_three.perimeter()}\n')
        # если треугольник не существует сообщает эту информацию
    elif print(f'Треугольник number_three не существует, следовательно у него нет периметра\n'):
        pass
