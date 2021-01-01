import random

members = ["강수현","김지우","남윤종","배재현","송민경","안리아","이승준","장지환"]
pairs = {}

for p in range(len(members) // 2):
    pairs[p+1] = ( members.pop(random.randrange(len(members))),
        members.pop(random.randrange(len(members))) )

print(pairs)