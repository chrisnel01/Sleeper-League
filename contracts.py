import json
import csv

csv_file = "contracts.csv"

three_year_contracts = []
two_year_contracts = []

# Read data from the CSV file
with open(csv_file, mode="r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    for row in reader:
        # Check if both columns have values and are not empty
        if len(row) == 2 and all(cell.strip() != "" for cell in row):
            # Extract only the player_id
            three_year_contracts.append(row[0].split(":")[0])
            two_year_contracts.append(row[1].split(":")[0])

with open("rosters.json", "r") as json_file:
    json_data = json.load(json_file)
    
rosters_json_players = set()

for obj in json_data:
    for player in obj["players"]:
        player_id = player["player_id"]
        rosters_json_players.add(player_id)
        if player_id in three_year_contracts:
            player["contract"] = "3"
        elif player_id in two_year_contracts:
            player["contract"] = "2"
        else:
            player["contract"] = "1"
            
for player_name in three_year_contracts:
    if player_name and player_name not in rosters_json_players:
        print(f"Error: Player '{player_name}' not found in rosters.json")

for player_name in two_year_contracts:
    if player_name and player_name not in rosters_json_players:
        print(f"Error: Player '{player_name}' not found in rosters.json")

with open("rosters.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)