'''
Google foobar Level 4 Problem 2

Maximum flow through a network.

Code for Edmonds-Karp algorithm adapted from:
https://github.com/bigbighd604/Python/blob/master/graph/Edmonds-Karp.py
'''


import decimal
from collections import defaultdict


def EdmondsKarp(capacity, neighbors, start, end):
    flow = 0
    length = len(capacity)
    flows = [[0 for i in range(length)] for j in range(length)]
    while True:
        max, parent = BreadthFirstSearch(capacity, neighbors, flows, start, end)
        if max == 0:
            break
        flow = flow + max
        v = end
        while v != start:
            u = parent[v]
            flows[u][v] = flows[u][v] + max
            flows[v][u] = flows[v][u] - max
            v = u
    return flow


def BreadthFirstSearch(capacity, neighbors, flows, start, end):
    length = len(capacity)
    parents = [-1 for i in xrange(length)]
    parents[start] = -2
    M = [0 for i in xrange(length)]
    M[start] = decimal.Decimal('Infinity')

    queue = []
    queue.append(start)
    while queue:
        u = queue.pop(0)
        for v in neighbors[u]:
            if capacity[u][v] - flows[u][v] > 0 and parents[v] == -1:
                parents[v] = u
                M[v] = min(M[u], capacity[u][v] - flows[u][v])
                if v != end:
                    queue.append(v)
                else:
                    return M[end], parents
    return 0, parents


def collapse(entrances, exits, path):

    collapsed_entrances = [0 for x in range(len(path))]
    collapsed_exits = [0 for x in range(len(path))]
    direct_flow = 0

    for i in range(len(path)):
        for j in range(len(path[i])):
            if i in entrances and path[i][j] > 0:
                if j in exits:
                    direct_flow += path[i][j]
                    path[i][j] = 0
                else:
                    collapsed_entrances[j] += path[i][j]
            if j in exits and path[i][j] > 0:
                collapsed_exits[i] += path[i][j]

    if len(entrances) > 1:
        path[entrances[0]] = collapsed_entrances
        entrances.pop(0)
        for i in entrances:
            path[i] = [0 for x in range(len(path))]

    if len(exits) > 1:
        path = zip(*path)
        path[exits[0]] = collapsed_exits
        exits.pop(0)
        if exits:
            for i in exits:
                path[i] = [0 for x in range(len(path))]
        path = zip(*path)
    return path, direct_flow


def get_neighbors(path):
    neighbors = defaultdict(list)
    for vertex, flows in enumerate(path):
        for neighbor, flow in enumerate(flows):
            if flow > 0:
                neighbors[vertex].append(neighbor)
                neighbors[neighbor].append(vertex)
    return neighbors


def answer(entrances, exits, path):
    start = entrances[0]
    end = exits[0]
    capacity, direct_flow = collapse(entrances, exits, path)
    neighbors = get_neighbors(capacity)
    flow = EdmondsKarp(capacity, neighbors, start, end)
    return flow + direct_flow



