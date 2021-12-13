import os
import time
from functools import reduce

start_time = time.time()

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']

SCORING = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORING_AUTO = {')': 1, ']': 2, '}': 3, '>': 4}


def get_syntax_error_score(lines):
    syntax_errors = []

    for line in lines:
        open_tags = []
        for c in line:
            if c in OPEN:
                open_tags.append(c)
            else:
                if CLOSE.index(c) == OPEN.index(open_tags[-1]):
                    del open_tags[-1]
                else:
                    # print(
                    # f'Syntax error - Expected {CLOSE[OPEN.index(open_tags[-1])]}, but found {c} instead')
                    syntax_errors.append(c)
                    break

    return sum([SCORING[s] for s in syntax_errors])


def discard_corrupt_lines(lines):
    corrupt_lines = []
    for i, line in enumerate(lines):
        open_tags = []
        for c in line:
            if c in OPEN:
                open_tags.append(c)
            else:
                if CLOSE.index(c) == OPEN.index(open_tags[-1]):
                    del open_tags[-1]
                else:
                    corrupt_lines.append(i)
                    break
    lines = [line for i, line in enumerate(lines) if i not in corrupt_lines]
    return lines


def get_completion_strings(lines):
    closing_strings = []
    for line in lines:
        open_tags = []
        for c in line:
            if c in OPEN:
                open_tags.append(c)
            else:
                del open_tags[-1]
        # here we have the remaining closing tags in reverse order
        close = ''
        for x in reversed(open_tags):
            close = close + CLOSE[OPEN.index(x)]
        closing_strings.append(close)
    return closing_strings


def get_string_complete_score(compl_string):
    return reduce(lambda n, s: n*5 + SCORING_AUTO[s], compl_string, 0)
    # score = 0
    # for s in compl_string:
    #     score = score * 5
    #     score = score + SCORING_AUTO[s]
    # return score


print(get_syntax_error_score(lines))
inc_lines = discard_corrupt_lines(lines)
completion_strings = get_completion_strings(inc_lines)
scores = [get_string_complete_score(s) for s in completion_strings]
scores = sorted(scores)
print(scores[int(len(scores) / 2)])

end_time = time.time()
print("Execution time is :", "{:.5f}".format(end_time-start_time) + " seconds")
