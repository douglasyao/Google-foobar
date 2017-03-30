'''
Google foobar Level 2 Problem 1
'''

def answer(total_lambs):
    maximum = 0
    while 2**(maximum+1)-1 <= total_lambs:
        maximum += 1

    minimum_count = 0
    prev_minimum = 1
    next_minimum = 1
    while prev_minimum + next_minimum - 1 <= total_lambs:
        temp = next_minimum
        next_minimum += prev_minimum
        prev_minimum = temp
        minimum_count += 1
    return minimum_count-maximum