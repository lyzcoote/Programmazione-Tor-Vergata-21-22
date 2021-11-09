"""
Exercise Author: Gainluca Rossi
Student: Flavio Fois
Date: 7th of November 2021
Exercise:
    Program that asks for two x and y numbers in input and prints the square root of x added to the square root of y.
    It is forbidden to use the operator **.
"""

def sqrt_x_without_power(x):
    """
    Returns the square root of x without using power.
    """
    if 0 == x:
        return 0        # Avoid division by zero
    n = (x / 2) + 1     # Initial estimate, never low
    n1 = (n + (x / n)) / 2
    while n1 < n:
        n = n1
        n1 = (n + (x / n)) / 2
        result_x = n
    return result_x


def sqrt_y_without_power(y):
    """
    Returns the square root of y without using power.
    """
    if 0 == y:
        return 0        # Avoid division by zero
    n = (y / 2) + 1     # Initial estimate, never low
    n1 = (n + (y / n)) / 2
    while n1 < n:
        n = n1
        n1 = (n + (y / n)) / 2
        result_y = n
    return result_y


def sqrt_sum_without_power(x, y):
    """
    Returns the square root of x added to the square root of y without using power.
    """
    return sqrt_x_without_power(x) + sqrt_y_without_power(y)


if __name__ == '__main__':
    """
    Main function.
    """
    print("Running exercise without using ** operator.")
    print(sqrt_sum_without_power(float(input("x value: ")), float(input("y value: "))))
