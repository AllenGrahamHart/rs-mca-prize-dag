#!/usr/bin/env python3
"""Exact congruence replay for the core-free degree-two exclusion."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = 2 * E - 1


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    need(E % 3 == 0, "official e is not divisible by three")
    all_baseline = E - 1
    one_extra = (E - 2) + 3
    need(all_baseline % 3 != E % 3, "baseline congruence did not fail")
    need(one_extra > E, "single extra order did not overshoot")
    for i0, deficits in ((0, (1, 1)), (1, (1, 2))):
        incidence_degree = sum(E - c for c in deficits)
        forced_degree = incidence_degree + 2 * i0
        need(DELTA - forced_degree == 1 - i0, "determinant remainder failed")
    print(f"CORE_FREE_DEGREE_TWO_EXCLUSION_PASS e={E} baseline={all_baseline} overshoot={one_extra}")


if __name__ == "__main__":
    main()
