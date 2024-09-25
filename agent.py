# Create the connect 4 agent class with minimax and alpha-beta pruning
import numpy as np
from board import Board


class Agent:
    def __init__(self, depth=3):
        self.depth = depth
        self.player = 1
        self.opponent = 2

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.winner is not None:
            return self.heuristic(board), None

        if maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in board.get_valid_moves():
                board_copy = self.copy_board(board)
                board_copy.make_move(move)
                eval, _ = self.minimax(board_copy, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.get_valid_moves():
                board_copy = self.copy_board(board)
                board_copy.make_move(move)
                eval, _ = self.minimax(board_copy, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def copy_board(self, board):
        board_copy = Board()
        board_copy.board = np.copy(board.board)
        board_copy.turn = board.turn
        board_copy.winner = board.winner
        board_copy.moves = board.moves
        return board_copy

    def heuristic(self, board):
        # Check if we have four in a row
        score = 0

        # Check if middle bottom slot is open (Optimal first/second move)
        if board.board[3][0] == 0:
            score += 50
        for i in range(6):
            for j in range(4):
                # Check four in row to right
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == board.board[i][j + 3] == self.player:
                    score += 1000
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == board.board[i][j + 3] == self.opponent:
                    score -= 1000
                if i < 3:
                    # Check four in a row up
                    if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == board.board[i + 3][j] == self.player:
                        score += 1000
                    if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == board.board[i + 3][j] == self.opponent:
                        score -= 1000
                    # Check four in a row up diagonal right
                    if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == board.board[i + 3][j + 3] == self.player:
                        score += 1000
                    if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == board.board[i + 3][j + 3] == self.opponent:
                        score -= 1000
                if i <3 and j > 2:
                    # Check four in a row down diagonal right
                    if board.board[i][j] == board.board[i + 1][j - 1] == board.board[i + 2][j - 2] == board.board[i + 3][j - 3] == self.player:
                        score += 1000
                    if board.board[i][j] == board.board[i + 1][j - 1] == board.board[i + 2][j - 2] == board.board[i + 3][j - 3] == self.opponent:
                        score -= 1000
                if i > 2 and j < 4:
                    # Check four in a row up diagonal left
                    if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == board.board[i - 3][j + 3] == self.player:
                        score += 1000
                    if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == board.board[i - 3][j + 3] == self.opponent:
                        score -= 1000
                if i > 2 and j > 2:
                    # Check four in a row down diagonal left
                    if board.board[i][j] == board.board[i - 1][j - 1] == board.board[i - 2][j - 2] == board.board[i - 3][j - 3] == self.player:
                        score += 1000
                    if board.board[i][j] == board.board[i - 1][j - 1] == board.board[i - 2][j - 2] == board.board[i - 3][j - 3] == self.opponent:
                        score -= 1000



        # Check if we have three in a row
        for i in range(6):
            for j in range(4):
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == self.player:
                    score += 10
                if board.board[i][j] == board.board[i][j + 1] == board.board[i][j + 2] == self.opponent:
                    score -= 10
                if i < 3:
                    if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == self.player:
                        score += 10
                    if board.board[i][j] == board.board[i + 1][j] == board.board[i + 2][j] == self.opponent:
                        score -= 10
                    if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == self.player:
                        score += 10
                    if board.board[i][j] == board.board[i + 1][j + 1] == board.board[i + 2][j + 2] == self.opponent:
                        score -= 10
                if i > 2:
                    if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == self.player:
                        score += 10
                    if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == self.opponent:
                        score -= 10
                if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == self.player:
                    score += 10
                if board.board[i][j] == board.board[i - 1][j + 1] == board.board[i - 2][j + 2] == self.opponent:
                    score -= 10
                    # Check if we can trap the opponent
        for i in range(6):
            for j in range(7):
                if board.board[i][j] == 0:
                    if i == 5 or board.board[i + 1][j] != 0:
                        if j > 0 and j < 6:
                            if board.board[i][j - 1] == self.opponent and board.board[i][j + 1] == self.opponent:
                                score -= 10
                        if j > 1:
                            if board.board[i][j - 1] == self.opponent and board.board[i][j - 2] == self.opponent:
                                score -= 10
                        if j < 5:
                            if board.board[i][j + 1] == self.opponent and board.board[i][j + 2] == self.opponent:
                                score -= 10
                        if j > 0 and j < 6 and i < 5:
                            if board.board[i + 1][j - 1] == self.opponent and board.board[i + 1][j + 1] == self.opponent:
                                score -= 10
                        if j > 1 and i < 5:
                            if board.board[i + 1][j - 1] == self.opponent and board.board[i + 1][j - 2] == self.opponent:
                                score -= 10
                        if j < 5 and i < 5:
                            if board.board[i + 1][j + 1] == self.opponent and board.board[i + 1][j + 2] == self.opponent:
                                score -= 10
        return score


    def get_move(self, board):
        _, move = self.minimax(board, self.depth, float('-inf'), float('inf'), True)
        return move

    def make_move(self, board):
        move = self.get_move(board)
        board.make_move(move)
        return move

    def set_player(self, player):
        self.player = player
        self.opponent = 1 if player == 2 else 2

    def set_depth(self, depth):
        self.depth = depth