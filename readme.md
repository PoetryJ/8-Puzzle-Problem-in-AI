# 8-Puzzle Solver

**Student Name**: Jiang Meishi  
**Student ID**: 225040099  

---

## 1. Overview

This project solves the classic **8-puzzle problem** using two search algorithms:

- **Depth-First Search (DFS)** – Tasks A1 and A2  
- **A\* Search** – Tasks B1 and B2 (with Manhattan distance heuristic)

According to the assignment requirements, since the student ID is **odd**, DFS and A\* are implemented.

---

## 2. File Structure
```
8 Puzzle Problem in AI/
├── README.md              # Project description
├── base.py                # Common data structures and helper functions
├── dfs_solver.py          # DFS implementation
├── astar_solver.py        # A* implementation
├── main.py                # Run all tasks (A1, A2, B1, B2)
└── requirements.txt       # Python requirements
```


---

## 3. How to Run

### Run all tasks
```bash
python main.py
```

This will execute the following tasks in order:
- A1: DFS with fixed start and goal states
- B1: A* with fixed start and goal states
- A2: DFS with random start and goal states
- B2: A* with the same random states as A2

### Run algorithms separately
```bash
python dfs_solver.py
python astar_solver.py
```

---

## 4. Task Description

### Task A1: DFS (Fixed States)
- **Start state**: `[2, 8, 3, 7, 6, 4, 1, 0, 5]`
- **Goal state**: `[1, 2, 3, 8, 0, 4, 7, 6, 5]`
- **Algorithm**: Depth-First Search(DFS)

### Task B1: A* (Fixed States)
- **Start state**: `[2, 8, 3, 7, 6, 4, 1, 0, 5]`
- **Goal state**: `[1, 2, 3, 8, 0, 4, 7, 6, 5]`
- **Algorithm**:A* Search
- **Heuristic**: Manhattan distance

### Task A2: DFS (Random States)
- **Random seed**: 225040099
- **Algorithm**: Depth-First Search(DFS)
- The generated start and goal states are guaranteed to be solvable.

### Task B2: A* (Random States)
- **Random seed**: 225040099
- **Algorithm**: A* Search
- Uses the same random start and goal states as Task A2.

---

## 5. Algorithm Details

### Depth-First Search (DFS)
- Implemented using a stack
- Uses a visited set to avoid revisiting states
- Each state keeps a parent pointer to reconstruct the solution path

### A* Search
- Implemented using a priority queue
- Evaluation function: `f(n) = g(n) + h(n)`
  - `g(n)`: path cost from the start state
  - `h(n)`: Manhattan distance to the goal state
- Guarantees an optimal solution

### Manhattan Distance Heuristic
```
h(n) = Σ |current_x - goal_x| + |current_y - goal_y|
```
For each tile (excluding the blank), the Manhattan distance between its current
position and its goal position is computed and summed.

### Solvability Check
A pair of 8-puzzle states is solvable if the parity of inversion counts
of the start and goal states is the same.

This condition is checked automatically for random state generation.

---

## 6. Output

For each task, the program prints:
- The sequence of moves from start to goal
- The complete solution path


---

## 7. References

- GeeksforGeeks - 8 Puzzle Problem: https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/
- GeeksforGeeks - A* Algorithm: https://www.geeksforgeeks.org/a-search-algorithm/

---

## 8. Submission Note

This project is submitted as part of the Artificial Intelligence course assignment.
All code is written in Python and follows the given assignment instructions.

---

## Contact

For any questions regarding this project, please contact:

- **Student Name**: Meishi Jiang 
- **Email**: 225040099@link.cuhk.edu.cn


