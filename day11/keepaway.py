from typing import List
import math

class Monkey:
    def __init__(self, items: List[int], operand: str, inc: str, test: int, outcome: List[int]) -> None:
        self.items = items
        self.operand = operand
        self.inc = inc
        self.test = test
        self.outcome = outcome
        self.inspected = 0
        
    def operation(self, old: int) -> int:
        self.inspected += 1
        res = 0
        if self.operand == '*':
            res = old * (int(self.inc) if self.inc != 'old' else old)
        else:
            res = old + (int(self.inc) if self.inc != 'old' else old)
        return res #part2 // 3

monkeys: List[Monkey] = []
with open('day11/monkeys.txt') as f:
    lines = [x.strip().split(' ') for x in f.readlines() if x.strip()]
    for monkey in range(0, len(lines), 6):
        vals = [int(lines[monkey+1][x].strip(',')) for x in range(2, len(lines[monkey+1]))]
        oper = lines[monkey+2][-2]
        incr = lines[monkey+2][-1]
        divis = int(lines[monkey+3][-1])
        throw = [int(lines[monkey+4][-1]), int(lines[monkey+5][-1])]
        monkeys.append(Monkey(vals, oper, incr, divis, throw))
turns = 10000
# part2
lcm = math.lcm(*[monkey.test for monkey in monkeys])
for i in range(turns):
    for monkey in monkeys:
        for j in range(len(monkey.items)):
            new = monkey.operation(monkey.items.pop(0)) % lcm
            if new % monkey.test == 0:
                monkeys[monkey.outcome[0]].items.append(new)
            else:
                monkeys[monkey.outcome[1]].items.append(new)
inspections = [monkey.inspected for monkey in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])
         
        