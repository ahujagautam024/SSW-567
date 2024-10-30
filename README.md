# Triangle Classifier [![CircleCI](https://dl.circleci.com/status-badge/img/circleci/RuQkQSfbtATvPQwW6cYotg/N8u5uuq2twHTop7143XpZS/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/RuQkQSfbtATvPQwW6cYotg/N8u5uuq2twHTop7143XpZS/tree/main)

This project contains a Python program to classify triangles based on their side lengths. The program also includes a set of unit tests written using Python's `unittest` framework to verify the correctness of the classification logic.

## Project Structure

The repository contains the following primary files:

1. **`Hw-02a/Triangle.py`**: This file contains the `classifyTriangle` function, which classifies triangles based on the input side lengths.
2. **`Hw-02a/TestTriangle.py`**: This file contains the test cases for the `classifyTriangle` function, using the `unittest` framework.
3. **`.circleci/config.yml`**: CircleCI configuration file, located at the root of the repository, that defines the build and test pipeline for continuous integration.

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

The project uses Python's `unittest` framework to test the functionality of the `classifyTriangle` function. The test cases are included in the `Hw-02a/TestTriangle.py` file.

### How to Run Tests

1. Ensure that both `Hw-02a/Triangle.py` and `Hw-02a/TestTriangle.py` are in the same directory.
2. From the command line, navigate to the project directory.
3. Run the following command to execute the tests:

   ```bash
   python -m unittest Hw-02a/TestTriangle
