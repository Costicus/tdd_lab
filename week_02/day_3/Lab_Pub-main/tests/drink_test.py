import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.instance_of_drink = Drink("Scotch Whisky", 10, 3)
    
    def test_drink_has_name(self):
        self.assertEqual("Scotch Whisky", self.instance_of_drink.name)

    def test_drink_has_price(self):
        self.assertEqual(10, self.instance_of_drink.price)


