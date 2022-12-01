import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.instance_of_customer = Customer("Bob", 2000.00, 21, 0)
        self.instance_of_drink = Drink("Scotch Whisky", 10, 3)
        self.instance_of_pub = Pub("The flying bull", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.instance_of_customer.name)
 
    def test_customer_has_wallet(self):
        self.assertEqual(2000.00, self.instance_of_customer.wallet)

    def test_remove_money_from_wallet(self):
        self.instance_of_customer.remove_money_from_wallet(self.instance_of_drink.price)
        self.assertEqual(1990.00, self.instance_of_customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(21, self.instance_of_customer.age)

    def test_increase_drunkenness_level(self):
        self.instance_of_customer.increase_drunkenness_level(self.instance_of_drink.alcohol_level)
        self.assertEqual(3, self.instance_of_customer.drunkenness)
        
    