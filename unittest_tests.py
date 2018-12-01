import unittest
from app import *


# must inherit from TestCase?
class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custon_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3, 3, 2), 54)

    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5, 2, 3)[2], 16)
        self.assertEqual(custom_non_lin_num_list(5, 3, 2)[4], 48)


if __name__ == '__main__':
    unittest.main()
