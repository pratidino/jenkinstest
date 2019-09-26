import test
import unittest

class TestTest(unittest.TestCase):
    def test_add_int(self):
        result = test.add(1,2)
        self.assertEqual(result,3)

    def test_add_float(self):
        result = test.add(20.5,10.0)
        self.assertEqual(result,30.5)

    def test_add_str(self):
        result=test.add('abc','def')
        self.assertEqual(result,'abcdef')

    def test_add_str_int(self):
        result=test.add('abc',1)
        self.assertEqual(result,'abc1')

    def test_add_str_float(self):
        result=test.add('abc',10.5)
        self.assertEqual(result,'abc10.5')

if __name__ == '__main__':
    unittest.main()
