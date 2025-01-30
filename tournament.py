import itertools
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
"""
[
    [AB, CD],
    [EF, GH],
    ... x19 more

]

"""

for i in range(len(games)):
    schedule[i%days].append(games[i])

for i, day in enumerate(schedule):
    print(f"Day {i+1}: {day}")

def evaluate_schedule(schedule):
    max_days = 0
    for team in teams:
        # count the maximum number of days that a team plays in a row
        days = 0
        for day in schedule:
            if team in day[0] or team in day[-1]:
                days += 1
            else:
                max_days = max(max_days, days)
                days = 0
    return max_days

def schedule_tournament(schedule_so_far, remaining_games):
    if remaining_games == []:
        return [evaluate_schedule(schedule_so_far),schedule_so_far]
    fewwest_repeats = [100][0]

    for game in remaining_games:
        # option = schedule_tournament(schedule_so_far + [game], remaining_games - [game])
        # ^ needs replaced with the correct data format for days in the schedule. the for loop may need rewritten
        
        fewwest_repeats = option if (fewwest_repeats[0] > option[0]) else fewwest_repeats
    return fewwest_repeats
        

print(schedule_tournament([], games))
            
print(evaluate_schedule(schedule))