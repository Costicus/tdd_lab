import unittest

from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):                                                #arrange
        self.instance_of_coffee_shop = CoffeeShop("The Prancing Pony", 100.00)

    def test_coffee_shop_has_name(self):
        self.assertCountEqual("The Prancing Pony", self.instance_of_coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(100.00, self.instance_of_coffee_shop.till)

    def test_increase_till(self):                                   
        self.instance_of_coffee_shop.increase_till(5)               #act
        self.assertEqual(105.00, self.instance_of_coffee_shop.till) #assert
