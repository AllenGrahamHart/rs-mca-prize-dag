#!/usr/bin/env python3
"""Independent arithmetic audit of the cell-12 boundary census."""

import ast
import json
from pathlib import Path
import re

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
BOUNDARY = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
PRIME = 2130706433
z, c, b, t = sp.symbols("z c b t")
SYMBOLS = {"z": z, "c": c, "b": b, "t": t}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_singular(text):
    expression = 0
    for term in re.findall(r"[+-]?[^+-]+", text):
        sign = -1 if term.startswith("-") else 1
        unsigned = term.lstrip("+-")
        digits = re.match(r"\d*", unsigned).group()
        monomial = sp.Integer(sign * int(digits or "1"))
        for variable, exponent in re.findall(
            r"([zcbt])(\d*)", unsigned[len(digits):]
        ):
            monomial *= SYMBOLS[variable] ** int(exponent or "1")
        expression += monomial
    return expression


def pairings(values):
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def main():
    ast.parse((NODE / "verify.py").read_text())
    cells = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        cells.extend((singleton, matching) for matching in pairings(rest))
    require(cells[12] == (4, ((0, 1), (2, 3))),
            "cell-12 role reconstruction")
    payload = json.loads(BOUNDARY.read_text())
    points = 0
    nonsplit = 0
    for row in payload["rows"]:
        if row["boundary"] == "b_leading":
            for point in row["rational_points"]:
                values = {
                    t: point["t"], b: point["b"], c: point["c"],
                    z: point["z"],
                }
                require(all(int(parse_singular(poly).subs(values)) % PRIME == 0
                            for poly in row["lex_basis"]),
                        "boundary point misses lex ideal")
                rv, tv, bv, cv = (
                    point[name] for name in ("r", "t", "b", "c")
                )
                guards = (
                    rv, tv, bv, cv, bv-1, bv+1, cv-1, cv+1, bv-cv, bv+cv,
                    rv*rv-1, rv*rv+1, tv*tv-1, tv*tv+1,
                    tv*tv-rv*rv, tv*tv+rv*rv,
                )
                require(all(value % PRIME for value in guards),
                        "boundary point violates route guard")
                points += 1
        else:
            eliminant = sp.Poly(
                sp.sympify(row["b_factors"][0]["expression"]),
                b, modulus=PRIME,
            )
            discriminant = int(sp.discriminant(eliminant.as_expr(), b)) % PRIME
            require(pow(discriminant, (PRIME - 1) // 2, PRIME) == PRIME - 1,
                    "quadratic boundary eliminant splits")
            nonsplit += 1

    proof = (NODE / "proof.md").read_text()
    statement = (NODE / "statement.md").read_text()
    require("`BC-` is the singleton" in statement and
            "outside record" in statement and "does not close" in statement,
            "scope and role audit")
    require(points == 8 and nonsplit == 8, "boundary totals")
    print("audit=ok cell=12 boundary_points=8 nonsplit_fibers=8")


if __name__ == "__main__":
    main()
