duration = {"addx": 2, "noop": 1} # duration of 
cycle = 0 # current cycle
milestone = 40 # +40 #par1 = 20; part2 = 40
x = 1 # register X
value = 0 # part1 result
line = ''
with open('day10/asm.txt') as f:
    commands = [y.strip().split(' ') for y in f.readlines()]
    for cmd in commands:
        for c in range(duration[cmd[0]]):
            # part2
            if (cycle % 40) >= (x - 1) and (cycle % 40) <= (x + 1):
                line += '#'
            else:
                line += '.'
            cycle += 1
            if cycle == milestone:
                # part1
                # tmp = x * cycle
                # print(f"{tmp} in cycle {cycle}")
                # value += tmp
                milestone += 40
                # part2
                print(line)
                line = ''
        if cmd[0] == "addx":
            x += int(cmd[1])
#print(value)
    