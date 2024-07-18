house_names = ["Blue", "Green", "Purple", "Red", "Yellow"]
houses = {c[0]:c for c in house_names}
teams = set([])

points = {houses[c]:0 for c in houses}

while True:
    match = input("Match Report: ")
    if match == "end":
        break
    match = match.split(",")

    try:
        team_names = match[1:]
        for name in team_names:
            assert (name[0] in houses) and (name[1:].isdigit())
            teams.add(name)
            break
    except:
        print("please enter a valid team name")

    N = int(match[0])

    winning_teams = match[1:N+1]

    for team in winning_teams:
        points[houses[team[0]]] += 1

house_teams = {house:[] for house in house_names}

for team in teams:
    for house in house_teams:
        if house[0] == team[0]:
            house_teams[house].append(team)

print("---- TEAMS ----")

for house in house_teams:
    print("{}: {}".format(house, ", ".join(house_teams[house])))

print("Teams: {}".format(len(" ".join(list(teams)))))

print("\n---- MATCH REPORT ----\n")


for team in points:
    print("{}: {}".format(team, points[team]))
