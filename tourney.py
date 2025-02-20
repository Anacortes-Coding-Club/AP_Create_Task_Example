"""Schedule a 7-team tournament"""


def check_schedule(teams, schedule):
    # print("Checking schedule for teams", teams)
    games = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            games.append(set(teams[i] + teams[j]))

    errors = []
    # check that no team plays twice on the same day
    for day in schedule:
        # contruct a set of all teams playing on the day
        day_teams = set()
        for game in day:
            day_teams.update(game)
        if len(day_teams) != len(day) * 2:
            errors.append(f"Team plays twice on day {day}")

    # check that all games are present in schedule
    for game in games:
        found = False
        for day in schedule:
            if game in day:
                found = True
                break
        if not found:
            errors.append(f"Game {game} not found in schedule")
            break

    # find the duplicate games in schedule
    for i, day in enumerate(schedule):
        for j, other_day in enumerate(schedule):
            if i != j:
                for game in day:
                    if game in other_day:
                        errors.append(
                            f"Duplicate game {game} found in days {i+1} and {j+1}"
                        )
                        break

    # check that no team plays more than 2 days in a row
    for team in teams:
        days_played = []
        for i, day in enumerate(schedule):
            for game in day:
                if team in game:
                    days_played.append(i)

        # print(f"Team {team} plays on days {days_played}")
        for i in range(2, len(schedule)):
            if all(j in days_played for j in range(i - 2, i + 1)):
                errors.append(f"Team {team} plays 3 days in a row on days {i-2} to {i}")

    # if errors:
    #     for error in errors:
    #         print(error)
    return errors


def b2b_count(teams, schedule):
    """Count the number of back-to-back games for each team"""

    b2b_counts = dict()
    for team in teams:
        b2b_count = 0
        days_played = []
        for i, day in enumerate(schedule):
            for game in day:
                if team in game:
                    days_played.append(i)
        for i in range(1, len(schedule)):
            if all(j in days_played for j in range(i - 1, i + 1)):
                b2b_count += 1
        b2b_counts[team] = b2b_count
    return sum(b2b_counts.values())


def generate_schedule(teams):
    games = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            games.append(set(teams[i] + teams[j]))

    # initialize a schedule of length games//2+1
    schedule = [[] for _ in range((len(games) // 2) + 1)]

    # add the games to the schedule
    schedule = fill_schedule(schedule, teams, games)

    return schedule


def fill_schedule(schedule, teams, games):
    if not games:
        return schedule

    game = games.pop(0)
    for i, day in enumerate(schedule):
        # if day is not full, see if we can add the game to the day
        if len(day) < 2:
            # check that no team plays twice on the same day
            if not any(team in game for other_game in day for team in other_game):
                # check that no team plays more than 2 days in a row
                if i < 2 or not all(
                    team in game
                    for other_game in schedule[i - 2 : i + 1]
                    for team in other_game
                ):
                    new_schedule = [day[:] for day in schedule]
                    new_schedule[i].append(game)
                    result = fill_schedule(new_schedule, teams, games)
                    if result and not check_schedule(teams, result):
                        return result
    games.insert(0, game)
    return None


foo = generate_schedule("ABCDE")
check_schedule("ABCDE", foo)
print(foo)

five = """AB, CD
AC, DE
BD, 
CE,
AD, BE

AE, BC"""

tournament_schedule = """AB, CD
EF, AG
BC, AC
FG, DE
BD, EG
CF
DF, AE
DG, BF
BE, AF
AD, CG
CE, BG"""


"""performance:

[Running] python -u "/workspaces/AP_Create_Task_Example/tourney.py"
[[{'B', 'A'}, {'D', 'C'}], [{'A', 'C'}, {'B', 'E'}], [{'D', 'E'}], [{'D', 'A'}, {'B', 'C'}], [{'E', 'A'}], [{'B', 'D'}, {'E', 'C'}]]

[Done] exited with code=0 in 0.591 seconds

[Running] python -u "/workspaces/AP_Create_Task_Example/tourney.py"
[[{'A', 'B'}, {'E', 'D'}], [{'C', 'A'}, {'E', 'F'}], [{'C', 'B'}, {'F', 'D'}], [{'A', 'D'}, {'E', 'B'}], [{'A', 'E'}, {'C', 'F'}], [{'B', 'D'}], [{'A', 'F'}, {'C', 'D'}], [{'F', 'B'}, {'C', 'E'}]]

[Done] exited with code=0 in 59.236 seconds

"""

# parse the schedule
# mads_schedule = [[set(game) for game in day.split(", ")] for day in three.split("\n")]
# print(mads_schedule)

# check_schedule("ABCDEFG", mads_schedule)


# b2b_count_result = b2b_count(teams, mads_schedule)
# print("Total Back-to-Back Games:", b2b_count_result)


def solve(game_index, day_index, schedule):
    """Recursive function to build the schedule"""

    if game_index == len(games):  # All games scheduled
        b2b = b2b_count(teams, schedule)
        if b2b != -1:
            return schedule, b2b
        else:
            return None, -1

    if day_index == days:  # No more days, but not all games scheduled
        return None, -1

    for i in range(3):  # Try 0, 1 or 2 games on current day
        if i == 0:
            new_schedule = [day[:] for day in schedule]
            result, b2b = solve(game_index, day_index + 1, new_schedule)
            if result:
                return result, b2b

        elif (
            i > 0 and game_index < len(games) and len(schedule[day_index]) < 2
        ):  # Try scheduling a game
            new_schedule = [day[:] for day in schedule]
            new_game = games[game_index]

            # Check if either team in the new game has already played today
            teams_in_game = set(new_game)
            teams_played_today = set()
            for existing_game in new_schedule[day_index]:
                teams_played_today.update(existing_game)

            if not teams_in_game.intersection(
                teams_played_today
            ):  # No team plays twice on the same day
                new_schedule[day_index].append(new_game)
                result, b2b = solve(game_index + 1, day_index, new_schedule)
                if result:
                    return result, b2b

    return None, -1  # No valid schedule found from this point
