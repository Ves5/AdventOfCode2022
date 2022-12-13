from functools import cmp_to_key
import json

def check_order(p1, p2) -> int:
    for left, right in zip(p1, p2):
        # both items are integers
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
            continue
        # both items are lists - go deeper
        elif isinstance(left, list) and isinstance(right, list):
            tmp = check_order(left,right)
            if tmp == 0:
                continue
            return tmp
        # left is not a list - go deeper after [left]
        elif isinstance(left, int) and isinstance(right, list):
            tmp = check_order([left],right)
            if tmp == 0:
                continue
            return tmp
        # right is not a list - go deeper after [right]
        elif isinstance(left, list) and isinstance(right, int):
            tmp = check_order(left,[right])
            if tmp == 0:
                continue
            return tmp
    # left side runs out faster - correct order
    if len(p1) < len(p2):
        return 1
    # right side runs out faster - incorrect order
    elif len(p1) > len(p2):
         return -1
    return 0

values = []
pairs = []
with open('day13/lists.txt') as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]
    for i in range(0, len(lines), 2):
        p1 = json.loads(lines[i])
        p2 = json.loads(lines[i+1])
        pairs.append([p1, p2])
    #print(pairs)

# part 1
for i in range(len(pairs)):
    if check_order(pairs[i][0], pairs[i][1]) >= 0:
        values += [i + 1]

print(sum(values))

# part2
packets = []
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

packets.append([[2]])        
packets.append([[6]])        

packets_sorted = sorted(packets, key=cmp_to_key(check_order), reverse=True)
print((packets_sorted.index([[2]]) + 1) * (packets_sorted.index([[6]]) + 1) )