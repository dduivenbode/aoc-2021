import os
import time

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


class LowPoint:
    def __init__(self, cave, value, level, pos):
        self.cave = cave
        self.value = value
        self.level = level
        self.pos = pos

        self.index = level * len(cave[0]) + pos

    def get_risk(self):
        return int(self.value) + 1

    def get_value(self):
        return self.value

    def get_basin_size(self):
        return len(self.get_surrounding_basin_points()) + 1

    def get_surrounding_basin_points(self, points=None):
        if not points:
            points = set()
        newpoints = []
        up, down, left, right = get_directions(
            self.cave, self.cave[self.level], self.level, self.pos)
        if up:
            checkvalue = self.cave[self.level - 1][self.pos]
            if checkvalue > self.value and checkvalue != '9':
                newpoints.append(LowPoint(self.cave, checkvalue,
                                          self.level - 1, self.pos))
        if down:
            checkvalue = self.cave[self.level + 1][self.pos]
            if checkvalue > self.value and checkvalue != '9':
                newpoints.append(LowPoint(self.cave, checkvalue,
                                          self.level + 1, self.pos))
        if left:
            checkvalue = self.cave[self.level][self.pos - 1]
            if checkvalue > self.value and checkvalue != '9':
                newpoints.append(LowPoint(self.cave, checkvalue,
                                          self.level, self.pos - 1))
        if right:
            checkvalue = self.cave[self.level][self.pos + 1]
            if checkvalue > self.value and checkvalue != '9':
                newpoints.append(LowPoint(self.cave, checkvalue,
                                          self.level, self.pos + 1))

        for p in newpoints:
            points.add(p.index)
            points = p.get_surrounding_basin_points(points)

        return points


def get_directions(lines, line, lines_i, line_i):
    up = True if lines_i != 0 else False
    down = True if lines_i != len(lines) - 1 else False
    left = True if line_i != 0 else False
    right = True if line_i != len(line) - 1 else False
    return up, down, left, right


def is_low_point(lines, line, lines_i, line_i):
    up, down, left, right = get_directions(lines, line, lines_i, line_i)

    check_points = []
    if up:
        check_points.append(lines[lines_i - 1][line_i])
    if down:
        check_points.append(lines[lines_i + 1][line_i])
    if left:
        check_points.append(line[line_i - 1])
    if right:
        check_points.append(line[line_i + 1])

    for c in check_points:
        if c <= line[line_i]:
            return False
    return True


def get_low_points(lines):
    low_points = []
    for i, line in enumerate(lines):
        for n, c in enumerate(line):
            if is_low_point(lines, line, i, n):
                low_points.append(LowPoint(lines, c, i, n))
    return low_points


low_points = get_low_points(lines)

risk = sum([p.get_risk() for p in low_points])
print(f'Cave risk level: {risk}')

low_points.sort(key=lambda x: x.get_basin_size(), reverse=True)
mult = low_points[0].get_basin_size(
) * low_points[1].get_basin_size() * low_points[2].get_basin_size()
print(f'Basin multiplier: {mult}')

end_time = time.time()
print("Execution time is :", "{:.5f}".format(end_time-start_time) + " seconds")
