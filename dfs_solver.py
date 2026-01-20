"""
DFS (Depth-First Search) Solver for 8-Puzzle
使用深度优先搜索解决8-puzzle问题
"""

from base import *

def dfs(start, goal):
    stack = [PuzzleState(start)]
    visited = set()

    while stack:
        current = stack.pop()

        if current.board == goal:
            return current

        visited.add(tuple(current.board))
        blank_pos = current.board.index(0)

        for move in moves:
            if not is_valid_move(move, blank_pos):
                continue

            new_board = move_tile(current.board, move, blank_pos)
            if tuple(new_board) in visited:
                continue

            stack.append(
                PuzzleState(
                    new_board,
                    current,
                    move,
                    current.depth + 1
                )
            )

    return None


if __name__ == "__main__":
    # A1: fixed start & goal
    start = [2, 8, 3, 7, 6, 4, 1, 0, 5]
    goal  = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    print("DFS: A1 Fixed Start/Goal")
    solution = dfs(start, goal)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")

    # A2: random start & goal
    print("\nDFS: A2 Random Start/Goal")
    start, goal = generate_solvable_pair(225040099)

    print("Start:", start)
    print("Goal :", goal)

    solution = dfs(start, goal)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")