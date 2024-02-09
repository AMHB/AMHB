teams = ['Iran', 'Spain', 'Portugal', 'Morocco']

results_library = {team: {'wins': 0, 'loses': 0, 'draws': 0, 'goal_difference': 0, 'points': 0, 'matches': []} for team in teams}

matches = []

print("Enter the results of the matches (Format: 'Team1-Score1-Team2-Score2', enter 'done' to finish):")
while True:
    match_input = input()
    if match_input.lower() == 'done':
        break
    
    match_data = match_input.split('-')
    if len(match_data) != 4:
        print("Invalid input format. Please enter in 'Team1-Score1-Team2-Score2' format.")
        continue
    
    try:
        home_team = match_data[0]
        home_score = int(match_data[1])
        away_team = match_data[2]
        away_score = int(match_data[3])

        matches.append({"home_team": home_team, "away_team": away_team, "home_score": home_score, "away_score": away_score})
    except ValueError:
        print("Invalid score. Please enter valid numeric scores.")
        continue

for match in matches:
    home_team = match['home_team']
    away_team = match['away_team']
    home_score = match['home_score']
    away_score = match['away_score']

    results_library[home_team]['matches'].append({'opponent': away_team, 'score': f"{home_score}-{away_score}"})
    results_library[away_team]['matches'].append({'opponent': home_team, 'score': f"{away_score}-{home_score}"})

    if home_score > away_score:
        results_library[home_team]['wins'] += 1
        results_library[home_team]['points'] += 3
    elif home_score < away_score:
        results_library[away_team]['wins'] += 1
        results_library[away_team]['points'] += 3
    else:
        results_library[home_team]['draws'] += 1
        results_library[away_team]['draws'] += 1
        results_library[home_team]['points'] += 1
        results_library[away_team]['points'] += 1

    results_library[home_team]['goal_difference'] += (home_score - away_score)
    results_library[away_team]['goal_difference'] += (away_score - home_score)

for team, stats in results_library.items():
    print(f"{team}  wins:{stats['wins']} , loses:{stats['loses']} , draws:{stats['draws']} , goal difference:{stats['goal_difference']} , points:{stats['points']} , matches: {stats['matches']}")
