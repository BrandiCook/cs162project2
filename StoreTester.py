# Author: Brandi Cook
# Date: 10/5/2020
# Description: This program is to test a simulated store, named Store.py
# Store.py has members, grocery items, and keeps track of items in cart as
# well as price. StoreTester.py ensures functions and classes are working properly.

import unittest
import uuid

from cs162project2.Store import Product
from cs162project2.Store import Customer
from cs162project2.Store import Store

class ProductTest(unittest.TestCase):
    """
    This is a class made in order to test the Product class from Store.py
    """

    def setUp(self):
        """
        Creates example/test specifications for the product
        """
        self.product_id = uuid.getnode()
        self.product_title = "Test Title"
        self.product_desc = "Test Description"
        self.product_price = 102.38
        self.product_quant = 1
        self.product = Product(self.product_id, self.product_title, self.product_desc,
                               self.product_price, self.product_quant)

    def test_get_product_id(self):
        """
        Tests whether or not Store.py successfully gets product id
        """
        self.assertEqual(self.product_id, self.product.get_id_code())

    def test_get_product_title(self):
        """
        Tests whether or not Store.py successfully gets product title
        """
        self.assertEqual(self.product_title, self.product.get_title())

    def test_decrement_quantity(self):
        """
        Tests whether or not Store.py successfully decrements quantity available
        """
        self.assertEqual(self.product.get_quantity_available(), 1)


class CustomerTest(unittest.TestCase):
    """
    This is a class made in order to test the Customer class from Store.py
    """
    def setUp(self):
        """
        Sets up test specifications for a customer object
        """
        #note to self *** UUID is universal unique id***
        self.customer_id = uuid.uuid1()
        self.customer_name = "Billy Bob"
        self.customer_premium = True

        #Testing 2 customers because there's not a lot to test with Product
        #Testing customer 2 premium false while 1 is true
        self.customer2_id = uuid.uuid1()
        self.customer2_name = "Sally Jane"
        self.customer2_premium = False

        self.customer1 = Customer(self.customer_name, self.customer_id, self.customer_premium)
        self.customer2 = Customer(self.customer2_name, self.customer2_id, self.customer2_premium)

    def test_is_premium_member(self):
        """
        Checks whether or not the premium member checker
        from Store.py works correctly
        """
        self.assertTrue(self.customer1.is_premium_member())
        self.assertFalse(self.customer2.is_premium_member())

class StoreTest(unittest.TestCase):
    """
    This is a class made in order to test the Store class from Store.py
    """
    def setUp(self):
        """
        Sets up test specifications for a Store
        """
        self.first_member = Customer("John Doe", uuid.uuid1(), True)
        self.second_member = Customer("Tony Hawk", uuid.uuid1(), False)
        self.store = Store()
        self.inventory = dict()
        self.members = dict()

    def test_add_member(self):
        """
        Tests whether or not the member adding function from Store.py
        functions correctly
        """
        self.store = Store()
        self.store.add_member(self.first_member)
        self.assertIsNotNone(self.store.get_member_from_id(self.first_member.get_account_ID()))

    def test_add_member_none(self):
        self.store = Store()
        self.assertIsNone(self.store.get_member_from_id(self.first_member.get_account_ID()))
        self.store.add_member(self.first_member)
        self.assertIsNotNone(self.store.get_member_from_id(self.first_member.get_account_ID()))
        self.assertIsNone(self.store.get_member_from_id(self.second_member.get_account_ID()))

if __name__ == '__main__':
    unittest.main()
