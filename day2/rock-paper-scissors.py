# Rock (x) = 1; Paper (y) = 2; Scissors (z) = 3
# Win = 6; Draw = 3; Loss = 0
# rock < paper < scissors < rock

#part 2
# x = loss; y = draw; z = win

#points = {'X': 1, 'Y': 2, 'Z': 3}
matches = {'A': {'X': 0+3, 'Y': 3+1, 'Z': 6+2}, 'B': {'X': 0+1, 'Y': 3+2, 'Z': 6+3}, 'C': {'X': 0+2, 'Y': 3+3, 'Z': 6+1}}
result = 0

with open("day2/moves.txt") as f:
    moves = f.readlines()
    moves = [x.strip().split(' ') for x in moves]
    #print(moves)
    for pair in moves:
        #result += points[pair[1]]
        result += matches[pair[0]][pair[1]]
        # loss without anything

print(result)