import requests
import re
from passwords import DaylyInput
from itertools import islice 

passwordInput = DaylyInput().GetDaylyInput(2).content.decode('utf-8').splitlines()

Output = []
count = 0
for i in passwordInput:
    colon_split = i.split(": ")
    
    rules = colon_split[0]
    
    min_max_rules_split = rules.split(" ")
    min_max_split = min_max_rules_split[0].split("-")
    
    min = int(min_max_split[0])
    max = int(min_max_split[1])
    letter = min_max_rules_split[1]
    password = colon_split[1]

    occurrences = re.findall(letter, password)
    
    if (len(occurrences) >= min and len(occurrences) <= max):
        count += 1

print(count)