import os
import time

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def line_to_int(line, sep):
    strings = line.split(sep)
    return [int(n) for n in strings if n]


def transform_line(line):
    l = line.replace(' -> ', ',')
    input = l.split(',')
    return [int(n) for n in input]


def get_result(lines):
    result = {}
    for line in lines:
        input = transform_line(line)
        c = get_coordinates(input[0], input[1], input[2], input[3])
        for n in c:
            if result.get(n):
                result[n] = result[n] + 1
            else:
                result[n] = 1
    return result


def get_coordinates(x1, y1, x2, y2):
    # horizontal line
    coordinates = []
    if x1 == x2:
        values = sorted([y1, y2])
        while values[0] <= values[1]:
            coordinate = f'{x1},{values[0]}'
            coordinates.append(coordinate)
            values[0] += 1
    # vertical line
    elif y1 == y2:
        values = sorted([x1, x2])
        while values[0] <= values[1]:
            coordinate = f'{values[0]},{y1}'
            coordinates.append(coordinate)
            values[0] += 1
    # diagonal line
    elif abs(x1 - x2) == abs(y1 - y2):
        while x1 != x2:
            coordinate = f'{x1},{y1}'
            coordinates.append(coordinate)
            x1 = x1 + 1 if x1 < x2 else x1 - 1
            y1 = y1 + 1 if y1 < y2 else y1 - 1

        coordinates.append(f'{x2},{y2}')

    return coordinates


result = get_result(lines)

# sum dictionary in ugly for loop

# n = 0
# for coordinate, number in result.items():
#     if number > 1:
#         n += 1

# nicer one-line
print(sum(1 for c in result if result[c] > 1))

end_time = time.time()

print("Execution time is :", "{:.2f}".format(end_time-start_time) + " seconds")
