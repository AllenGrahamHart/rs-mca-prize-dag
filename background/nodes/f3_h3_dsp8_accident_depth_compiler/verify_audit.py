#!/usr/bin/env python3
"""Audit the accident-depth split on complete small subgroup rows."""

from __future__ import annotations

import collections


def order_root(prime: int, order: int) -> int:
    exponent = (prime - 1) // order
    for base in range(2, prime):
        root = pow(base, exponent, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError((prime, order))


def main() -> None:
    checked = 0
    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        subgroup = [pow(root, exponent, prime) for exponent in range(order)]
        shifted = [(1 - value) % prime for value in subgroup if value != 1]

        products = collections.Counter(
            left * right % prime for left in shifted for right in shifted
        )
        quotients = collections.Counter(
            right * pow(left, -1, prime) % prime
            for left in shifted for right in shifted
        )

        nonidentity_mass = sum(
            count for target, count in quotients.items() if target != 1
        )
        support = {target for target in quotients if target != 1}
        rho_mass = sum(count - 1 for target, count in quotients.items() if target != 1)
        assert nonidentity_mass == (order - 1) * (order - 2)
        assert len(support) >= order - 2
        assert rho_mass == nonidentity_mass - len(support)
        assert rho_mass <= (order - 2) ** 2

        for depth in range(1, 18):
            x18 = 0
            base = 0
            accident = 0
            rho_depth = sum(
                max(count - depth, 0)
                for target, count in quotients.items()
                if target != 1
            )
            assert rho_depth <= rho_mass <= (order - 2) ** 2
            for target, product_count in products.items():
                if target == 1:
                    continue
                excess = max(product_count - 18, 0)
                quotient_count = quotients[target]
                x18 += excess * quotient_count
                base += excess * min(quotient_count, depth)
                accident += excess * max(quotient_count - depth, 0)
            assert x18 == base + accident
            assert base <= depth * (order - 1) ** 2
        checked += 1

    print(f"AUDIT_F3_H3_DSP8_ACCIDENT_DEPTH_COMPILER_PASS rows={checked}")


if __name__ == "__main__":
    main()
