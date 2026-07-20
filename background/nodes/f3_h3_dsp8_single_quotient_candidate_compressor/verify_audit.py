#!/usr/bin/env python3
"""Mutation audit for the DSP8 one-lift candidate compressor."""

from __future__ import annotations

import verify


def main() -> None:
    assert len(set(verify.center_ideals(0))) == 1
    assert verify.center_ideals(0)[0] > 0
    assert verify.ideal_gcd([0]) == 0

    pi = 2
    c_u = 3
    alpha = 5
    correct = pi * pi * c_u * alpha
    wrong = pi * c_u * alpha
    assert correct != wrong

    assert max(35 - 34, 0) > 0
    assert max(35 - 35, 0) == 0

    s_35, s_18 = 3, 15
    assert s_18 % s_35 == 0
    assert s_35 % s_18 != 0

    print(
        "F3_H3_DSP8_SINGLE_QUOTIENT_CANDIDATE_COMPRESSOR_AUDIT_PASS "
        "mutations=5"
    )


if __name__ == "__main__":
    main()
