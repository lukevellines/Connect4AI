# Create the connect 4 board class
import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros((6,7))
        self.turn = 1
        self.winner = None
        self.moves = 0


    def reset(self):
        self.board = np.zeros((6,7))
        self.turn = 1
        self.winner = None
        self.moves = 0

    def make_move(self, col):
        if self.winner is not None:
            return False
        if self.board[0][col] != 0:
            return False
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                self.board[i][col] = self.turn
                self.moves += 1
                self.check_winner()
                self.turn = 1 if self.turn == 2 else 2
                return True
        return False

    def check_winner(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == 0:
                    continue
                if j + 3 < 7 and self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                    self.winner = self.board[i][j]
                    return
                if i + 3 < 6:
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                        self.winner = self.board[i][j]
                        return
                    if j + 3 < 7 and self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                        self.winner = self.board[i][j]
                        return
                    if j - 3 >= 0 and self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3]:
                        self.winner = self.board[i][j]
                        return

    def get_valid_moves(self):
        valid_moves = []
        for j in range(7):
            if self.board[0][j] == 0:
                valid_moves.append(j)
        return valid_moves

