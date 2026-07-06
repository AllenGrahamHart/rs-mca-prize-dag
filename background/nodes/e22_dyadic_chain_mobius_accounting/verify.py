#!/usr/bin/env python3
"""Light verifier for triangular minimal-scale accounting."""

from itertools import combinations


def nonempty_subsets(items):
    for r in range(1, len(items) + 1):
        yield from combinations(items, r)


def main() -> None:
    for length in range(1, 9):
        scales = list(range(length))
        # Treat each nonempty admissible-scale set as one support class.
        classes = [set(s) for s in nonempty_subsets(scales)]
        minimal = {idx: min(adm) for idx, adm in enumerate(classes)}

        for j in scales:
            raw = sum(1 for adm in classes if j in adm)
            selected = sum(1 for idx, adm in enumerate(classes) if j in adm and minimal[idx] == j)
            overlaps = sum(
                1
                for i in scales
                if i < j
                for idx, adm in enumerate(classes)
                if j in adm and minimal[idx] == i
            )
            assert raw == selected + overlaps, (length, j, raw, selected, overlaps)

    print("PASS: raw dyadic scale counts split triangularly by minimal scale")


if __name__ == "__main__":
    main()
