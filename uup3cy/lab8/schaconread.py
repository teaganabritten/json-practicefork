#!/usr/bin/python3

import json

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

output_file = 'schacon.csv'

with open(output_file, 'w') as file:
    for entry in data[:5]:
        name = entry.get('name', '')
        html_url = entry.get('html_url', '')
        updated_at = entry.get('updated_at', '')
        visibility = entry.get('visibility', '')
        line = f'{name},{html_url},{updated_at},{visibility}\n'
        file.write(line)

print(f"Data has been written to {output_file}")

