# Triangle Classifier

This project contains a Python program to classify triangles based on their side lengths. The program also includes a set of unit tests written using Python's `unittest` framework to verify the correctness of the classification logic.

## Project Structure

The repository contains two primary files:

1. **`Triangle.py`**: This file contains the `classifyTriangle` function, which classifies triangles based on the input side lengths.
2. **`TestTriangle.py`**: This file contains the test cases for the `classifyTriangle` function, using the `unittest` framework.

## Function Description

### `classifyTriangle(a, b, c)`

The function takes three integer inputs representing the lengths of the sides of a triangle. Based on the input, it returns one of the following classifications:

- **Equilateral**: All three sides are equal.
- **Isosceles**: Exactly two sides are equal.
- **Scalene**: No sides are equal.
- **Right**: The sides satisfy the Pythagorean theorem, indicating a right triangle.
- **NotATriangle**: The input values do not satisfy the triangle inequality theorem.
- **InvalidInput**: The input values are either non-integer, non-positive, or exceed 200.

## Testing

The project uses Python's `unittest` framework to test the functionality of the `classifyTriangle` function. The test cases are included in the `test_triangle.py` file.

### How to Run Tests

1. Ensure that both `Triangle.py` and `test_triangle.py` are in the same directory.
2. From the command line, navigate to the project directory.
3. Run the following command to execute the tests:

   ```bash
   python -m unittest test_triangle.py
