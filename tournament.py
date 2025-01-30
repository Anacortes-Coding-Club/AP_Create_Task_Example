"""Schedule a 7-team tournament"""

teams = list("ABCDEFG")
games = []
for i in range(len(teams)):
    for j in range(i+1, len(teams)):
        games.append(teams[i]+teams[j])
# how many games?
print(len(games), games)
# how many days for 2 games per day?
days = len(games)//2+1

# schedule the games
schedule = [[] for _ in range(int(days))]
for i in range(len(games)):
    schedule[i%days].append(games[i])

for i, day in enumerate(schedule):
    print(f"Day {i+1}: {day}")
