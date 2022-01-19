"""
Calculator
"""

def sum(x,y):
    """
    Sum operation between two values.
    """
    return x+y

def diff(x,y):
    """
    Subtraction operation between two values.
    """
    return x-y

def prod(x,y):
    """
    Multiplication operation between two values.
    """
    return x*y

def div(x,y):
    """
    Division operation between two values.

    In this operation, the second value can't be zero.
    """
    if (y != 0):
        return x/y
    return "The second value can't be zero."

def mod(x,y):
    """
    Modulo operation between two values, that is, the remainder of the division
    between the two values.

    In this operation, the second value can't be zero.
    """
    if (y != 0):
        return x%y
    return "The second value can't be zero."

def pot(x,y):
    """
    Potential operation between two values.

    In this operation, the  two values values can't be simultaneously zero.
    If the first value is zero, the result is zero.
    If the second value is zero, the result is one.
    """
    if ((x == 0) and (y == 0)):
        return "Both values can't be simultaneously zero."
    return x**y

def root(x,y):
    """
    Rooting operation between  two values.

    In this operation, the second value can't be zero.
    If the first value is zero, the result is zero.
    """
    if (y != 0):
        return x**(1/y)
    return "The second value can't be zero."

def get_result(operat, x, y):
    """
    Return the selected operation applied on the input values.

    If the operation fails, the return will be a string.
    """
    data = {'+': sum(x,y), '-': diff(x,y), '*': prod(x,y), '/': div(x,y),
            '%': mod(x,y), '^': pot(x,y), '!': root(x,y)}
    return data[operat]
