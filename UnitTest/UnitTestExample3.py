import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # set upclass gets executed only once in the entire test case methods before testcase methods execution
        print(" set upclass gets executed only once in the entire test case methods before testcase methods execution")
    @classmethod
    def tearDownClass(cls): # teardownclass gets executed only once in the entire test case methods after testcase methods execution
        print("teardownclass gets executed only once in the entire test case methods after testcase methods execution")
    def test_add(self):
        print(5+3)
    def test_sub(self):
        print(8-2)



