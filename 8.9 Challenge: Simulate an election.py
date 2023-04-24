import random

cand_a = 0
cand_b = 0
def election():
    cand_a = 0
    cand_b = 0
    for i in range(10000):
        x = random.randint(1, 2)
        if x == 1:
            cand_a = cand_a + 1
        else:
            cand_b = cand_b + 1



