import random

board = {
    'A1': ' ',
    'A2': ' ',
    'A3': ' ',
    'B1': ' ',
    'B2': ' ',
    'B3': ' ',
    'C1': ' ',
    'C2': ' ',
    'C3': ' ',
}
chosen = []
sign_h = 'O'
sign_c = 'X'

def write():
    while True:
        print(f'    [1]  [2]  [3]')
        print(f'[A] [{board["A1"]}]  [{board["A2"]}]  [{board["A3"]}]')
        print(f'[B] [{board["B1"]}]  [{board["B2"]}]  [{board["B3"]}]')
        print(f'[C] [{board["C1"]}]  [{board["C2"]}]  [{board["C3"]}]')
        choice_h = input("Enter a coordinate: ").upper()
        if choice_h in chosen:
            while choice_h in chosen:
                print("wrong value. Enter again")
                choice_h = input("Enter a coordinate: ").upper()
            board[choice_h] = sign_h
        else: board[choice_h] = sign_h
        chosen.append(choice_h)
        if board["A1"] == sign_h and board["A2"] == sign_h and board["A3"] == sign_h:
            print("You won!")
            break
        elif board["B1"] == sign_h and board["B2"] == sign_h and board["B3"] == sign_h:
            print("You won!")
            break
        elif board["C1"] == sign_h and board["C2"] == sign_h and board["C3"] == sign_h:
            print("You won!")
            break
        elif board["A1"] == sign_h and board["B1"] == sign_h and board["C1"] == sign_h:
            print("You won!")
            break
        elif board["A2"] == sign_h and board["B2"] == sign_h and board["C2"] == sign_h:
            print("You won!")
            break
        elif board["A3"] == sign_h and board["B3"] == sign_h and board["C3"] == sign_h:
            print("You won!")
            break
        elif board["A1"] == sign_h and board["B2"] == sign_h and board["C3"] == sign_h:
            print("You won!")
            break
        elif board["A3"] == sign_h and board["B2"] == sign_h and board["C1"] == sign_h:
            print("You won!")
            break
        choice_c = random.choice(list(board))
        if choice_c in chosen:
            while choice_c in chosen:
                choice_c = random.choice(list(board))
        board[choice_c] = sign_c
        chosen.append(choice_c)
        if board["A1"] == sign_c and board["A2"] == sign_c and board["A3"] == sign_c:
            print("You lost!")
            break
        elif board["B1"] == sign_c and board["B2"] == sign_c and board["B3"] == sign_c:
            print("You lost!")
            break
        elif board["C1"] == sign_c and board["C2"] == sign_c and board["C3"] == sign_c:
            print("You lost!")
            break
        elif board["A1"] == sign_c and board["B1"] == sign_c and board["C1"] == sign_c:
            print("You lost!")
            break
        elif board["A2"] == sign_c and board["B2"] == sign_c and board["C2"] == sign_c:
            print("You lost!")
            break
        elif board["A3"] == sign_c and board["B3"] == sign_c and board["C3"] == sign_c:
            print("You lost!")
            break
        elif board["A1"] == sign_c and board["B2"] == sign_c and board["C3"] == sign_c:
            print("You lost!")
            break
        elif board["A3"] == sign_c and board["B2"] == sign_c and board["C1"] == sign_c:
            print("You lost!")
            break
write()
print(f'    [1]  [2]  [3]')
print(f'[A] [{board["A1"]}]  [{board["A2"]}]  [{board["A3"]}]')
print(f'[B] [{board["B1"]}]  [{board["B2"]}]  [{board["B3"]}]')
print(f'[C] [{board["C1"]}]  [{board["C2"]}]  [{board["C3"]}]')