'''
Google foobar Level 4 Problem 1

Lexicographically least subsets of a set of n integers whose union spans the entire set.
'''

from copy import deepcopy
from itertools import combinations


def generate_lookup_table():
    table = {}
    table[(2,2)] = [2,1]
    for n in range(1, 8):
        newkey = (2+n, 2)
        table[newkey] = [n+2] + table[2+n-1, 2]

    for nums in range(3, 10):
        for buns in range(nums, 10):
            newkey = (buns, nums)
            if nums == buns:
                newvalue = [nums, 1]
            else:
                toadd = table[(buns-1,nums-1)][0] + table[(buns-1,nums)][0]
                newvalue = [toadd] + table[(buns-1,nums)]
            table[newkey] = newvalue
    return table


def generate_solutions(num_buns, overlap):
    total_length = overlap[0]
    num_keys = overlap[1]

    count = num_buns*num_keys/total_length
    keys = []

    for i in range(num_buns):
        keys.append([])
    for i in range(total_length):
        prev_pos = 0
        for j in range(count):
            if j == 0 and i < num_keys:
                keys[0].append(i)
                continue
            curr_pos = prev_pos + 1
            while (len(keys[curr_pos]) == num_keys):
                curr_pos += 1
            while True:
                tempkey = deepcopy(keys[curr_pos])
                tempkey.append(i)

                to_break = False
                for k in range(len(overlap) - 2):
                    tocompare = list(combinations(keys[:curr_pos], k + 1))
                    tocompare = [list(x) for x in tocompare]
                    for compare in tocompare:
                        compare.append(tempkey)
                        tempoverlap = len(set(compare[0]).intersection(*compare))
                        if tempoverlap > overlap[k+2]:
                            curr_pos += 1
                            to_break = True
                            break
                    else:
                        continue
                    break
                if (to_break):
                    continue
                else:
                    keys[curr_pos].append(i)
                    prev_pos = curr_pos
                    break
    return keys


def answer(num_buns, num_required):
    if num_required == 0:
        return [[] for x in range(num_buns)]
    if num_required == num_buns:
        return [[x] for x in range(num_buns)]
    if num_required == 1:
        return [[0] for x in range(num_buns)]
    lookup = generate_lookup_table()
    ans = lookup[(num_buns, num_required)]
    keys = generate_solutions(num_buns, ans)
    return keys








