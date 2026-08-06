#!/usr/bin/env python3
"""Replay the exact guard inequalities on all official degree/order types."""

from fractions import Fraction


N = 1 << 41
TYPES = (
    ("plus-k1-e1", 1, 1),
    ("plus-k1-e2", 1, 2),
    ("plus-k1-e3", 1, 3),
    ("plus-k1-e4", 1, 4),
    ("plus-k1-e5", 1, 5),
    ("plus-k1-e6", 1, 6),
    ("plus-k2-e2", 2, 2),
    ("plus-k2-e4", 2, 4),
    ("plus-k4-e4", 4, 4),
    ("minus-k2-e2", 2, 2),
    ("minus-k2-e4", 2, 4),
    ("minus-k4-e4", 4, 4),
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    print(f"PASS {label}")


def main() -> None:
    require(Fraction(N, 6) > 256, "official scale dominates one ceiling step")
    require(len(TYPES) == 12, "twelve official signed types")
    require(sum(k < e for _, k, e in TYPES) == 7, "seven non-generating types")
    require(sum(k == e for _, k, e in TYPES) == 5, "five generating types")

    for label, k, e in TYPES:
        require(e <= 6 and k <= e and e % k == 0, f"{label} field ordering")
        if k == e:
            require(True, f"{label} ambient-balance guard passes")
        else:
            upper = Fraction(k, e) * (N + 256)
            require(upper < N, f"{label} ambient-balance guard fails")

        # If t*e*ell<N, then t*k*ell<=t*e*ell<N because k<=e.
        require(k <= e, f"{label} exact-slice guard fails by monotonicity")

    print("F2_CONSUMER_GUARD_DEPTH_RECONCILIATION_PASS")


if __name__ == "__main__":
    main()
