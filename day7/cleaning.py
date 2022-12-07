from typing import List, Tuple

class Dir:
    def __init__(self, parent, name):
        self.parent : Dir = parent
        self.name : str = name
        self.dirs : List[Dir] = []
        self.files : List[Tuple[str, int]] = []

def tree(node: Dir, ind: int):
    print((' '*ind) + '+' + f'{node.name}')
    for d in node.dirs:
        tree(d, ind+1)
    for f in node.files:
        print((' '*(ind+1)) + f'- {f[0]} - {f[1]}')

def part1(dir: Dir):
    size = 0
    for f in dir.files:
        size += int(f[1])
    total = 0
    for d in dir.dirs:
        tup = part1(d)
        size += tup[0]
        total += tup[1]
    #print(f"name {dir.name} - size: {size}")
    total += size if size <= 100000 else 0
    return (size, total)

def part2(dir: Dir, needed: int):
    applicable = []
    size = part1(dir)[0]
    if size >= needed:
        applicable.append(size)
    for d in dir.dirs:
        applicable += part2(d, needed)
    return applicable

root = Dir(None, '/')
# traverse history   
with open('day7/browsing.txt') as f:
    history = [x.strip().split() for x in f.readlines()]
    curDir: Dir = root
    for line in history:
        # commands
        if line[0] == '$':
            if line[1] == 'ls':
                continue
            elif line[1] == 'cd':
                # go up
                if line[2] == '..':
                    curDir = curDir.parent if curDir.parent is not None else curDir
                elif line[2] == '/':
                    curDir = root
                # go down
                else:
                    for d in curDir.dirs:
                        if d.name == line[2]:
                            curDir = d
                            break
        # dirs
        elif line[0] == 'dir':
            curDir.dirs.append(Dir(curDir, line[1]))     
        # files
        else:
            curDir.files.append((line[1], line[0]))
            
#tree(root, 0)
used, answer = part1(root)
print(answer)

needed = used - (70000000 - 30000000)
#print(needed)
print(min(part2(root, needed)))