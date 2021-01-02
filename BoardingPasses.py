from DailyInput import DailyInput

class BoardingPass(object):
    def __init__(self, row, seat, bpass):
        self.row = row
        self.seat = seat
        self.bpass = bpass

input = DailyInput(5).get_input_split_lines()

passes = {}

for bpass in input:
    totalRows = 128
    totalSeats = 8
    upperRow = totalRows
    upperSeat = totalSeats
    row = 0
    seat = 0
    count = 0
    for sec in bpass:
        if (sec == 'F'):
            upperRow = row + ((upperRow-row)/2)
        elif (sec == 'B'):
            row = upperRow - ((upperRow-row)/2)
            upperRow = upperRow
        elif (sec == 'L'):
            upperSeat = seat + ((upperSeat-seat)/2)
        elif (sec == 'R'):
            seat = upperSeat - ((upperSeat-seat)/2)
            upperSeat = upperSeat

        if count == 9:
            seatId = (row * 8) + seat
            bp = BoardingPass(row, seat, bpass)
            passes[seatId] = bp
        count += 1

keys = passes.keys()
print(f'Max: {max(keys)}')

sorted = list(keys)
sorted.sort()
numBefore = sorted[0] - 1
for num in sorted:
    if (num-1 != numBefore):
        print(f'Num: {num} and NumBefore: {numBefore}')
        print(f'Is this your number? {num -1}') 
        break
    else:
        numBefore += 1  

print(f'Part 1: {max(keys)}') # 892
print(f'Part 2: {num-1}') # 625


