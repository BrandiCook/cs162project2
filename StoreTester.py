import unittest
import uuid

from cs162project2.Store import Product
from cs162project2.Store import Customer
from cs162project2.Store import Store

class ProductTest(unittest.TestCase):

    def setUp(self):
        self.product_id = uuid.getnode()
        self.product_title = "Test Title"
        self.product_desc = "Test Description"
        self.product_price = 102.38
        self.product_quant = 1
        self.product = Product(self.product_id, self.product_title, self.product_desc,
                               self.product_price, self.product_quant)

    def test_get_product_id(self):
        self.assertEqual(self.product_id, self.product.get_id_code())

    def test_get_product_title(self):
        self.assertEqual(self.product_title, self.product.get_title())

    def test_decrement_quantity(self):
        self.assertEqual(self.product.get_quantity_available(), 1)


class CustomerTest(unittest.TestCase):
    def setUp(self):
        #note*** UUID is universal unique id***
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
        self.assertTrue(self.customer1.is_premium_member())
        self.assertFalse(self.customer2.is_premium_member())

class StoreTest(unittest.TestCase):
    def setUp(self):
        self.first_member = Customer("John Doe", uuid.uuid1(), True)
        self.second_member = Customer("Mike Hawk", uuid.uuid1(), False)
        self.store = Store()
        self.inventory = dict()
        self.members = dict()

    def test_add_member(self):
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
