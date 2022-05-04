import random
from typing import Sized
# set important variables to default values
letter_input = ''
position_input = 0
do_end = 'No'
not_here = []
letters = ('X', 'O')
turn = 'Player'
# this class will be a tictactoe board
class Board:
    # initialization function
    def __init__(self, char):
        self.char = char

        self.board = [char for i in range(0, 10)]
    
    def printBoard(self):
        print(f'\
 {self.board[7]} | {self.board[8]} | {self.board[9]}\n\
---+---+---\n\
 {self.board[4]} | {self.board[5]} | {self.board[6]}\n\
---+---+---\n\
 {self.board[1]} | {self.board[2]} | {self.board[3]}\n'
        )
# create new board
board = Board(' ')
# choose opposite letter for opponent
def opponents_letter():
    if letter_input == 'X':
        return 'O'
    elif letter_input == 'O':
        return 'X'

def do_computer_turn():
    global not_here
    print(not_here)

    free = []
    place_here = None

    for i in range(1, 10):
        if not i in not_here:
            free.append(i)

    print(free)

    place_here = free[random.randint(1, len(free)-1)]
    board.board[place_here] = opponents_letter()

    not_here.append(place_here)

    return place_here
# check if someone won
def check_board():
    if not board.char in board.board: print('Tie!'); return 2

    won_player = [letter_input for i in range(0, 3)]
    won_computer = [opponents_letter() for i in range(0, 3)]

    if board.board[1:4] == won_player or board.board[4:7] == won_player or board.board[7:10] == won_player: print('Player won'); return 1
    elif board.board[1:4] == won_computer or board.board[4:7] == won_computer or board.board[7:10] == won_computer: print('Computer won'); return 1

    if board.board[7] == board.board[4] == board.board[1] != board.char:
        print(f'{turn} won')
        return 1

    if board.board[8] == board.board[5] == board.board[2] != board.char:
        print(f'{turn} won')
        return 1

    if board.board[9] == board.board[6] == board.board[3] != board.char:
        print(f'{turn} won')
        return 1

    if board.board[7] == board.board[5] == board.board[3] != board.char:
        print(f'{turn} won')
        return 1

    if board.board[9] == board.board[5] == board.board[1] != board.char:
        print(f'{turn} won')
        return 1



def when_not_end():
    global letter_input
    global turn
    global do_end
    letter_input = input('X or O? > ')

    if letter_input in letters:
        while True:
            while True:
                try:
                    turn = 'Player'
                    position_input = int(input('Your turn (1 - 9)> '))
                except:
                    print('Please, enter a number value')
                finally:
                    break

            if position_input < 1 or position_input > 9:
                print('Invalid input')
            else:
                if board.board[position_input] == board.char:
                    board.board[position_input] = letter_input
                    not_here.append(position_input)
                    
                    if check_board() in (1, 2): do_end = input('Do you want to quit (Yes or No)? >'); break

                    turn = 'Computer'
                    print(f'Computer turn: {do_computer_turn()}')
                    board.printBoard()

                    if check_board() in (1, 2): do_end = input('Do you want to quit (Yes or No)? >'); break

                board.printBoard()

def main():
    while True:
        if do_end == 'No':
            board.__init__(board.char)
            when_not_end()

        else:
            print('Goodbye')
            break
# don't run when used as module
if __name__ == '__main__':
    main()
