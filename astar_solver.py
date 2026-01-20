"""
A* Search Solver for 8-Puzzle
使用A*搜索算法解决8-puzzle问题
使用曼哈顿距离作为启发函数
"""

import heapq
from base import *

# A* search algorithm
def a_star(start, goal):
    open_list = []
    closed_list = set()
    start_state = PuzzleState(
        start,
        parent=None,
        move=None,
        depth=0,
        cost=heuristic(start, goal)
    )

    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal:
            return current_state

        closed_list.add(tuple(current_state.board))

        blank_pos = current_state.board.index(0)

        for move in moves:
            if not is_valid_move(move, blank_pos):
                continue

            new_board = move_tile(current_state.board, move, blank_pos)

            if tuple(new_board) in closed_list:
                continue
            
            g = current_state.depth + 1
            h = heuristic(new_board, goal)

            new_state = PuzzleState(new_board, current_state, move, g, g+h)
            heapq.heappush(open_list, new_state)

    return None

if __name__ == "__main__":
    # B1: fixed start & goal
    start = [2, 8, 3, 7, 6, 4, 1, 0, 5]
    goal  = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    print("A*: B1 Fixed Start/Goal")
    solution = a_star(start, goal)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")

    # B2: random start & goal
    print("\nA*: B2 Random Start/Goal")
    start, goal = generate_solvable_pair(225040099)

    print("Start:", start)
    print("Goal :", goal)

    solution = a_star(start, goal)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")