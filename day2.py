# https://adventofcode.com/2016/day/2

with open('input.txt') as fp:
    data = fp.readlines()

# data = """ULL
# RRDDD
# LURDL
# UUUUD""".splitlines()

digits = [[1,2,3],[4,5,6],[7,8,9]]

dirs = {
    'U': (0,-1),
    'D': (0,1),
    'L': (-1,0),
    'R': (1,0)
}

x,y = 1, 1
code = []
for line in data:
    line = line.strip()
    
    for move in line:
        dir = dirs[move]
        x += dir[0]
        y += dir[1]
        if x < 0: x = 0
        if x > 2: x = 2
        if y < 0: y = 0
        if y > 2: y = 2
    code.append(digits[y][x])

print(''.join(str(x) for x in code))