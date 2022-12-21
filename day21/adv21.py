operators = {
    '+': (lambda x, y: x + y), 
    '-': (lambda x, y: x - y), 
    '*': (lambda x, y: x * y), 
    '/': (lambda x, y: x // y),
    '=': (lambda x, y: x == y)}
monkeys = {}
class Monkey:
    def __init__(self, name, role) -> None:
        self.name = name
        if len(role) > 1:
            # combination
            self.oper = role[1]
            self.p1 = role[0]
            self.p2 = role[2]
            self.value = None
        else:
            # value
            self.value = int(role[0])
    
    def getValue(self):
        if self.value is None:
            self.value = operators[self.oper](monkeys[self.p1].getValue(), monkeys[self.p2].getValue())
        return self.value
    
with open('day21/monkeys.txt') as f:
    lines = [x.strip().split(' ') for x in f.readlines()]
    for l in lines:
        l[0] = l[0].strip(':')
        monkeys[l[0]] = Monkey(l[0], l[1:])
        
print(monkeys['root'].getValue())
