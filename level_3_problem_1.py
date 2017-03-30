'''
Google foobar Level 3 Problem 1

Number of steps to get from any integer to 1. Each step can be: divide by 2, add 1, or subtract 1.
'''

def answer(n):
    n = int(n)
    steps = 0
    while n > 1:
        if n%2 == 0:
            n /= 2
            steps += 1
        elif n == 3:
            n -= 1
            steps += 1
        else:
            if ((n+1)/2)%2 == 0:
                n += 1
                steps += 1
            else:
                n -= 1
                steps += 1
    return steps