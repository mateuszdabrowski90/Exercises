password = input("Tell me your password: ")
first_letter = password[1].upper()
right_password = first_letter + password[1:]
print(right_password)