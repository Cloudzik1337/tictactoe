from colorama import init, Fore, Back, Style
from random import randint
from time import sleep
from cloud import *
init(autoreset=True, convert=True)
Cloud.banner('TicTacToe', 'Cloud', '1.0', 'cloudzik.cc', 'github.com/Cloudzik1337', '2023')
Cloud.exit_timer = 2
Cloud.exit_handler()
Cloud.hide_cursor()
class chess:
    pass
chess.enemy = Fore.RED +        '| X |'
chess.player = Fore.GREEN +     '| O |'
chess.empty = Fore.WHITE +      '|   |'

chess.board = [
    [chess.empty, chess.empty, chess.empty],
    [chess.empty, chess.empty, chess.empty],
    [chess.empty, chess.empty, chess.empty]
]
chess.turn = 0
chess.winner = None
chess.gameover = False
chess.player_turn = True
chess.enemy_turn = False
chess.player_win = False
chess.enemy_win = False

class Game:
    def __init__(self):
        self.board = chess.board
        self.turn = chess.turn
        self.winner = chess.winner 
        self.gameover = chess.gameover
        self.player_turn = chess.player_turn
        self.enemy_turn = chess.enemy_turn
        self.player_win = chess.player_win
        self.enemy_win = chess.enemy_win
        self.player = chess.player
        self.enemy = chess.enemy

    def print_board(self):
        i = 0
        print('   0     1    2 ')
        for row in self.board:
            print(i, end=' ')
            i += 1
            for col in row:
                print(col, end='')
            print()
    
    def player_move(self, x, y):
        if self.board[x][y] == chess.empty:
            self.board[x][y] = self.player
            self.player_turn = False
            self.enemy_turn = True
        else:
            print('You can\'t move there')
            sleep(1)
    
    def ai_move(self, x, y):
        while True:
            if self.board[x][y] == chess.empty:
                self.board[x][y] = self.enemy
                self.player_turn = True
                self.enemy_turn = False
                break
            else:
                x = randint(0, 2)
                y = randint(0, 2)
                continue
        
    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] == self.player:
                self.player_win = True
                self.gameover = True
            elif row[0] == row[1] == row[2] == self.enemy:
                self.enemy_win = True
                self.gameover = True
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.player:
                self.player_win = True
                self.gameover = True
            elif self.board[0][col] == self.board[1][col] == self.board[2][col] == self.enemy:
                self.enemy_win = True
                self.gameover = True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player:
            self.player_win = True
            self.gameover = True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.enemy:
            self.enemy_win = True
            self.gameover = True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player:
            self.player_win = True
            self.gameover = True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.enemy:
            self.enemy_win = True
            self.gameover = True
        # Check if board is full
        if self.turn == 9:
            self.gameover = True
            

    def run(self):
        
        while not self.gameover:
            
            self.check_win()
            self.print_board()
            if self.player_turn:
                x = int(input('x: '))
                y = int(input('y: '))
                self.player_move(x, y)
                self.print_board()
            elif self.enemy_turn:
                x = randint(0, 2)
                y = randint(0, 2)
                self.ai_move(x, y)
                self.print_board()
            self.turn += 1
            Cloud.cls()
        self.print_board()
        if self.player_win:
            print(Fore.GREEN+'You win!')
        elif self.enemy_win:
            print(Fore.RED+'You lose!')
        else:
            print(Fore.YELLOW+'Draw!')

Game = Game()
Game.run()
