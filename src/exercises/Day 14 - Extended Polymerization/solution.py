import os
import time
import copy
from collections import defaultdict
from collections import Counter
from termcolor import colored, cprint

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

rules = defaultdict(dict)
template = ''
for line in lines:
    if '->' in line:
        l = line.split(' -> ')
        rules[l[0]] = l[1]
    elif line:
        template = line


def run_step(result, rules):
    new_result = copy.deepcopy(result)

    for key, value in result.items():
        if value > 0:
            el1 = key[0] + rules[key]
            el2 = rules[key] + key[1]

            if new_result[el1]:
                new_result[el1] += value
            else:
                new_result[el1] = value

            if new_result[el2]:
                new_result[el2] += value
            else:
                new_result[el2] = value
            new_result[key] -= value

    return new_result


def step_zero(template):
    output = defaultdict(dict)
    i = 0
    while i < len(template) - 1:
        output[template[i:i+2]] = 1
        i += 1
    return output


def insert_pairs(steps, result, rules):
    for i in range(steps):
        result = run_step(result, rules)
    return result
    # return line


def get_line_length(steps, l_length):
    for i in range(steps):
        l_length = l_length + l_length - 1
    return l_length


def get_count(result, start):
    count = defaultdict(dict)
    elements = set()
    for key, value in result.items():
        elements.add(key[0])
        elements.add(key[1])

    for el in elements:
        n = 0
        for key, value in result.items():
            if key[0] == el and key[1] == el:  # for instance BB
                n = n + value * 2
            elif el in key:
                n += value
        if el == start[0] or el == start[-1]:
            n += 1
        count[el] = int(n/2)

    return count


start = step_zero(template)
result = insert_pairs(40, start, rules)
count = get_count(result, template)


cprint('\nDay 14 - Extended Polymerization:', 'blue', attrs=['bold'])

c = Counter(count)
mc = c.most_common()
print(f'\nMost commmon element {mc[0][0]} occurs {mc[0][1]} times')
print(f'Least commmon element {mc[-1][0]} occurs {mc[-1][1]} times')
print(f'{mc[0][1]} - {mc[-1][1]} = {mc[0][1] - mc[-1][1]}')

end_time = time.time()
print("\nExecution time is:", "{:.5f}".format(
    end_time-start_time) + " seconds")
