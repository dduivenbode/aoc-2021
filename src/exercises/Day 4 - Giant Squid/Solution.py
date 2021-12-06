import os

dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir, 'input.txt')

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def line_to_int(line, sep):
    strings = line.split(sep)
    return [int(n) for n in strings if n]


numbers = []
boards = []
board_width = 0

for i, line in enumerate(lines):
    if i == 0:  # these are the bingo numbers
        numbers = line_to_int(line, ',')
    else:  # these are the boards
        if not line:
            boards.append([])
            board_index = len(boards) - 1
        else:
            boards[board_index].extend(line_to_int(line, ' '))
            if board_width == 0:
                board_width = len(boards[board_index])


def mark_hits(boards, number):
    for b in boards:
        try:
            i = b.index(number)
            b[i] = 'X'
        except ValueError:
            continue
    return boards


def check_field(board, width, inc, start, counter=0):
    if board[start] == 'X':
        if width - 1 == counter:
            return True
        else:
            start = start + inc
            counter += 1
            return check_field(board, width, inc, start, counter)
    else:
        return False


def check_horizontal(board, width):
    start = 0
    for _ in range(width):
        win = check_field(board, width, 1, start)
        if win:
            return True
        else:
            start += width
    return False


def check_vertical(board, width):
    for n in range(width):
        win = check_field(board, width, width, n)
        if win:
            return True
    return False


def check_winners(boards, width):
    winning_boards = []
    for i, b in enumerate(boards):
        if check_horizontal(b, width):
            winning_boards.append(i)
            continue
        if check_vertical(b, width):
            winning_boards.append(i)

    return winning_boards


def play_bingo(numbers, boards, width, n_o_boards):
    first_found = False
    for i, n in enumerate(numbers):
        boards = mark_hits(boards, n)
        if i >= width - 1:  # no point in checking winner before at least width amount of numbers
            result = check_winners(boards, width)
            if result:
                if not first_found:  # this is the first winner
                    print(
                        f"The first winning board score: {get_remaining_number(boards[result[0]]) * n}")
                    first_found = True
                if len(result) == n_o_boards:  # this is the last winner
                    print(
                        f"The last winning board score: {get_remaining_number(boards[result[-1]]) * n}")
                    return

                result.sort(reverse=True)
                for x in result:
                    del boards[x]
                    n_o_boards -= 1


def get_remaining_number(board):
    result = 0
    for n in board:
        if isinstance(n, int):
            result += n
    return result


winning_board = play_bingo(numbers, boards, board_width, len(boards))
# print(get_remaining_number(boards[winning_board[0]]) * winning_board[1])
