import json

file = open("player_data.json", "r")
player_data = json.load(file)
file.close()

print(player_data)

player_data["username"] = 1000

file = open("player_data.json", "w")
json.dump(player_data, file)
file.close()
