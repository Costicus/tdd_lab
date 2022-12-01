import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
class TestPub(unittest.TestCase):

    def setUp(self):
        self.instance_of_pub = Pub("The flying bull", 200.00)
        self.instance_of_drink = Drink("Scotch Whisky", 10, 3)
        self.instance_of_customer = Customer("Bob", 2000.00, 21, 3)

    def test_pub_has_name(self):
        self.assertEqual("The flying bull", self.instance_of_pub.name)

    def test_pub_has_till(self):
        self.assertEqual(200.00, self.instance_of_pub.till)

    def test_add_drink_to_menu(self):
        self.instance_of_pub.add_drink_to_menu(self.instance_of_drink)
        self.assertEqual(1, len(self.instance_of_pub.drinks))

    def test_add_money_to_till(self):
        self.instance_of_pub.add_money_to_till(self.instance_of_drink.price)
        self.assertEqual(210.00, self.instance_of_pub.till)

    def test_is_customer_old_enough(self):
        customer_1 = Customer("Guido van Rossum", 500, 64, 0)
        age =  self.instance_of_pub.check_age(customer_1)
        self.assertEqual(True, age)

    def test_customer_is_not_old_enough(self):
        customer_2 = Customer("Carol Willing", 750, 15, 10)
        age =  self.instance_of_pub.check_age(customer_2)
        self.assertEqual(False, age)

    def test_sell_drink(self):
        self.instance_of_pub.sell_drink(self.instance_of_customer,self.instance_of_drink)
        self.assertEqual(1990.00, self.instance_of_customer.wallet)
        self.assertEqual(210.00, self.instance_of_pub.till)

    def test_customer_too_drunk(self):
        customer_2 = Customer("Carol Willing", 750, 15, 10)
        drunkenness = self.instance_of_pub.check_drunkenness(customer_2)
        self.assertEqual(True, drunkenness)

    def test_customer_not_too_drunk(self):
        drunkenness = self.instance_of_pub.check_drunkenness(self.instance_of_customer)
        self.assertEqual(False, drunkenness)
        