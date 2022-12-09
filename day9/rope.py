def adjacent(tail, head):
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return True
    return False

def vector_add(v1, v2):
    res = [0 for x in range(len(v1))]
    for i in range(len(v1)):
        res[i] += v1[i] + v2[i]
    return res

def get_movevector(k1, k2):
    return [-1 if (k1[0] - k2[0]) < 0 else (0 if (k1[0] - k2[0]) == 0 else 1),
            -1 if (k1[1] - k2[1]) < 0 else (0 if (k1[1] - k2[1]) == 0 else 1)]

move = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
visited = set([(0,0)]) #starting point
with open('day9/steps.txt') as f:
    steps = [x.strip().split(' ') for x in f.readlines()]
    end = 10
    rope = [[0,0] for x in range(end)]
    for s in steps:
        for t in range(int(s[1])):
            rope[0] = vector_add(rope[0], move[s[0]])
            for i in range(1, len(rope)):
                if not adjacent(rope[i-1], rope[i]):
                    movevector = get_movevector(rope[i-1], rope[i])
                    rope[i] = vector_add(rope[i], movevector)
                    if i == end-1:
                        visited.add((rope[end-1][0], rope[end-1][1]))
print(len(visited))