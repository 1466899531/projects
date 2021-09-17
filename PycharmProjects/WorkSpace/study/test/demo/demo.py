# coding=utf-8

import unittest

def addNum(a,b):
    return a+b
def delNum(a,b):
    c = a-b
    if c>=0:
        return c
    else:
        return -c
class TestFun(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(2,addNum(1,1))
    def testDel(self):
        self.assertEqual(3,delNum(6,9))

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFun)
    unittest.TextTestRunner(verbosity=2).run(suite)