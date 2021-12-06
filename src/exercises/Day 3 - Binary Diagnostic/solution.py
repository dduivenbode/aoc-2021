from collections import Counter

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def getNewLines(lines):
    newLines = []
    for n in lines[0]:
        newLines.append([])

    for line in lines:
        for i, c in enumerate(line):
            newLines[i].append(c)
    return newLines


def convertBinary(bin):
    value = 1
    result = 0
    for i in range(len(bin), 0, -1):
        if bin[i - 1] == "1":
            result += value
        value = value * 2
    return result


def ex1(lines):
    alpha = ""
    for l in getNewLines(lines):
        alpha += Counter(l).most_common(1)[0][0]

    epsilon = ["1" if c == "0" else "0" for c in alpha]
    return convertBinary(alpha) * convertBinary(epsilon)


def ex2(lines):
    r = list(range(len(lines)))
    oxygen_rating = convertBinary(
        getValue(lines, r, 'most', '1', len(lines[0]) - 1))
    scrubber_rating = convertBinary(
        getValue(lines, r, 'least', '0', len(lines[0]) - 1))
    return scrubber_rating * oxygen_rating


def getCount(lines, index, pos):
    l = []
    for i in index:
        l.append(lines[i][pos])
    return Counter(l).most_common()


def getValue(lines, r, common, tie, maxpos, pos=0):
    count = getCount(lines, r, pos)

    if len(count) == 1:
        bit = count[0][0]
    else:
        # if equal take tiebreaker
        if count[0][1] == count[1][1]:
            bit = tie
        else:
            bit = count[0][0] if common == 'most' else count[1][0]

    r = [n for n in r if lines[n][pos] == bit]
    if len(r) == 1:
        return lines[r[0]]
    else:
        pos += 1 if pos < maxpos else 0
        return getValue(lines, r, common, tie, maxpos, pos)


print(f"Answer Part 1: {ex1(lines)}")
print(f"Answer Part 2: {ex2(lines)}")
