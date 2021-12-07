import os
import time
import math

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_positions(lines):
    numbers = []
    for line in lines:
        numbers.extend([int(i) for i in line.split(',')])
    return numbers


def get_fuel_consumption_linear(positions, n):
    return sum(abs(p - n) for p in positions)


def get_fuel_consumption_exponential(positions, n):
    # get steps and calculate fuel consumption in mapper and sum the map
    return sum(map(lambda i: int(i * (i + 1) / 2), [(lambda p:abs(p-n))(p) for p in positions]))

    # steps to get to the oneliner
    # fuel = 0
    # for p in positions:
    #     steps = abs(p-n)
    #     # my fist ugly loop to count
    #     # i = 1
    #     # while i <= steps:
    #     #     moves = moves + i
    #     #     i = i + 1

    #     #  formula to sum range of integers
    #     fuel = fuel + steps * (steps + 1) / 2
    # return fuel


def get_test_positions(targets):
    if len(targets) == 2:
        return targets[0], targets[1]
    else:
        i1 = math.floor(len(targets) / 2)
        i2 = i1 + 1
        return targets[i1], targets[i2]


def determine_position(positions, f_fuel_consumption):
    targets = list(range(min(positions), max(positions) + 1))
    return find_position(positions, targets, f_fuel_consumption)


def find_position(positions, targets, f_fuel_consumption):
    # get the 2 middle entries
    t1, t2 = get_test_positions(targets)
    # get fuel consumption for both possible positions
    r1 = f_fuel_consumption(positions, t1)
    r2 = f_fuel_consumption(positions, t2)

    # remove part of list from highest result
    if r1 < r2:
        targets = [t for t in targets if t < t2]
    else:
        targets = [t for t in targets if t > t1]

    return targets[0] if len(targets) == 1 else find_position(positions, targets, f_fuel_consumption)


positions = get_positions(lines)
p1 = determine_position(positions, get_fuel_consumption_linear)
p2 = determine_position(positions, get_fuel_consumption_exponential)
print(f"Crabs fuel use part 1: {get_fuel_consumption_linear(positions, p1)}")
print(
    f"Crabs fuel use part 2: {get_fuel_consumption_exponential(positions, p2)}")

end_time = time.time()
print("Execution time is :", "{:.4f}".format(end_time-start_time) + " seconds")
