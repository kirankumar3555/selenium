import unittest


class MyTestCase(unittest.TestCase):
    def test_addNumbers(self):
        print(2+3)
        self.assertEqual(2,2) # we can add assertions for every unit test script
        #self.assertEqual(2,12)
    def test_subNumbers(self):
        print(5-1)

#if __name__ == '__main__':
    #unittest.main()
