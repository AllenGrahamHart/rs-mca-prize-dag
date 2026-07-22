#!/usr/bin/env python3
"""Mutation audit for the colored-code equivalence."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    p, omega = 7, 2
    one_constraint_non_equal = []
    for s0 in range(p):
        for s1 in range(p):
            for s2 in range(p):
                first = (s0 + omega * s1 + omega * omega * s2) % p
                second = (s0 + omega * omega * s1 + omega * s2) % p
                if first == 0 and not (s0 == s1 == s2):
                    one_constraint_non_equal.append((s0, s1, s2, second))
    assert one_constraint_non_equal
    assert any(second != 0 for *_prefix, second in one_constraint_non_equal)

    statement = (HERE / "statement.md").read_text()
    assert "b^[2] in C_M" in statement
    assert "coefficientwise cube" in statement
    assert "does not prove" in statement
    print("L1_M4_H3_COLORED_CYCLIC_EQUIVALENCE_AUDIT_PASS checks=5")


if __name__ == "__main__":
    main()
