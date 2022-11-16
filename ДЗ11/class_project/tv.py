from product import Product


class TV(Product):
    def __init__(self, name, price, quantity, diagonal):
        super().__init__(name=name, category='TV', price=price, quantity=quantity)
        self.diagonal = diagonal

    def __str__(self):
        return f'''
        Телевизор {self.name} 
        из категории {self.category} 
        диагональю {self.diagonal} дюйма,
        цена составляет: {self.price},
        в наличии {self.quantity} штук.
        '''
