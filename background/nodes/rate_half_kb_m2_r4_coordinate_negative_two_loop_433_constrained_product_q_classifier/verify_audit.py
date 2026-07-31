#!/usr/bin/env python3
"""Independent finite-field audit of constrained 433 packets."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def rank_mod(rows, prime):
    matrix = [[value % prime for value in row] for row in rows]
    pivot = 0
    for column in range(4):
        row = next((i for i in range(pivot, len(matrix)) if matrix[i][column]), None)
        if row is None:
            continue
        matrix[pivot], matrix[row] = matrix[row], matrix[pivot]
        inv = pow(matrix[pivot][column], -1, prime)
        matrix[pivot] = [value*inv % prime for value in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot and matrix[i][column]:
                scale = matrix[i][column]
                matrix[i] = [(a-scale*b) % prime for a,b in zip(matrix[i],matrix[pivot])]
        pivot += 1
    return pivot


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(prime, m, c, ell, cell):
    b = -c**3 % prime
    if cell == "X2": labels = (-m*m,m,1,m*m,-m)
    elif cell == "N1": labels = (-1,m,1,m*m,-m)
    else: labels = (ell,m,1,-1,-m)
    labels = tuple(value % prime for value in labels)
    products = (-1 % prime, -c*c % prime, b, -b % prime, b*c % prime)
    require(len(set(labels)) == len(set(products)) == 5, f"distinct {cell}")
    rows = [[-p,-p*k,1,k] for k,p in zip(labels,products)]
    require(rank_mod(rows,prime) == 3, f"rank {cell}")
    L,Z=labels[0],labels[4]
    q=(Z*(1-L)**2*(c*c+b)**2-c*c*(1+b)**2*(Z-L)**2)%prime
    require(q == 0, f"q {cell}")


def main() -> None:
    check(11,7,7,6,"X2")
    check(11,7,3,10,"N1")
    check(113,15,23,74,"L1")
    statement=(NODE/"statement.md").read_text()
    require("F_11" in statement and "F_113" in statement, "witness pins")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_CONSTRAINED_AUDIT_PASS witnesses=3 ranks=3 q=0")


if __name__ == "__main__":
    main()
