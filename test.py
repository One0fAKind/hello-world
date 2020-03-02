import unittest

import function

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        pass
    def testadder(self):
        self.assertEqual( function.adder(1), 2)
      
if __name__ == '__main__':
  unittest.main()
