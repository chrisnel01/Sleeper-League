import requests
import json

try:
    response = requests.get(
        "https://api.sleeper.app/v1/league/991955407021158400/rosters")
    users = requests.get(
        "https://api.sleeper.app/v1/league/991955407021158400/users")
    draft = requests.get(
        "https://api.sleeper.app/v1/draft/991955407893565440/picks")
    waiver_data = []
    
    for round_num in range(0, 17 + 1):
        url = f"https://api.sleeper.app/v1/league/991955407021158400/transactions/{round_num}"
        waiver = requests.get(url)
        waiver_data2 = waiver.json()
        waiver_data.extend(waiver_data2)

    
    # Parse the JSON responses directly
    player_data = draft.json()
    with open("players.json", 'r') as json_file:
        other_players = json.load(json_file)
    rosters = response.json()
    owners = users.json()
    
    waiver_data.extend(waiver_data2)
    
    # Fetch additional player data from another JSON file or API
    filtered_rosters = []
    filtered_player_data = []
    for player_info in player_data:
        filtered_player_data.append(
            {'player_id': player_info['metadata']['player_id'],
             'first_name': player_info['metadata']['first_name'],
             'last_name': player_info['metadata']['last_name'],
             'amount': player_info['metadata']['amount']})

    # Initialize the filtered_rosters list
    for entry in rosters:
        players_list = entry['players']
        owner_id = entry['owner_id']
        roster_id = entry['roster_id']
        display_name = ""
        for owner in owners:
            if owner['user_id'] == owner_id:
                display_name = owner['display_name']
                break

        # Initialize a list to store player information including 'id' and 'amount'
        players_with_id_and_amount = []

        for player in players_list:
            # Check if the player exists in filtered_player_data
            player_info = next(
                (draft_pick for draft_pick in filtered_player_data if draft_pick['player_id'] == player), None)

            if player_info:
                players_with_id_and_amount.append(player_info)
                continue
                
            
            for waiver_entry in waiver_data:
                adds = waiver_entry.get('adds')
                if adds is not None:
                    first_adds_value = next(iter(adds.keys()), None)
                    if first_adds_value == player:
                        for waiver_player in other_players:
                            if waiver_player['player_id'] == player:
                                players_with_id_and_amount.append(
                                    {'player_id': player, 'first_name': waiver_player['first_name'], 'last_name': waiver_player['last_name'], 'off_waiver': True})
                                break
                        break

        filtered_rosters.append(
            {'owner_id': owner_id, 'display_name': display_name, 'roster_id': roster_id, 'number of players': len(players_with_id_and_amount), 'players': players_with_id_and_amount})
    
    with open("rosters.json", "w") as json_file:
        json.dump(filtered_rosters, json_file,indent=4)

except Exception as e:
    print("Error:", e)
