import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custon_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)


if __name__ == '__main__':
    unittest.main()

# Running this file results in following output:
#
# E.
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# ERROR: test_custon_num_list(__main__.MyFirstTests)
# ----------------------------------------------------------------------
# Traceback(most recent call last):
#   File "mytests.py", line 11, in test_custon_num_list
#   self.assertEqual(len(create_num_list(10)), 10)
# TypeError: object of type 'NoneType' has no len()

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED(errors=1)
