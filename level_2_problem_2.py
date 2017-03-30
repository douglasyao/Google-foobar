'''
Google foobar Level 2 Problem 2
'''

def answer(l):
    l = [x.split('.') for x in l]
    l.sort(key = lambda x: (int(x[0]), int(x[1]) if len(x) > 1 else None, int(x[2]) if len(x) > 2 else None))
    l = ['.'.join(x) for x in l]
    return l