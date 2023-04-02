import re
from words import word
from tqdm import tqdm

with open('C:/Users/abdea/OneDrive/Desktop/Code/Edgar_lookup/cik-lookup-data.txt', 'r') as f:
        cik_data = f.readlines()

cik_data_str = ''.join(cik_data)

with open('output.txt', 'w') as f:
        for searchString in tqdm(word):
                searchable= searchString.strip().upper()
                s = r"^.*{}.*$".format(searchable)
                pattern = re.compile(s,re.MULTILINE)
                out = pattern.search(cik_data_str)
                if out:
                        f.write(out.group(0) + "\n")
