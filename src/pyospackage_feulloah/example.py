"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    c=0
    for i in range(abs(a)):
        if a > 0:
            c+=1
        else:
            c-=1
    for j in range(abs(b)):
        if b > 0:
            c+=1
        else:
            c-=1
    return c


def multiply_integers_slow(a,b):
    """
    Multiply 2 integers by counting.
    Parameters
    ----------
    a : int
        The first number to multiply.
    b : int
        The second number to multiply.

    Returns
    -------
    int
        The sum of the two numbers.

    Examples
    --------
    >>> multiply_integers_slow(3, 5)
    15
    >>> multiply_integers_slow(-2, 7)
    -14
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Booleans are not accepted, please pass integers")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"Both arguments must be integers, got {type(a).__name__} and {type(b).__name__}")
    if a == 0 or b == 0:
        return 0

    MAX = 10_000
    if abs(b) > MAX:
        raise ValueError(f"b={b} exceeds the maximum allowed magnitude ({MAX}) for this slow implementation")


    a_sign = a>0
    b_sign = b>0
    c_sign = 1 if a_sign == b_sign else -1
    c = 0
    for i in range(1, abs(b)+1):
        # c += abs(a)
        c = add_numbers(abs(a),c)
    return c_sign*c