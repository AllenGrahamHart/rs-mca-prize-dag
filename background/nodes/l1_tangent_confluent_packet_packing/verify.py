#!/usr/bin/env python3
"""Exhaustive F_7 replay of tangent confluent-packet packing."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from fractions import Fraction
from math import comb
from pathlib import Path


HELPER = (
    Path(__file__).resolve().parents[1]
    / "l1_split_pencil_content_exact_shell_descent"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_content_helpers", HELPER)
assert SPEC is not None and SPEC.loader is not None
HLP = module_from_spec(SPEC)
SPEC.loader.exec_module(HLP)


def derivative(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    if len(f) <= 1:
        return (0,)
    return HLP.trim(tuple(i * f[i] for i in range(1, len(f))), p)


def main() -> None:
    p = 7
    h = tuple(range(p))
    n, k = len(h), 3
    u_values = (0, 0, 0, 0, 5, 6, 1)
    u_hat = HLP.interpolate(h, u_values, p)
    u_derivative = derivative(u_hat, p)
    shells: dict[int, list[dict[str, object]]] = {}

    for coeffs in product(range(p), repeat=k):
        c = HLP.trim(tuple(coeffs), p)
        support = tuple(x for x in h if HLP.evaluate(c, x, p) == u_values[x])
        a = len(support)
        if a < k:
            continue
        locator = HLP.locator(support, p)
        q, remainder = HLP.divmod_poly(HLP.sub(u_hat, c, p), locator, p)
        assert remainder == (0,)
        owner = HLP.gcd_poly(locator, q, p)
        owner_roots = HLP.roots_on_h(owner, h, p)
        c_derivative = derivative(c, p)
        for x in owner_roots:
            assert HLP.evaluate(c_derivative, x, p) == HLP.evaluate(u_derivative, x, p)
        shells.setdefault(a, []).append(
            {"c": c, "support": support, "owner": owner_roots, "r": len(owner_roots)}
        )

    tangent_total = 0
    packet_total = 0
    mixed_packet_total = 0
    for a, records in sorted(shells.items()):
        for j in range(k // 2 + 1):
            packet_owner: dict[tuple[tuple[int, ...], tuple[int, ...]], tuple[int, ...]] = {}
            incidence = 0
            for row in records:
                r = int(row["r"])
                if r < j:
                    continue
                support = tuple(row["support"])
                owner = tuple(row["owner"])
                c = tuple(row["c"])
                local = 0
                for doubled in combinations(owner, j):
                    available = tuple(x for x in support if x not in doubled)
                    for values in combinations(available, k - 2 * j):
                        packet = (tuple(doubled), tuple(values))
                        assert packet not in packet_owner
                        packet_owner[packet] = c
                        local += 1
                assert local == comb(r, j) * comb(a - j, k - 2 * j)
                incidence += local
            universe = comb(n, j) * comb(n - j, k - 2 * j)
            assert incidence <= universe
            packet_total += incidence

        omega = n - a
        s = n - 2 * a + k
        assert 1 <= s <= omega
        for j in range(s + 1):
            packet_owner = {}
            incidence = 0
            for row in records:
                r = int(row["r"])
                if r < j:
                    continue
                support = tuple(row["support"])
                complement = tuple(x for x in h if x not in support)
                owner = tuple(row["owner"])
                c = tuple(row["c"])
                local = 0
                for doubled in combinations(owner, j):
                    for missed in combinations(complement, s - j):
                        packet = (tuple(doubled), tuple(missed))
                        assert packet not in packet_owner
                        packet_owner[packet] = c
                        local += 1
                assert local == comb(r, j) * comb(omega, s - j)
                incidence += local
            universe = comb(n, j) * comb(n - j, s - j)
            assert incidence <= universe
            mixed_packet_total += incidence

        w = a - k
        for r0 in range(a + 1):
            upper = min(r0, s)
            bounds = [
                Fraction(
                    comb(n, j) * comb(n - j, s - j),
                    comb(r0, j) * comb(omega, s - j),
                )
                for j in range(upper + 1)
            ]
            delta = r0 - w - 1
            ceil_half = -((-delta) // 2)
            j_star = min(upper, max(0, ceil_half))
            assert bounds[j_star] == min(bounds)
            for j in range(upper):
                assert bounds[j + 1] / bounds[j] == Fraction(w + j + 1, r0 - j)
        tangent_total += sum(int(row["r"]) >= 1 for row in records)

    assert set(shells) == {3, 4}
    assert tangent_total > 0
    print(
        "L1_TANGENT_CONFLUENT_PACKET_PACKING_PASS "
        f"shells={{{', '.join(f'{a}:{len(v)}' for a, v in sorted(shells.items()))}}} "
        f"tangent={tangent_total} packet_incidence={packet_total} "
        f"mixed_incidence={mixed_packet_total}"
    )


if __name__ == "__main__":
    main()
