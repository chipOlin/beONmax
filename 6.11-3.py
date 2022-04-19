prices = {
    'Strawberries': 1.50,
    'Banana': 0.50,
    'Mango': 2.50,
    'Blueberries': 1.00,
    'Raspberries': 1.00,
    'Apples': 1.75,
    'Pineapple': 3.50
}


class Beverage:
    # ingr_cost = {
    #     'Strawberries': 1.50,
    #     'Banana': 0.50,
    #     'Mango': 2.50,
    #     'Blueberries': 1.00,
    #     'Raspberries': 1.00,
    #     'Apples': 1.75,
    #     'Pineapple': 3.50
    # }

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        # seb = 0
        # for ing in self.ingredients:
        #     seb += Beverage.ingr_cost[ing]
        return f'${self.cost:.2f}'

    def get_price(self):
        # return Beverage.get_cost(self) * 2.5
        return f'${self.price:.2f}'

    def get_name(self):
        # if len(self.ingredients) > 1:
        #     name = ' '.join(sorted(self.ingredients)).replace('berries', 'berry') + ' Fusion'
        # else:
        #     name = ' '.join(sorted(self.ingredients)).replace('berries', 'berry') + ' Smoothie'
        # return name
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'


b1 = Beverage(['Banana', 'Raspberries', 'Pineapple'])
print(b1.get_cost())
print(b1.get_price())
print(b1.get_name())

b2 = Beverage(['Raspberries'])
print(b2.get_cost())
print(b2.get_price())
print(b2.get_name())
