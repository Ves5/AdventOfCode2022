temp = []
# turn state into down-up matrix
with open('day5/initial-state.txt') as f:
    state = [x.strip('\n') for x in f.readlines()]
    for i in range(len(state)-1, -1, -1):
        tmp = []      
        for j in range(1, len(state[i]), 4):
            tmp.append(state[i][j])
        temp.append(tmp)
# turn it into stack
stacks = [[] for x in range(len(temp[0]))]
for i in range(len(temp)):
    for j in range(len(temp[i])):
        if temp[i][j] != ' ':
            stacks[j].append(temp[i][j])
moves = []
with open('day5/moves.txt') as f:
    tmp = [x.strip().split(' ') for x in f.readlines()]
    for move in tmp:
        moves.append([move[x] for x in range(1, len(move), 2)])
for move in moves:
    # part1
    # for x in range(int(move[0])):
    #     tmp = stacks[int(move[1])-1].pop()
    #     stacks[int(move[2])-1].append(tmp)
    # part2
    # print(stacks[int(move[1])-1])
    # print(stacks[int(move[2])-1])
    tmp = stacks[int(move[1])-1][-int(move[0]):]
    # print(tmp)
    stacks[int(move[1])-1] = stacks[int(move[1])-1][:-int(move[0])]
    # print(stacks[int(move[1])-1])
    stacks[int(move[2])-1] += tmp
    # print(stacks[int(move[2])-1])
    
tmp = ''
for stack in stacks:
    tmp += stack.pop()
print(tmp)