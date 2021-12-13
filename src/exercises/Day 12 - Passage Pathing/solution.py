import os
import time
from termcolor import colored, cprint

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_connections(lines):
    connections = {}
    for line in lines:
        con = line.split('-')
        if connections.get(con[0]):
            connections[con[0]].append(con[1])
        else:
            connections[con[0]] = [con[1]]
        if connections.get(con[1]):
            connections[con[1]].append(con[0])
        else:
            connections[con[1]] = [con[0]]
    return connections


def get_paths(path, connections, revisit=False):
    paths = []
    cave = path[-1]
    if cave == 'end':
        return [path]

    dest = connections[cave]
    # part1
    # dest = [d for d in dest if d.islower() == False or (
    #     d.islower() == True and d not in path)]
    visited_twice = False
    if revisit:
        for p in path:
            # visited a small cave twice already
            if p.islower() and path.count(p) > 1:
                visited_twice = True
                break

    if revisit and not visited_twice:
        dest = [d for d in dest if d.islower() == False or (
            d.islower() and path.count(d) < 2)]
    else:
        dest = [d for d in dest if d.islower() == False or (
            d.islower() and d not in path)]

    for d in dest:
        if d == 'start':
            continue
        paths.extend(get_paths(path + [d], connections, revisit))

    return paths


cons = get_connections(lines)
p1 = paths = get_paths(['start'], cons)
p2 = paths = get_paths(['start'], cons, True)

cprint('\nDay 12 - Passage Pathing:', 'blue', attrs=['bold'])
cprint(f'Paths through the cave part 1: {len(p1)}', 'green')
cprint(f'Paths through the cave part 2: {len(p2)}', 'green')

end_time = time.time()
print("\nExecution time is:", "{:.5f}".format(
    end_time-start_time) + " seconds")
