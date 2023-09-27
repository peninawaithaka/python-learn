# create a store applocation


class Item:
    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self, x, y):
        return x * y


item_1 = Item('Shoes', 300, 5) #creating an instance of the class
print(item_1.price)

item_2 = Item('Pants', 400, 10)
print(item_2.name)

print(item_2.calculate_total_price(item_2.price, item_2.quantity))