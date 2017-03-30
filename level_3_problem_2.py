'''
Google foobar Level 3 Problem 2

Number of staircases out of n blocks.
'''


def answer_n(diff, length):
    count = 0
    if length == 2:
        return (diff+1)/2
    else:
        num = (diff+length-1)/length
        for i in range(num):
            count += answer_n(diff - length*i, length - 1)
    return count


def answer(n):
    count = 0
    locations = [n - 1, 1]
    starting_locations = [n - 1, 1]
    while locations[0] > locations[1]:
        count += answer_n(locations[0] - locations[1], len(locations))
        starting_locations.append(0)
        starting_locations = [x+1 for x in starting_locations]
        starting_locations[0] -= len(starting_locations)
        locations = []
        for x in starting_locations:
            locations.append(x)
    return count