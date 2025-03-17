def race(x, y):
    assert x > 0 and y > 0 and x >= y/2 and x < y, "The hare must be faster than the turtle but not too fast"
    t = 0
    hare = 0
    turtle = 0
    while hare > turtle or t == 0:
        t += 1
        if t // 5 % 2 == 0:
            turtle = t * x
            hare = t // 5 // 2 * y * 5 + t % 5 * y
        else:
            turtle = t * x
            hare = (t // 5 // 2 + 1) * y * 5
    if hare == turtle:
        print(f"It's a tie at {t} mim with distance {hare} and the turtle with distance {turtle}")
    else:
        print(f"The turtle wins at {t} min with distance {turtle} and the hare with distance {hare}")


def fizzbuzz(n):
    assert n > 0 and isinstance(n, int), "The input must be a positive integer"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

def is_prime(n):
    assert n > 0 and isinstance(n, int), "The input must be a positive integer"
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def unique_digit(n):
    assert n > 0 and isinstance(n, int), "The input must be a positive integer"
    def has_digit(n, k):
        while n > 0:
            if n % 10 == k:
                return True
            n = n // 10
        return False
    i = 1
    u = 0
    while i < 10:
        if has_digit(n, i):
            u += 1
        i += 1
    return u

    