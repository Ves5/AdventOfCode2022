contains = 0
overlap = 0
with open("day4/ranges.txt") as f:
    ranges = [x.strip().split(',') for x in f.readlines()]
    for r in ranges:
        r1 = r[0].split('-')
        r2 = r[1].split('-')
        if (int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[1])) or (int(r2[0]) <= int(r1[0]) and int(r2[1]) >= int(r1[1])):
            contains += 1
        if (int(r1[0]) <= int(r2[1]) and int(r2[0]) <= int(r1[1])):
            overlap += 1
print(contains)
print(overlap)