import random

# 1
def roll():
    x = random.randint(1, 6)
    return x

roll()

# 2
sum = 0
for i in range(10000):
    j = roll()
    sum = sum + j
average = sum / 10000
print(average)
