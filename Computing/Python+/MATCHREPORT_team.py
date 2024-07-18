house_names = ["Blue", "Green", "Purple", "Red", "Yellow"]
houses = {c[0]:c for c in house_names}

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
            break
    except:
        print("please enter a valid team name")

    N = int(match[0])

    winning_teams = match[1:N+1]

    for team in winning_teams:
        points[houses[team[0]]] += 1


print("\n---- MATCH REPORT ----\n")


for team in points:
    print("{}: {}".format(team, points[team]))


