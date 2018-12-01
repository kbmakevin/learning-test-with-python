import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')


if __name__ == '__main__':
    unittest.main()

# Running this file results in following output:
#
# F
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# FAIL: test_hello(__main__.MyFirstTests)
# ----------------------------------------------------------------------
# Traceback(most recent call last):
#   File "mytests.py", line 8, in test_hello
#   self.assertEqual(hello_world(), 'hello world')
# AssertionError: None != 'hello world'

# ----------------------------------------------------------------------
# Ran 1 test in 0.003s

# FAILED(failures=1)
