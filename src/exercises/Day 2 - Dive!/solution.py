with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def change_position(value, change, func):
  return func(value,change)

def add(a,b):
  return a + b

def sub(a,b):
  return a - b  

def mult(a,b):
  return a * b    

def determine_positions(lines):
  horizontal = 0
  depth = 0
  for line in lines:
    input = line.split(" ")
    if input[0] == 'forward':
      horizontal = change_position(horizontal, int(input[1]), lambda a,b : a+b )
    else:
      depth = change_position(depth,int(input[1]), add if input[0] == 'down' else sub)  

  return (horizontal,depth)

def determine_positions2(lines):
  horizontal = 0
  depth = 0
  aim = 0
  for line in lines:
    input = line.split(" ")
    if input[0] == 'forward':
      horizontal = change_position(horizontal, int(input[1]), add)
      depth = depth + change_position(aim, int(input[1]), mult)
    else:
      aim = change_position(aim,int(input[1]), add if input[0] == 'down' else sub)  

  return (horizontal,depth)  

h,d = determine_positions(lines)
x,z = determine_positions2(lines)
print(f"Answer Part 1: {h * d}")
print(f"Answer Part 2: {x * z}")
