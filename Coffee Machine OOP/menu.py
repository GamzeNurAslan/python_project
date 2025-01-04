class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="turk_kahvesi", water=50, milk=0, coffee=20, cost=2.50),
            MenuItem(name="menengic_kahvesi", water=40, milk=30, coffee=35, cost=4.00),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=3.50),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=2.00),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.00)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
