"""
8-Puzzle Base Module
For DFS and A* Search
"""

import random
from termcolor import colored

class PuzzleState:
    """8-puzzle 状态类"""
    
    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = board  # The puzzle board configuration
        self.parent = parent  # Parent state
        self.move = move  # Move to reach this state
        self.depth = depth  # Depth in the search tree
        self.cost = cost  # Cost (depth + heuristic)
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    # Function to display the board in a visually appealing format
def print_board(board):
    print("+---+---+---+")
    for row in range(0, 9, 3):
        row_visual = "|"
        for tile in board[row:row + 3]:
            if tile == 0:  # Blank tile
                row_visual += f" {colored(' ', 'cyan')} |"
            else:
                row_visual += f" {colored(str(tile), 'yellow')} |"
        print(row_visual)
        print("+---+---+---+")


moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}


def is_valid_move(move, blank_pos):
    if move == 'U' and blank_pos < 3:
        return False
    if move == 'D' and blank_pos > 5:
        return False
    if move == 'L' and blank_pos % 3 == 0:
        return False
    if move == 'R' and blank_pos % 3 == 2:
        return False
    return True


def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]
    new_board[blank_pos], new_board[new_blank_pos] = \
        new_board[new_blank_pos], new_board[blank_pos]
    return new_board

def heuristic(board, goal):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(board[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_path(goal_state):
    path = []
    current = goal_state
    while current:
        path.append(current)
        current = current.parent
    path.reverse()
    return path


def print_solution(solution):
    path = get_path(solution)
    print(f"\nSolution found! Steps: {len(path) - 1}\n")
    for i, state in enumerate(path):
        if state.move:
            print(f"Step {i}: Move {state.move}")
        else:
            print("Step 0: Initial State")
        print_board(state.board)

def count_inversions(board):
    nums = [x for x in board if x != 0]
    inv = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv


def is_solvable(start, goal):
    return count_inversions(start) % 2 == count_inversions(goal) % 2


def generate_solvable_pair(seed):
    random.seed(seed)

    start = list(range(9))
    goal = list(range(9))

    random.shuffle(start)
    random.shuffle(goal)

    while not is_solvable(start, goal):
        random.shuffle(goal)

    return start, goal

