import re
from words import word

with open('C:/Users/abdea/OneDrive/Desktop/Code/Edgar_lookup/cik-lookup-data.txt', 'r') as f:
    cik_data = f.readlines()

for search_string in word:
    searching_strings = search_string.strip().upper()
    found = False
    for line in cik_data:
        if re.match(f"{searching_strings}:", line):
            print(line.strip())
            found = True
            break
    if not found:
        print(f"No results found for {search_string}")
