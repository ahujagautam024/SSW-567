"""
Module for classifying triangles based on the lengths of their sides.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classifies a triangle based on the lengths of its sides.
    Returns:
    - 'Equilateral' if all three sides are equal
    - 'Isosceles' if exactly two sides are equal
    - 'Scalene' if no sides are equal
    - 'Right' if the triangle satisfies the Pythagorean theorem
    - 'NotATriangle' if the sides don't form a valid triangle
    - 'InvalidInput' if input is invalid (e.g., non-positive or greater than 200)
    """
    if not (all(isinstance(side, int) for side in (side_a, side_b, side_c)) and
        all(0 < side <= 200 for side in (side_a, side_b, side_c))):
        return 'InvalidInput'
    sides = sorted([side_a, side_b, side_c])     # Sort the sides to apply the right triangle check
    if sides[0] + sides[1] <= sides[2]:# Check for triangle inequality theorem
        return 'NotATriangle'
    if side_a == side_b == side_c:# Classify the triangle
        return 'Equilateral'
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return 'Isosceles'
    return "Scalene"
