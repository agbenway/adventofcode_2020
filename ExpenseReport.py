from passwords import DaylyInput

entries = DaylyInput().GetDaylyInput(1).content.decode('utf-8').splitlines()

answer1 = 0
answer2 = 0
while answer1 == 0:
    for i in entries:
        for j in entries:
            if i != j and int(i) + int(j) == 2020:
                answer1 = int(i) * int(j)

while answer2 == 0:
    for i in entries:
        for j in entries:
            if i != j:
                for h in entries:
                    if h != j and int(i) + int(j) + int(h) == 2020:
                        answer2 = int(i) * int(j) * int(h)

print(f'Part 1 = {str(answer1)}')
print(f'Part 2 = {str(answer2)}')

