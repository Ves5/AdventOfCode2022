import json

def check_order(p1, p2) -> bool:
    for i in range(max(len(p1), len(p2))):
        # left side runs out faster - correct order
        if i >= len(p1):
            return True
        # right side runs out faster - incorrect order
        if i >= len(p2):
            return False
        # both items are lists - go deeper
        if isinstance(p1[i], list) and isinstance(p2[i], list):
            # if it returned false then finish function
            if not check_order(p1[i], p2[i]):
                return False
            continue
        # left is not a list - go deeper after [left]
        if not isinstance(p1[i], list) and isinstance(p2[i], list):
            if not check_order([p1[i]], p2[i]):
                return False
            continue
        # right is not a list - go deeper after [right]
        if isinstance(p1[i], list) and not isinstance(p2[i], list):
            if not check_order(p1[i], [p2[i]]):
                return False
            continue
        # both items are integers
        if p1[i] < p2[i]:
            return True
        elif p1[i] == p2[i]:
            continue
        else:
            return False
    return True

values = []
pairs = []
with open('day13/lists.txt') as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]
    for i in range(0, len(lines), 2):
        p1 = json.loads(lines[i])
        p2 = json.loads(lines[i+1])
        pairs.append([p1, p2])
    #print(pairs)

for i in range(len(pairs)):
    if not check_order(pairs[i][0], pairs[i][1]):
        values += [i + 1]
        
print(sum(values))