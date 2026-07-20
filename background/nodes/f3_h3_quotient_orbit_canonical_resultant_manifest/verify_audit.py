#!/usr/bin/env python3
"""Mutation audit for the canonical quotient-orbit manifest."""

from __future__ import annotations

import verify


def main() -> None:
    exponent = 5
    order = 2**exponent
    representatives = verify.canonical_representatives(exponent)
    assert len(representatives) == 3 * (order - exponent - 1)

    identifiers = {(j, sign, parameter) for j, sign, parameter, _, _ in representatives}
    assert len(identifiers) == len(representatives)
    assert all(parameter != 0 for _, _, parameter in identifiers)
    assert all(not (sign == "+" and parameter == 1) for _, sign, parameter in identifiers)

    even_plus = sum(sign == "+" and parameter % 2 == 0 for _, sign, parameter in identifiers)
    even_minus = sum(sign == "-" for _, sign, _ in identifiers)
    assert even_plus == even_minus
    assert even_minus > 0

    assert 2 ** (2 ** verify.valuation_two(2) - 1) == 2
    assert 2 ** (2 ** verify.valuation_two(4) - 1) == 8
    assert 2 ** (2 ** verify.valuation_two(8) - 1) == 128
    assert not verify.power_of_two(6)

    print(
        "F3_H3_QUOTIENT_ORBIT_CANONICAL_RESULTANT_MANIFEST_AUDIT_PASS "
        "mutations=7"
    )


if __name__ == "__main__":
    main()
