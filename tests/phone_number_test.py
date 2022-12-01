import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):

    def test_phone_number_can_format(self):
        formatted_number = phone_number_formater(1234567890)
        self.assertEqual("(123) 456-7890", formatted_number)

        