def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return keeper


def find_digit(k):
    """take one argument k, return a function f. The function f take one 
    digit n, to check if the digit n has the same digit in the inteval k.
    >>> f = find_digit(1)
    >>> f(1111)
    True
    >>> f(1234)
    False
    >>> f = find_digit(2)
    >>> f(1212)
    True
    >>> f(1234)
    False
    >>> f = find_digit(3)
    >>> f(123123)
    True"""

    def check(x):
        while x // (10**k) > 0:
            if x % 10 != (x // (10**k)) % 10:
                return False
            x = x // 10
        return True
    return check

        

    
    
    



