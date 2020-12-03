import requests
import re

from itertools import islice 


passwordInput = response.content.decode('utf-8').splitlines()

Output = []
count = 0
for i in passwordInput:
    colon_split = i.split(": ")
    
    rules = colon_split[0]
    
    min_max_rules_split = rules.split(" ")
    min_max_split = min_max_rules_split[0].split("-")
    
    pos1 = int(min_max_split[0])
    pos2 = int(min_max_split[1])
    letter = min_max_rules_split[1]
    password = colon_split[1]

    
    if (((password.find(letter, pos1 - 1) + 1) == pos1) != ((password.find(letter, pos2 - 1) + 1) == pos2)):
        count += 1

print(count)