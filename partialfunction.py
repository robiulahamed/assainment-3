from functools import partial

def multiply(x, y, z):
    """
    Function to multiply three numbers.
    """
    return x * y * z

# Create partial functions with different combinations of arguments
partial_multiply_by_2 = partial(multiply, 2)
partial_multiply_by_3 = partial(multiply, z=3)
partial_multiply_by_4 = partial(multiply, y=4)

# Example usage
print("Partial function results:")
print("Multiply by 2:", partial_multiply_by_2(3, 4))
print("Multiply by 3:", partial_multiply_by_3(2, 5))
print("Multiply by 4:", partial_multiply_by_4(2, 3))
