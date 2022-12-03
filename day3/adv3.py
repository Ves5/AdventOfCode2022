# priorities 

def prio(char):
    if ord(char) >= 97:
        return ord(char) - 96
    return ord(char) - 38

res = 0
res2 = 0
with open("day3/backpacks.txt") as f:
    contents = f.readlines()
    contents = [x.strip() for x in contents]
    splits = [[x[:len(x)//2], x[len(x)//2:]] for x in contents]
    for sp in splits:
        common = set(sp[0]).intersection(sp[1])
        #print(common)
        res += prio(next(iter(common)))
        
    for i in range(0, len(contents), 3):
        common = set(contents[i]).intersection(contents[i+1]).intersection(contents[i+2])
        res2 += prio(next(iter(common)))
        
print(res)
print(res2)