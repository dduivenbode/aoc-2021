import os
import time
from termcolor import colored, cprint

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'test-input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def hex_to_binary(hex):
    # https://www.kite.com/python/answers/how-to-convert-hexadecimal-into-binary-rounded-up-to-the-nearest-nibble-in-python
    end_length = len(hex) * 4
    hex_as_int = int(hex, 16)
    hex_as_binary = bin(hex_as_int)
    return hex_as_binary[2:].zfill(end_length)


def binary_to_num(bin):
    value = 1
    result = 0
    for i in range(len(bin), 0, -1):
        if bin[i - 1] == "1":
            result += value
        value = value * 2
    return result


print(binary_to_num('011111100101'))


cprint('\nDay 16 - Packet Decoder:', 'blue', attrs=['bold'])
cprint(f'', 'green', attrs=['bold'])

end_time = time.time()
print("\nExecution time is:", "{:.5f}".format(
    end_time-start_time) + " seconds")
