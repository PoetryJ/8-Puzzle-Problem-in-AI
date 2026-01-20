"""
8-Puzzle Solver - Main Program
Run tasks A1, A2, B1, B2
Student ID: 225040099
"""

from base import *
from dfs_solver import dfs
from astar_solver import a_star


def run_task(name, algorithm, solver, start, goal):
    print("\n" + "=" * 60)
    print(f"{name}: {algorithm}")
    print("=" * 60)

    print("Start state:")
    print_board(start)

    print("Goal state:")
    print_board(goal)

    solution = solver(start, goal)

    if solution:
        print("\nSolution path:")
        print_solution(solution)
    else:
        print("\nNo solution found.")


if __name__ == "__main__":
    STUDENT_ID = 225040099

    # A1: DFS with fixed start and goal
    start_fixed = [2, 8, 3, 7, 6, 4, 1, 0, 5]
    goal_fixed  = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    run_task(
        name="A1",
        algorithm="DFS (Fixed Start & Goal)",
        solver=dfs,
        start=start_fixed,
        goal=goal_fixed
    )

    # B1: A* with fixed start and goal
    run_task(
        name="B1",
        algorithm="A* (Fixed Start & Goal)",
        solver=a_star,
        start=start_fixed,
        goal=goal_fixed
    )

    # A2 & B2: Random start and goal
    start_random, goal_random = generate_solvable_pair(STUDENT_ID)

    # A2: DFS with random states
    run_task(
        name="A2",
        algorithm="DFS (Random Start & Goal)",
        solver=dfs,
        start=start_random,
        goal=goal_random
    )

    # B2: A* with random states
    run_task(
        name="B2",
        algorithm="A* (Random Start & Goal)",
        solver=a_star,
        start=start_random,
        goal=goal_random
    )
