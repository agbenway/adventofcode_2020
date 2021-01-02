from DailyInput import DailyInput

entries = DailyInput(6).get_input_split_and_replace_lines_with_sapces()
total_yes = 0
for form in entries:
    yes_answers = []
    for q in form:
        if q != ' ' and not yes_answers.__contains__(q):
            yes_answers.append(q)
    total_yes += len(yes_answers)

total_all_yes = 0
for forms in entries:
    sets_of_ind = [set(ind) for ind in forms.strip().split(" ")] # Last line ends in a space
    all_answers = sets_of_ind[0].intersection(*sets_of_ind)
    total_all_yes += len(all_answers)

print(f'Part 1: {total_yes}') # 6416
print(f'Part 2: {total_all_yes}') # 3050

