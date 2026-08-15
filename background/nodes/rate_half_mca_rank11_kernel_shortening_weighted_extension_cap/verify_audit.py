#!/usr/bin/env python3
"""Independent audit of shortening-weighted kernel extensions."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def direct_f(r_value: int, w_value: int, d: int, t: int) -> Fraction:
    numerator = prod(r_value + t + offset for offset in range(d + 1))
    denominator = (w_value + d + t) * prod(w_value + offset for offset in range(1, d))
    return Fraction(numerator, denominator)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    r_value, w_value = p["R"], p["w"]
    s_min, s_max = p["K_prime_minimum"] - 10, p["K_prime_maximum"] - 10
    checks = 0
    for d in range(4, 10):
        q = d + 1
        f1 = direct_f(r_value, w_value, d, 1)
        require([f1.numerator, f1.denominator] == p["t1_F_fractions"][str(d)], "F1 custody")
        for s_value in (s_min, s_max):
            target = f1 * comb(s_value - 1, q)
            require(target > p["complete_record_caps"][d - 1] * comb(s_value, q), "branch custody")
            for t in (1, 2, s_value // 3, s_value - q):
                if 1 <= t <= s_value - q:
                    actual = direct_f(r_value, w_value, d, t) * comb(s_value - t, q)
                    require(actual <= target, "direct weighted cap")
                    checks += 1
    require(checks == 48, "audit count")
    print(f"RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_EXTENSION_CAP_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
