from product import Product


class Headset(Product):
    def __init__(self, name, price, quantity, type_name):
        super().__init__(name=name, category='Headset', price=price, quantity=quantity)
        self.type_name = type_name

    def __str__(self):
        return f'''
        Наушники {self.name} 
        тип наушников {self.type_name}
        из категории {self.category} 
        цена составляет: {self.price},
        в наличии {self.quantity} штук.
        '''
