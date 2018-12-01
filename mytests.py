import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custon_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3, 3, 2), 54)

    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5, 2, 3)[2], 16)
        self.assertEqual(custom_non_lin_num_list(5, 3, 2)[2], 48)


if __name__ == '__main__':
    unittest.main()

# Running this file results in following output:
#
# .E..
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# ERROR: test_custom_non_lin_num_list(__main__.MyFirstTests)
# ----------------------------------------------------------------------
# Traceback(most recent call last):
#   File "mytests.py", line 17, in test_custom_non_lin_num_list
#   self.assertEqual(custom_non_lin_num_list(5, 2, 3)[2], 16)
# TypeError: 'NoneType' object is not subscriptable

# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# FAILED(errors=1)
