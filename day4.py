# https://adventofcode.com/2023/day/4

sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

def parse_line(line):
    left, right = line.split(" | ")
    card, nums = left.split(":")
    winning = [int(x) for x in nums.split()]
    plays = [int(x) for x in right.split()] 
    #print(card, winning, plays)
    return card, winning, plays

def score1(card, winning, plays):
    score = 0
    for play in plays:
        if play in winning:
            if not score:
                score = 1
            else:
                score *= 2
    return score

def score2(card, winning, plays):
    score = 0
    for play in plays:
        if play in winning:
            score += 1

    return score

with open("input4.txt") as fp:
    sample = fp.readlines()

total_score = 0
for line in sample:
    total_score += score1(*parse_line(line))
print("#1", total_score)

copies = [1 for x in sample]

for idx, line in enumerate(sample):
    score = score2(*parse_line(line))
    for i in range(score):
        copies[idx+i+1] += copies[idx]
    #break
sum = 0
for x in copies:
    sum += x

print("#2", sum)
