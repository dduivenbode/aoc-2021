import os
import time
from collections import Counter

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_input(lines):
    result = []
    for line in lines:
        l = line.split(',')
        for i in l:
            result.append(int(i))
    return result


def get_count(input):
    d = {}
    for i in range(9):
        d[i] = 0
    count = Counter(input).most_common()
    for c in count:
        d[c[0]] = c[1]
    return d


def get_fish(dict, days):
    for i in range(days):
        new_fish = 0
        for d in dict:
            if d == 0:
                new_fish = dict[0]
            else:
                dict[d - 1] = dict[d]
        dict[6] = dict[6] + new_fish
        dict[8] = new_fish
    return dict


dict = get_count(get_input(lines))

fish = get_fish(dict, 80)
print('Total fish part1 is: ', sum(fish[f] for f in fish))

fish = get_fish(dict, 256)
print('Total fish part2 is: ', sum(fish[f] for f in fish))

end_time = time.time()
print("Execution time is :", "{:.4f}".format(end_time-start_time) + " seconds")
