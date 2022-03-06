import unittest #this is a python module with which we can use do any operation
from DemoExample1 import Sample1
#here we are creating a class with two methods inside it and i created a unit test in which i called those 2 methods
class MyTestCase(unittest.TestCase): #we can create one or more tests by inheriting  the TestCase class available in the unittest module.
    def test_addingNumbers(self): #testcase specific to unittesting.So whatever test we are writing should follow test keyword before it
        Sample1.add(self,3,5)
    def test_subtractNumbers(self):
        Sample1.sub(self,6,2)



#if __name__ == '__main__':
    #unittest.main()
