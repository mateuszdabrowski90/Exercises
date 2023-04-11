# 1
num = float(input("Enter a number: "))
numr = round(num, 2)
print(str(num) + "rounded to 2 decimal places is " + str(numr))

# 2
num2 = (input("Enter a number: "))
print("The absolute value of " + str(num2) + " is " + str(abs(float(num2))))

# 3
num10 = input("Enter a number ")
num20 = input("Enter another number: ")
dif = float(num10) - float(num20)
is_integer = dif.is_integer()
print("The difference between " + str(num10) + " and " + str(num20) + " is an integer? " + str(is_integer))