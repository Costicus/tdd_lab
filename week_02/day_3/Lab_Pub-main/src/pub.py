class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink_to_menu(self, drink):
        self.drinks.append(drink)
        
    def add_money_to_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def sell_drink(self, customer, drink):
        customer_drunk = self.check_drunkenness(customer)
        if not customer_drunk :
            customer.remove_money_from_wallet(drink.price)
            self.add_money_to_till(drink.price)

    def check_drunkenness(self, customer):
        if customer.drunkenness > 9:
            return True
        return False