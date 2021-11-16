"""
Exercise: Write a function for the calculation of the square root that makes use of the same technique used for the logarithm function. 
The function, called radice_per_bisezione, must take in input x and err and must return the square root of x using err as parameter for the evaluation of the quality of the approximation. 
"""

def radice_per_bisezione(x, err):
    """
    This function calculates the square root of x using the bisection method.
    """
    if x < 0:
        return "The number is negative"
    elif x == 0:
        return 0
    else:
        a = 0
        b = x
        while abs(a**2 - x) > err:
            c = (a + b)/2
            if c**2 > x:
                b = c
            else:
                a = c
        return c

if __name__ == "__main__":
    x = float(input("Insert the number: "))
    err = float(input("Insert the error: "))
    print(radice_per_bisezione(x, err))