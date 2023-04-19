# 1
while True:
    try:
        input_int = int(input("Write an integer: "))
        print(input_int)
        break
    except ValueError:
        print("Try again")


# 2
word = str(input("Enter a word: "))
while True:
    try:
        n = int(input("Enter an integer: "))
        if n < 1:
            print("Integer is to small")
        elif n > len(word):
            print("Integer is to big")
        else:
            print(word[n - 1])
            break
    except ValueError:
        print("n is not an integer")
