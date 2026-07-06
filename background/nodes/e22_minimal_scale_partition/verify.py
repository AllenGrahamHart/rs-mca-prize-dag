#!/usr/bin/env python3
"""Light verifier for the dyadic minimal-scale partition."""

from itertools import combinations


def nonempty_subsets(items: list[int]):
    for r in range(1, len(items) + 1):
        yield from combinations(items, r)


def main() -> None:
    for exponent in range(2, 10):
        moduli = [2**i for i in range(1, exponent + 1)]
        cells = {m: [] for m in moduli}
        for admissible_tuple in nonempty_subsets(moduli):
            admissible = set(admissible_tuple)
            minimal = min(admissible)
            tail_minimal_cells = [
                m
                for m in moduli
                if m in admissible and all(sm not in admissible for sm in moduli if sm < m)
            ]
            assert tail_minimal_cells == [minimal], (moduli, admissible, tail_minimal_cells)
            cells[minimal].append(frozenset(admissible))

        seen = set()
        for members in cells.values():
            for member in members:
                assert member not in seen
                seen.add(member)
        assert len(seen) == 2 ** len(moduli) - 1

    print("PASS: dyadic admissible classes partition by unique minimal scale")


if __name__ == "__main__":
    main()
