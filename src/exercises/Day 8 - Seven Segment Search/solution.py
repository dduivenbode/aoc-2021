import os
import time
from collections import Counter
from functools import reduce

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_input(lines):
    input = []
    for i, line in enumerate(lines):
        s = line.split(' | ')
        input.append((s[0].split(' '), s[1].split(' ')))
    return input


def key_accumulator(acc, key):
    l = len(key)
    if l not in acc:
        acc[l] = 1
    else:
        acc[l] = acc[l] + 1
    return acc


def count_unique_input(input):
    c = 0
    key_acc = reduce(key_accumulator, input[0][0], {})
    for inp in input:
        for v in inp[1]:
            if key_acc[len(v)] == 1:
                c += 1
    return c


def get_pattern_dict(pattern):
    d = {}
    # get known numbers
    for p in pattern:
        if len(p) == 2:
            d[1] = p
        if len(p) == 4:
            d[4] = p
        if len(p) == 3:
            d[7] = p
        if len(p) == 7:
            d[8] = p

    # get lenght 6
    for p in pattern:
        if len(p) == 6:
            if list(set(list(d[8])) - set(list(p)))[0] in list(d[1]):
                d[6] = p
            if list(set(list(d[8])) - set(list(p)))[0] not in list(d[4]):
                d[9] = p

    pattern = [p for p in pattern if p not in list(d.values())]
    d[0] = [p for p in pattern if len(p) == 6][0]
    pattern.remove(d[0])

    # only length 5 left here
    bottom_right = [c for c in list(d[1]) if c in list(d[6])][0]
    for p in pattern:
        if len(set(list(d[6])) - set(list(p))) == 1:
            d[5] = p
        if bottom_right not in list(p):
            d[2] = p

    pattern = [p for p in pattern if p not in list(d.values())]
    d[3] = pattern[0]
    return d


def get_numeric_value(p, value):
    for d in p:
        if len(p[d]) == len(value) and len(set(list(p[d])) - set(list(value))) == 0:
            return str(d)


def get_output_value(pattern, values):
    i = ''
    p = get_pattern_dict(pattern)
    for v in values:
        i += get_numeric_value(p, v)
    return int(i)


def get_sum_of_input(input):
    n = []
    for inp in input:
        n.append(get_output_value(inp[0], inp[1]))
    return sum(n)


input = get_input(lines)
print(count_unique_input(input))
print(get_sum_of_input(input))


end_time = time.time()
print("Execution time is :", "{:.4f}".format(end_time-start_time) + " seconds")
