from passwords import DaylyInput



def hash_key(height, width):
    return hash((height, width))    

def get_trees(tright, tdown):
    map = DaylyInput().GetDaylyInput(3).content.decode('utf-8').splitlines()
    mapWidth = len(map[0])
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
    trees = 0
    down = tdown
    right = tright
    while(down < height):
        if map_hash[hash_key(down, right%mapWidth)]:
            trees += 1
        right += tright
        down += tdown
    return trees

# var1 = get_trees(1, 1)
# var2 = get_trees(3, 1)
# var3 = get_trees(5, 1) * get_trees(7, 1) * get_trees(1, 2)

print(get_trees(1, 1) * get_trees(3, 1) * get_trees(5, 1) * get_trees(7, 1) * get_trees(1, 2))

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.