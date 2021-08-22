import random


nubmers = []

while len(nubmers) < 6:
    x = random.randint(1,10)
    nubmers.append(x)

set_nubmers = set(nubmers)

while len(nubmers) != len(set_nubmers):
    y = random.randint(1,10)

    set_nubmers = list(set_nubmers)

    if y in set_nubmers:
        pass
    else:
        set_nubmers.append(y)

print(set_nubmers)