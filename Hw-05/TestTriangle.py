# TestTriangle.py

import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    # Existing tests
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(7, 8, 9), 'Scalene', '7,8,9 should be Scalene')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be Isosceles')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classify_triangle(8, 5, 5), 'Isosceles', '8,5,5 should be Isosceles')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1,10,12 should be NotATriangle')

    def testInvalidTriangleA(self): 
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 should be InvalidInput')

    def testInvalidTriangleB(self): 
        self.assertEqual(classify_triangle(-1, 5, 5), 'InvalidInput', '-1,5,5 should be InvalidInput')

    def testInvalidTriangleC(self): 
        self.assertEqual(classify_triangle(100, 201, 100), 'InvalidInput', '100,201,100 should be InvalidInput')

    def testInvalidTriangleD(self): 
        self.assertEqual(classify_triangle("5", 5, 5), 'InvalidInput', '"5",5,5 should be InvalidInput')

    def testScaleneWithLargeValues(self): 
        self.assertEqual(classify_triangle(199, 198, 197), 'Scalene', '199,198,197 should be Scalene')

    def testRightTriangleWithLargeValues(self): 
        self.assertEqual(classify_triangle(300, 400, 500), 'InvalidInput', '300,400,500 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
