# 1
i = 1
while i > 0:
    n = input("Write something: ")
    if n == "q":
        break
    elif n == "Q":
        break
    i = i +1

# 2
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
