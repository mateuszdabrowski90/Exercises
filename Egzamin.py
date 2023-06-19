import random

board = {
    'A1': '',
    'A2': '',
    'A3': '',
    'B1': '',
    'B2': '',
    'B3': '',
    'C1': '',
    'C2': '',
    'C3': '',
}
chosen = []
sign_h = 'O'
sign_c = 'X'
def write():
    while True:
        print(f'[{board["A1"]}] [{board["A2"]}] [{board["A3"]}]')
        print(f'[{board["B1"]}] [{board["B2"]}] [{board["B3"]}]')
        print(f'[{board["C1"]}] [{board["C2"]}] [{board["C3"]}]')
        choose_h = input("Write a coordinate: ").upper()
        board[choose_h] = sign_h
        choose_c = random.choice(list(board))
        while choose_c in chosen:
            choose_c = random.choice(list(board))
        board[choose_c] = sign_c
        print(board)
        if A1 == sign_h and A2 == sign_h and A3 == sign_h or B1 == sign_h and B2 == sign_h and B3 == sign_h or C1 == sign_h and C2 == sign_h and C3 == sign_h:
            print("You won")

write()
