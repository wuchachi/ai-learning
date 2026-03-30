import json

#opens and loads JSON file
with open("person.json", "r") as file:
    data = json.load(file)

#prints whole thing to see structure
print("Full Data: ", data)
print()

# Access specific values by key
print("Name:", data["name"])
print("Goal:", data["goal"])
print()

# Loop through the skills array
print("Skills:")
for skill in data["skills"]:
    print(" -", skill)