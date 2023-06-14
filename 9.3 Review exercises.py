# 1
data = ((1, 2), (3, 4))

# 2
x = 1
for i in data:
    sum = i[0] + i[1]
    print(f"Row {x} sum: {sum}")
    x += 1

# 3
numbers = [4, 3, 2, 1]

# 4
copy_numbers = numbers[:]
print(copy_numbers)

# 5
numbers.sort()
print(numbers)
