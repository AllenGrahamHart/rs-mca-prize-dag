#!/usr/bin/env python3
"""Exhaust the one-coordinate logic of the common-mismatch theorem."""

from itertools import product


def main() -> None:
    checked = 0
    alphabet = range(3)
    for values in product(alphabet, repeat=4):
        for received in alphabet:
            for mask in range(1, 1 << 4):
                if any((mask >> i) & 1 and values[i] != received for i in range(4)):
                    continue
                if len(set(values)) == 1:
                    assert values[0] == received
                checked += 1

    print(f"BUDGET_THREE_COMMON_MISMATCH_ZERO_PASS cases={checked}")


if __name__ == "__main__":
    main()
