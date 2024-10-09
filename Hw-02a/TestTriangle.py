# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Gautam Vinod Ahuja - 20022514
"""

import unittest

from .Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '7,8,9 should be Scalene')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be Isosceles')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8,5,5 should be Isosceles')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 should be an invalid triangle')

    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 should be an invalid triangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

