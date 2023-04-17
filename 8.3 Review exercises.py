word = input("Enter your word: ")
if 5 < len(word):
    print(f"{word} is more than 5 characters")
elif 5 > len(word):
    print(f"{word} is less than 5 characters")
else:
    print(f"{word} is 5 characters")
