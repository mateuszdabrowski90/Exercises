import random

flip = 0
position_s = random.randint(1, 2)
for i in range(10000):
    position_n = random.randint(1, 2)
    if position_n == position_s:
        continue
    else:
        flip = flip + 1
        position_n = position_s
print(flip +1)