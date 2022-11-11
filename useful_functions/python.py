def prime_checker(_value):
    """
    Input is a singular numeric value.
    Output is a boolean depending on if the value is a prime number.
    """
    from math import sqrt

    _ft = True
    for i in range(2,int(sqrt(_value))+1):
        if _value % i == 0:
            _ft = False
            break

    return _ft


def LCM(_array):
    """
    Input is a list of numeric values.
    Output is the Lowest Common Multiple of those numeric values.
    """
    from math import lcm
    
    return lcm(*_array)


def HCF(_array):
    """
    Input is a list of numeric values.
    Output is the Highest Common Factor (Greatest Common Divisor) of those numeric values.
    """
    from math import gcd

    return gcd(*_array)
    

