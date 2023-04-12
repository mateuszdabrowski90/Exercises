# 1
def convert_cel_to_far(C):
    f = c * 9/5 + 32
    return f

c = float(input("Enter a temperature ic Celsius: "))
fahrenheit = convert_cel_to_far(c)
print(f"{c} degrees C = {fahrenheit:.2f} degrees F")

# 2
def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    return c
f = float(input("Enter a temperature in Fahrenheit: "))
celsius = convert_far_to_cel(f)
print(f"{f} degrees F = {celsius:.2f} degrees C")