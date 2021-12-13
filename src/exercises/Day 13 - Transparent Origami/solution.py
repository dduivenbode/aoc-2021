import os
import time
import math
from termcolor import colored, cprint

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def transform_input(lines):
    folds = []
    points = []
    for line in lines:
        if line.startswith('fold'):
            l = line.split()
            f = l[2].split('=')
            folds.append((f[0], int(f[1])))
        elif line:
            l = line.split(',')
            points.append({'x': int(l[0]), 'y': int(l[1])})
    return points, folds


def fold(points, fold_at):
    line = fold_at[0]
    at = fold_at[1]

    for p in points:
        if p[line] > at:
            p[line] = at - (p[line] - at)

    points = [p for p in points if p[line] < at]
    # remove duplicates
    np = []
    for p in points:
        if p not in np:
            np.append(p)
    return np


def fold_paper(n_o_folds, folds, points):
    for i in range(n_o_folds):
        points = fold(points, folds[i])
    return points


def print_code(points):
    xmax = 0
    ymax = 0
    for p in points:
        if p['x'] > xmax:
            xmax = p['x']
        if p['y'] > ymax:
            ymax = p['y']

    div = xmax + 1
    line = ''
    for i in range(div*ymax + div):
        x = i % div
        y = math.floor(i/div)
        found = [p for p in points if p['x'] == x and p['y'] == y]
        # very nice coloring :)
        line += colored('#', 'white', 'on_red') if len(found) > 0 else ' '
        if (i + 1) % div == 0 and i != 0:
            print(line)
            line = ''
        # line += '#' if len(found) > 0 else '.'
        # if (i + 1) % div == 0 and i != 0:
        #     cprint(line, 'red', 'on_white')
        #     line = ''


cprint('\nDay 13 - Transparent Origami:', 'blue', attrs=['bold'])
points, folds = transform_input(lines)
cprint(
    f'Number of points after one fold: {len(fold_paper(1,folds,points))}', 'green')
cprint(
    f'Manual code:\n', 'green')
print_code(fold_paper(len(folds), folds, points))

end_time = time.time()
print("\nExecution time is:", "{:.5f}".format(
    end_time-start_time) + " seconds")
