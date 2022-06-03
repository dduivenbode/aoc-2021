import os
import time
import copy
from collections import defaultdict
from queue import PriorityQueue
from termcolor import colored, cprint

# https://brilliant.org/wiki/dijkstras-short-path-finder/

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def multiply_lines(lines):
    nl1 = []
    nl2 = []
    for line in lines:
        s = ''
        for i in range(4):
            for c in line:
                if int(c) + i == 9:
                    s += '1'
                elif int(c) + i > 9:
                    s += str((int(c) + i) % 8)
                else:
                    s += str(int(c) + i + 1)
        line += s
        nl1.append(line)

    nl2 = copy.deepcopy(nl1)

    for i in range(4):
        for line in nl1:
            s = ''
            for c in line:
                if int(c) + i == 9:
                    s += '1'
                elif int(c) + i > 9:
                    s += str((int(c) + i) % 8)
                else:
                    s += str(int(c) + i + 1)
            nl2.append(s)
    return nl2


def get_graph(lines):
    graph = defaultdict(dict)
    pos = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            pos = y * len(line) + x
            graph[pos] = {
                'x': x,
                'y': y,
                'i': pos,
                'visited': False,
                'risk': int(c)
            }
    return graph, pos


def is_valid(x, y, width):
    return True if (x > -1 and x < MAX_WIDTH) and (y > -1 and y < MAX_WIDTH) else False


# def get_neighbours(v, q):
#     nodes = []
#     for n in q:
#         if n['x'] == v['x'] and n['y'] == (v['y'] - 1):
#             nodes.append(n)
#         if n['x'] == v['x'] and n['y'] == (v['y'] + 1):
#             nodes.append(n)
#         if n['x'] == (v['x'] - 1) and n['y'] == v['y']:
#             nodes.append(n)
#         if n['x'] == (v['x'] + 1) and n['y'] == v['y']:
#             nodes.append(n)
#     return nodes


def get_nodes(x, y, graph):
    nodes = []
    if is_valid(x, y + 1, MAX_WIDTH):
        nodes.append(graph[(y + 1) * MAX_WIDTH + x])
    if is_valid(x, y - 1, MAX_WIDTH):
        nodes.append(graph[(y - 1) * MAX_WIDTH + x])
    if is_valid(x + 1, y, MAX_WIDTH):
        nodes.append(graph[y * MAX_WIDTH + (x + 1)])
    if is_valid(x - 1, y, MAX_WIDTH):
        nodes.append(graph[y * MAX_WIDTH + (x - 1)])
    return [n for n in nodes if not n['visited']]

    # for each neighbour
    # if your min-dist = 0 or my-min-dist + your-risk is lower then yourt min-dist
    # min-dist = my-min-dist + your-risk


def get_distance(graph, source, target):
    q = PriorityQueue()
    source['dist'] = 0
    for _, v in graph.items():
        if v != source:
            v['dist'] = float('inf')

    q.put((0, source['i']))

    while not q.empty():
        # in a first iteration, used a normal array as q with every node in it.
        # this works, but putting everythin in an array, and getting the lowest is very inefficient, takes forever to finish
        # v = min(q, key=lambda x: x['dist'])

        v = graph[q.get()[1]]

        nodes = get_nodes(v['x'], v['y'], graph)
        for n in nodes:
            dist = v['dist'] + n['risk']
            if dist < n['dist']:
                n['dist'] = dist
                # made very big mistake here, only put changed entries in q
                # else q will keep growing
                q.put((dist, n['i']))
        v['visited'] = True
        if v == graph[target]:
            return v['dist']


lines = multiply_lines(lines)
MAX_WIDTH = len(lines[0])
graph, target = get_graph(lines)

shortest_path = get_distance(graph, graph[0], target)

cprint('\nDay 15 - Chiton:', 'blue', attrs=['bold'])
cprint(
    f'Shortest path through the cave: {shortest_path}', 'green', attrs=['bold'])

end_time = time.time()
print("\nExecution time is:", "{:.5f}".format(
    end_time-start_time) + " seconds")
