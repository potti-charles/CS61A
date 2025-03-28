def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)
    
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * skip_factorial(n - 2)


def is_prime(n):
    def f(i):
        if n % i == 0 and n != i:
            return False
        elif n == i:
            return True
        else:
            return f(i + 1)
    return f(2)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        elif i % 7 == 0 or has_seven(i):
            print("we got a seven here, i is ", i, "who is ", who, "direction is ", direction)
            direction = -direction
            i = i + 1
            who = (who + direction) % k
            if who == 0:
                who = k
            return f(i, who, direction)
            print("we now return to the f({i}, {who}, {direction}")
        else:
            i = i + 1
            who = (who + direction) % k
            if who == 0:
                who = k
            return f(i, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)