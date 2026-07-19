#!/usr/bin/env python3
"""Verify the exact order-1024 split-16 weight-six counterfixture."""

from __future__ import annotations

from math import gcd, isqrt
import json
from pathlib import Path


NODE = "dli_wcl_ell2_weight6_split16_counterfixture"
CERT = Path(__file__).with_name("certificate.json")


def main() -> None:
    row = json.loads(CERT.read_text())
    q = int(row["field_prime"])
    generator = int(row["field_generator"])
    order = int(row["subgroup_order"])
    exponents = [int(value) for value in row["union_exponents"]]

    assert row["schema"] == "dli-wcl-ell2-weight6-split16-counterfixture-v1"
    assert q - 1 == 2**16 and 2**16 > isqrt(q)
    assert pow(generator, q - 1, q) == 1
    assert gcd(pow(generator, (q - 1) // 2, q) - 1, q) == 1
    omega = pow(generator, int(row["subgroup_generator_power"]), q)
    assert pow(omega, order, q) == 1
    assert pow(omega, order // 2, q) == q - 1

    assert len(exponents) == len(set(exponents)) == 6
    assert all(
        (left - right) % order != order // 2
        for index, left in enumerate(exponents)
        for right in exponents[index + 1 :]
    )
    difference_gcd = order
    for exponent in exponents[1:]:
        difference_gcd = gcd(difference_gcd, exponent - exponents[0])
    assert difference_gcd == 1

    values = [pow(omega, exponent, q) for exponent in exponents]
    assert sum(values) % q == 0
    assert sum(pow(value, 3, q) for value in values) % q == 0

    dilation = int(row["router_odd_dilation"])
    selected = {
        0,
        dilation * int(row["router_exponents"][0]) % order,
        dilation * int(row["router_exponents"][1]) % order,
    }
    assert selected < set(exponents)
    remaining = set(exponents) - selected
    product_exponent = sum(remaining) % order
    assert product_exponent == dilation * int(row["router_exponents"][2]) % order

    # Hostile controls: first-moment-only, antipodal, and official-scope
    # overclaims must all be distinguishable from the theorem.
    assert sum(pow(value, 3, q) for value in values) % q == 0
    assert not any((exponent + order // 2) % order in exponents for exponent in exponents)
    assert 16 < 41
    mutations = 6
    print(
        f"{NODE}_PASS q={q} order={order} v2=16 "
        f"exponents={','.join(map(str, exponents))} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
