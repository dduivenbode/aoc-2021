import os
import time

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_positions(lines):
    positions = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            index = y * len(line) + x
            positions[index] = {
                'value': int(c),
                'flashed': False,
                'n_o_flashes': 0,
                'y': y,
                'x': x
            }
    return positions


def is_valid(x, y, octopus):
    return True if (x > -1 and x < len(octopus[0])) and (y > -1 and y < len(octopus)) else False


def add_energy(x, y, positions, octopus):
    if is_valid(x, y, octopus):
        position = positions[y * len(octopus[0]) + x]

        if position['flashed'] == False:
            position['value'] += 1
        if position['value'] > 9:
            position['value'] = 0
            position['flashed'] = True
            position['n_o_flashes'] += 1
            add_energy(x, y + 1, positions, octopus)
            add_energy(x, y - 1, positions, octopus)
            add_energy(x + 1, y, positions, octopus)
            add_energy(x - 1, y, positions, octopus)
            add_energy(x + 1, y + 1, positions, octopus)
            add_energy(x + 1, y - 1, positions, octopus)
            add_energy(x - 1, y + 1, positions, octopus)
            add_energy(x - 1, y - 1, positions, octopus)


def run_steps(steps, positions, octopus):
    for i in range(steps):
        for key, p in positions.items():
            p['flashed'] = False
        for key, p in positions.items():
            add_energy(p['x'], p['y'], positions, octopus)

        # print step output for testing
        # line = ''
        # print(f'After step {i + 1}')
        # for key, p in positions.items():
        #     line = line + str(p['value'])
        #     if key % int(len(octopus[0])) == len(octopus[0]) - 1:
        #         print(line)
        #         line = ''
        # print('-----')

        if all(p['flashed'] == True for key, p in positions.items()):
            print(f'All octopus flash at step {i + 1}')
    return positions


positions = get_positions(lines)
positions = run_steps(235, positions, lines)
print(sum([p['n_o_flashes']for key, p in positions.items()]))


end_time = time.time()
print("Execution time is :", "{:.5f}".format(end_time-start_time) + " seconds")
