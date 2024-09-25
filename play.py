# Play connect 4 with the agent

from board import Board
from agent import Agent
import numpy as np
import time
def play():
    board = Board()
    agent = Agent(depth=5)
    while board.winner is None:
        print(board.board)
        if board.turn == agent.player:
            move = agent.minimax(board, agent.depth, float('-inf'), float('inf'), True)[1]
            board.make_move(move)
        else:
            move = int(input('Enter a move: '))
            if move not in board.get_valid_moves():
                print('Invalid move')
                continue
            board.make_move(move)
    print(board.board)
    if board.winner == 0:
        print('It\'s a tie!')
    else:
        print(f'Player {board.winner} wins!')

def self_play():
    board = Board()
    agent = Agent(depth=5)
    agent2 = Agent(depth=4)
    while board.winner is None:
        print(board.board)
        if board.turn == agent.player:
            move = agent.minimax(board, agent.depth, float('-inf'), float('inf'), True)[1]
            board.make_move(move)
        else:
            move = agent2.minimax(board, agent2.depth, float('-inf'), float('inf'), False)[1]
            board.make_move(move)
    print(board.board)
    if board.winner == 0:
        print('It\'s a tie!')
    else:
        print(f'Player {board.winner} wins!')

def random_play():
    board = Board()
    agent = Agent()
    while board.winner is None:
        print(board.board)
        if board.turn == agent.player:
            move = agent.minimax(board, agent.depth, float('-inf'), float('inf'), True)[1]
            board.make_move(move)
        else:
            move = np.random.choice(board.get_valid_moves())
            board.make_move(move)
    print(board.board)
    if board.winner == 0:
        print('It\'s a tie!')
    else:
        print(f'Player {board.winner} wins!')

play()