from DailyInput import DailyInput

def hash_key(height, width):
    return hash((height, width))    

def get_map():
    map = DailyInput(3).get_input_split_lines()
    map_hash = {}
    height = 0
    for row in map:
        width = 0
        for char in row:
            key = hash((height, width))
            value = (char == '#')
            map_hash[key] = value
            width += 1
        height += 1
    return [map_hash, height , len(map[0])]

def get_trees(tright, tdown):
    result = get_map()
    map_hash = result[0]
    height = result[1]
    mapWidth = result[2]
    trees = 0
    down = tdown
    right = tright
    while(down < height):
        if map_hash[hash_key(down, right%mapWidth)]:
            trees += 1
        right += tright
        down += tdown
    return trees

part1 = get_trees(3, 1)
print(f'Part 1: {part1}') # 270 
print(f'Part 2: {get_trees(1, 1) * part1 * get_trees(5, 1) * get_trees(7, 1) * get_trees(1, 2)}') # 2122848000