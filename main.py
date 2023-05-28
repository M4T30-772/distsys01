import json

# Specify the file path
file_path = 'working_json.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the contents of the JSON file
for name in data:
    if name.URL('d') or name.startswith('w'):
        print(name)