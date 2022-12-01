elfs = []

with open("elfs.txt") as f:
    ls = f.readlines()
    
    new_ls = [x.strip('\n') for x in ls]
    #print(new_ls)
    
    calories = 0 
    for l in new_ls:
        if l != '':
            calories += int(l)
        else:
            elfs.append(calories)
            calories = 0
    elfs.append(calories)
    print(elfs)
    
    print(f"max: {max(elfs)} in place {elfs.index(max(elfs))}")
    elfs.sort()
    elfs.reverse()
    print(f"top 3 sum: {sum(elfs[0:3])}")
#print(l)