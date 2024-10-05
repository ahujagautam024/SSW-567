def classifyTriangle(a, b, c):
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
    # Check for invalid inputs: sides should be > 0 and <= 200
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Sort the sides to make sure we can correctly apply the right triangle check
    sides = sorted([a, b, c]) 
    
    # Check for triangle inequality theorem: the sum of any two sides must be greater than the third
    if sides[0] + sides[1] <= sides[2]:
        return 'NotATriangle'
    
    # Check for equilateral triangle: all sides are equal
    if a == b == c:
        return 'Equilateral'
    
    # Check for right triangle: Pythagorean theorem holds (a² + b² = c² after sorting)
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'
    
    # Check for isosceles triangle: exactly two sides are equal
    if a == b or b == c or a == c:
        return 'Isosceles'
    
    # If none of the above conditions apply, it's a scalene triangle
    return 'Scalene'
