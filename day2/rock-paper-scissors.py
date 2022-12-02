# Rock (x) = 1; Paper (y) = 2; Scissors (z) = 3
# Win = 6; Draw = 3; Loss = 0
# rock < paper < scissors < rock

opponent = ['A', 'B', 'C',]
you = ['X', 'Y', 'Z']

points = {'X': 1, 'Y': 2, 'Z': 3}
result = 0

with open("day2/moves.txt") as f:
    moves = f.readlines()
    moves = [x.strip().split(' ') for x in moves]
    #print(moves)
    for pair in moves:
        result += points[pair[1]]
        # draw
        if opponent.index(pair[0]) == you.index(pair[1]):
            result += 3
        elif pair[0]:
            pass
        # loss without anything

print(result)