#!/usr/bin/env python3
"""Exact lift/common-locator replay on the F_17 distance-three fixture."""

from __future__ import annotations

from itertools import combinations


P = 17
CORE = 1
DOMAIN = tuple(range(1, P))


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return out


def locator(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % P, 1])
    return out


def evaluate(poly: list[int], x: int) -> int:
    return sum(coefficient * pow(x, degree, P) for degree, coefficient in enumerate(poly)) % P


def annihilates(sequence: list[int], poly: list[int]) -> bool:
    rows = len(sequence) - len(poly) + 1
    return all(
        sum(poly[j] * sequence[i + j] for j in range(len(poly))) % P == 0
        for i in range(rows)
    )


def lift(sequence: list[int], tau: int) -> list[int]:
    out = [tau]
    for value in sequence:
        out.append((CORE * out[-1] + value) % P)
    return out


def main() -> None:
    h_0 = [0, 10, 2, 16, 7, 8, 3]
    h_1 = [15, 16, 6, 2, 14, 12, 1]
    a = locator((2, 5)) + [0]
    b = locator((3, 13, 15))
    q_1 = [(right - left) % P for left, right in zip(a, b, strict=True)]
    supported = (0, 1, 2, 4, 15)
    external = {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}

    # Every lift is annihilated by the full fixed-core locator at each
    # required slope; two representative lift pairs also replay directly.
    for tau_0, tau_1 in ((0, 0), (3, 7)):
        y_0 = lift(h_0, tau_0)
        y_1 = lift(h_1, tau_1)
        for z in supported:
            h_z = [(left + z * right) % P for left, right in zip(h_0, h_1, strict=True)]
            y_z = [(left + z * right) % P for left, right in zip(y_0, y_1, strict=True)]
            q_z = [(left + z * right) % P for left, right in zip(a, q_1, strict=True)]
            full_q = multiply([(-CORE) % P, 1], q_z)
            assert annihilates(h_z, q_z)
            assert annihilates(y_z, full_q)

    base_y = (lift(h_0, 0), lift(h_1, 0))
    core_common = []
    off_core_compatible = []
    for roots in combinations(DOMAIN, 4):
        full_q = locator(roots)
        if CORE in roots:
            residual_q = locator(tuple(root for root in roots if root != CORE))
            if annihilates(h_0, residual_q) and annihilates(h_1, residual_q):
                core_common.append(roots)
            continue

        lift_pair = []
        compatible = True
        core_value = evaluate(full_q, CORE)
        assert core_value
        for y in base_y:
            residuals = [
                sum(full_q[j] * y[i + j] for j in range(5)) % P
                for i in range(4)
            ]
            if any(residuals[i] != pow(CORE, i, P) * residuals[0] % P for i in range(4)):
                compatible = False
                break
            lift_pair.append(-residuals[0] * inv(core_value) % P)
        if compatible:
            off_core_compatible.append((roots, tuple(lift_pair)))

    assert core_common == []
    assert off_core_compatible == []
    external_union = set().union(*(set(roots) for roots in external.values()))
    assert len(external_union) == 9 > 4  # 6e+3 > r+1 at e=1.

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_ORIGINAL_LIFT_COLUMN_FAR_CONVERSE_PASS "
        f"field={P} full_locators=1820 core_common=0 off_core_common=0 "
        f"external_union={len(external_union)}"
    )


if __name__ == "__main__":
    main()
