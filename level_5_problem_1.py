'''
Google foobar Level 5 Problem 1

Number of different nxm matrices with s different states allowing row and column swaps.
'''


from itertools import groupby
from fractions import gcd
from collections import Counter
from math import factorial


def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0


def generate_cycles(m):
    l = [[m]]
    if m == 1:
        return l
    for i in range(1, m/2+1):
        toadd = generate_cycles(m-i)
        toadd = [[i] + add for add in toadd]
        l.extend(toadd)
    return l


def generate_cycle_index(m):
    l = generate_cycles(m)
    l = [sorted(x) for x in l]
    l.sort()
    l = [x[0] for x in groupby(l)]

    coeffs = []
    for cycle in l:
        coeff = factorial(m)
        divisors = [x for x in cycle if x > 1]
        dups = Counter(cycle)
        dups = [factorial(x[1]) for x in dups.most_common() if x[1] > 1]
        divisors.extend(dups)
        for i in divisors:
            coeff /= i
        coeffs.append(coeff)

    l = [Counter(x).most_common() for x in l]
    l = [(coeffs[i],l[i])for i in range(len(coeffs))]
    return l


def combine_cycle_indices(a, b):
    new_cycle = []
    for coeff_a, term_a in a:
        for coeff_b, term_b in b:
            new_coeff = coeff_a * coeff_b
            new_term = []
            for subterm_a in term_a:
                for subterm_b in term_b:
                    subscript = lcm(subterm_a[0], subterm_b[0])
                    exponent = subterm_a[1] * subterm_b[1] * subterm_a[0] * subterm_b[0] / subscript
                    new_term.append((subscript, exponent))
            new_cycle.append((new_coeff, new_term))
    return new_cycle


def answer(w, h, s):
    column_cycle_index = generate_cycle_index(w)
    row_cycle_index = generate_cycle_index(h)
    combined_cycle_index = combine_cycle_indices(column_cycle_index, row_cycle_index)
    total = 0
    for coeff, term in combined_cycle_index:
        combined_term = sum([x[1] for x in term])
        to_add = coeff * (s ** combined_term)
        total += to_add
    total /= (factorial(w) * factorial(h))
    return str(total)





