with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def count_increases(lines):
  increases = 0
    # Using enumerate()
  for i, val in enumerate(lines):
    if i != 0:
      if int(lines[i]) > int(lines[i-1]):
        increases += 1
        # print(f"{lines[i]} is greater than {lines[i-1]}")

  return increases 

windows = []

# tranform lines to three-measurements window
for i, val in enumerate(lines):
  if i + 2 <= len(lines) - 1:
    windows.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))

print(f"Answer Part 1: {count_increases(lines)}")
print(f"Answer Part 2: {count_increases(windows)}")
