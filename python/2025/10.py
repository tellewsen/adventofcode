"""Solution to Advent of Code 2025 Day 10.

https://adventofcode.com/2025/day/10

Part 1: Each button toggles counters (mod 2). Find minimal presses to reach target.
Part 2: Each button increments counters. Find minimal presses to reach target.
"""

import numpy as np
import galois
from itertools import product
from scipy.optimize import milp, LinearConstraint, Bounds


def solver(inp: str):
    return p1(inp), p2(inp)


def row_elements(line: str):
    target, *rest = line.split(" ")
    target = target.strip("[]")
    target = tuple(int(c == "#") for c in target)

    joltage = rest[-1]
    joltage = tuple(map(int, joltage.strip("{}").split(",")))

    buttons = rest[:-1]
    buttons = [tuple(map(int, b.strip("()").split(","))) for b in buttons]

    # Build matrix equation A x = c, where c = t+p
    t = np.array(target)
    j = np.array(joltage)

    # Build the A matrix
    A = np.zeros((len(t), len(buttons)), dtype=int)
    for j_idx, button in enumerate(buttons):
        for pos in button:
            A[pos, j_idx] = 1
    return A, t, j


def p1(inp: str):
    """Solve part 1

    Each line is on the form [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    target: .##.
    buttons: (3) (1,3) (2) (2,3) (0,2) (0,1)
    joltage requirements: {3,5,4,7}
    """
    total_presses = 0
    for line in inp.splitlines():
        A, t, _ = row_elements(line)
        total_presses += solve(A, t)
    return total_presses


def solve(A, b):
    """Solve Ax = b (mod 2) using galois package for GF(2) operations."""
    GF2 = galois.GF(2)

    # Convert to GF(2)
    M = GF2(A)
    b_vec = GF2(b)

    # Augment [M | b]
    aug = np.column_stack([M, b_vec])
    m, n = M.shape

    # Row reduce to reduced row echelon form
    aug_rref = aug.row_reduce()

    # Find pivot columns
    pivot_cols = []
    pivot_row = 0
    for col in range(n):
        if pivot_row < m and aug_rref[pivot_row, col] == 1:
            # Check if this is a pivot (all zeros above and below)
            is_pivot = True
            for other_row in range(m):
                if other_row != pivot_row and aug_rref[other_row, col] == 1:
                    is_pivot = False
                    break
            if is_pivot:
                pivot_cols.append(col)
                pivot_row += 1

    # Identify free variables
    free_vars = [i for i in range(n) if i not in pivot_cols]

    # If no free variables, extract the unique solution
    if not free_vars:
        x = np.zeros(n, dtype=int)
        for i, col in enumerate(pivot_cols):
            if i < m:
                x[col] = int(aug_rref[i, -1])
        return int(sum(x))

    # If there are free variables, try all combinations to find minimum
    min_presses = float("inf")

    for free_values in product([0, 1], repeat=len(free_vars)):
        x = GF2.Zeros(n)

        # Set free variables
        for i, var in enumerate(free_vars):
            x[var] = free_values[i]

        # Back-substitute to find pivot variables from RREF
        for i, col in enumerate(pivot_cols):
            if i < m:
                val = aug_rref[i, -1]
                for j in range(col + 1, n):
                    val = val - aug_rref[i, j] * x[j]
                x[col] = val

        # Convert to int for counting
        presses = sum(int(xi) for xi in x)
        if presses < min_presses:
            min_presses = presses

    return int(min_presses)


def p2(inp: str):
    """Solve part 2

    For part 2, buttons increment counters. We need to solve Ax = b where:
    - A is the button matrix (A[i,j] = 1 if button j affects counter i)
    - x is the number of presses for each button
    - b is the joltage requirements

    This is minimizing sum(x) subject to Ax = b, x >= 0 (integer).
    """
    total_presses = 0
    for line in inp.splitlines():
        A, _, joltage = row_elements(line)
        presses, _ = solve_integer_lp(A, joltage)
        total_presses += presses
    return total_presses


def solve_integer_lp(A, b):
    """Solve min sum(x) subject to Ax = b, x >= 0 (integer) using MILP."""
    m, n = A.shape

    # Objective: minimize sum of all x_i (button presses)
    c = np.ones(n)

    # Constraints: Ax = b means both Ax >= b and Ax <= b
    constraints = LinearConstraint(A, b, b)

    # Bounds: x_i >= 0
    bounds = Bounds(0, np.inf)

    # All variables must be integers
    integrality = np.ones(n, dtype=int)

    # Solve the MILP with options to improve success rate
    result = milp(
        c,
        constraints=constraints,
        bounds=bounds,
        integrality=integrality,
        options={"presolve": True},
    )

    if result.success:
        x = np.round(result.x).astype(int)  # Round to handle floating point errors
        # Verify the solution
        if np.all(A @ x == b):
            return int(np.sum(x)), True

    raise Exception("MILP solver failed to find a solution.")
