def add_rock(area, rock_coords, minx):
    for i in range(1, len(rock_coords)):
        xdiff = rock_coords[i][0] - rock_coords[i-1][0]
        if xdiff > 0:
            for j in range(rock_coords[i-1][0] - minx, rock_coords[i][0] - minx + 1):
                area[rock_coords[i][1]][j] = '#'
        elif xdiff < 0:
            for j in range(rock_coords[i][0] - minx, rock_coords[i-1][0] - minx + 1):
                area[rock_coords[i][1]][j] = '#'
        ydiff = rock_coords[i][1] - rock_coords[i-1][1]
        if ydiff > 0:
            for j in range(rock_coords[i-1][1], rock_coords[i][1] + 1):
                area[j][rock_coords[i][0] - minx] = '#'
        elif ydiff < 0:
            for j in range(rock_coords[i][1], rock_coords[i-1][1] + 1):
                area[j][rock_coords[i][0] - minx] = '#'


def sand_move(area, coords):
    try:
        # move one down
        if area[coords[1] + 1][coords[0]] == '.':
            return [0, 1]
        # move one down to the left
        if area[coords[1] + 1][coords[0] - 1] == '.':
            return [-1, 1]
        # move one down to the right
        if area[coords[1] + 1][coords[0] + 1] == '.':
            return [1, 1]
    except IndexError:
        return [0, -1]
    # sand stopped
    return [0, 0]

area = None
rocks_coords = None
minmaxx = None
minmaxy = None
diff = None
with open('day14/rocks.txt') as f:
    rocks = [x.strip().split(' -> ') for x in f.readlines()]
    rocks_coords = [[[int(x.split(',')[0]), int(x.split(',')[1])] for x in rock] for rock in rocks]
    x = []
    y = []
    for rock in rocks_coords:
        for coord in rock:
            x.append(coord[0])
            y.append(coord[1])
    minx = min(x)
    maxx = max(x)
    miny = 0
    maxy = max(y)
    #print(f"x {minx}-{maxx}\ny {miny}-{maxy}")
    diff = maxx - minx
    #print(f"diff {diff}")
    area = []
    for i in range(maxy + 1):
        line = []
        for j in range(diff + 1):
            line.append('.')
        area.append(line)

    minmaxx = [minx, maxx]
    minmaxy = [miny, maxy]    

for rock in rocks_coords:
    add_rock(area, rock, minmaxx[0])
area[0][500-minx] = '+'

counter = 0
run = True
while run:
    sand_coords = [500 - minx, 0]
    counter += 1
    while move := sand_move(area, sand_coords):
        # if sand goes out of area - stop simulation
        if move[1] == -1:
            run = False
            break
        
        if move[1] == 0:
            area[sand_coords[1] + move[1]][sand_coords[0] + move[0]] = 'o'
            break
        
        sand_coords[0] += move[0]
        sand_coords[1] += move[1]
  
for r in area:
    print(''.join(r))

print(counter - 1)
