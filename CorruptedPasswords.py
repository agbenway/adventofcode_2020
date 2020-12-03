from Helper import Helper
from passwords import DaylyInput
import re

passwordInput = DaylyInput().GetDaylyInput(2).content.decode('utf-8').splitlines()

policy1 = 0
policy2 = 0
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
        policy1 += 1

    indices = Helper().findInString(password, letter)
    if ((indices.__contains__(min)) != (indices.__contains__(max))):
        policy2 += 1

print(f'Part 1: {policy1}, Part 2: {policy2}')