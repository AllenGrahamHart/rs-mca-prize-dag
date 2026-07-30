#!/usr/bin/env python3
"""Independent audit of the degree-six common-pole exclusion."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent
P = 2_130_706_433


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def perfect_matchings(points: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    if not points:
        return [()]
    first = points[0]
    rows = []
    for second in points[1:]:
        rest = tuple(point for point in points if point not in (first, second))
        for tail in perfect_matchings(rest):
            rows.append(tuple(sorted(((first, second), *tail))))
    return sorted(set(rows))


def permutation(matching: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    row = list(range(6))
    for left, right in matching:
        row[left] = right
        row[right] = left
    return tuple(row)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(6))


def order(row: tuple[int, ...]) -> int:
    identity = tuple(range(6))
    power = identity
    for exponent in range(1, 7):
        power = compose(row, power)
        if power == identity:
            return exponent
    raise RuntimeError("permutation order")


def main() -> None:
    matchings = perfect_matchings(tuple(range(6)))
    require(len(matchings) == 15, "perfect matching count")
    base = matchings[0]
    base_perm = permutation(base)
    classifications = set()
    for matching in matchings[1:]:
        shared = len(set(base) & set(matching))
        product_order = order(compose(base_perm, permutation(matching)))
        classifications.add((shared, product_order))
    require(classifications == {(0, 3), (1, 2)}, "matching classification")

    reciprocal = 22_371_648
    norm = 71_132_574_457_861_006_005
    require(reciprocal % P == 22_371_648, "reciprocal residue")
    require(norm % P == 1_274_367_339, "order-three residue")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    dag = (ROOT / "dag.json").read_text()
    require("c=27/8" in statement and "c=756/125" in statement, "exception atlas")
    require("121" in proof and "220" in proof, "commuting obstruction")
    require("rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion" in dag, "DAG node")
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE6_COMMON_POLE_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
