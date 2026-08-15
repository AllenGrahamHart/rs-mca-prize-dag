#!/usr/bin/env python3
"""Independent audit of the residual-petal capacity cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2980ce37664731e481b65d74ea39f4635ef8e9cba09bd8c22d48cc1493d1a1a8"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ratio(p: dict[str, int], k: int) -> Fraction:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    lower = Fraction(
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2),
        p["lane_density_denominator"] * comb(n, 9),
    )
    j = k - 1
    upper = Fraction(p["fixed_owner_record_cap"] * (n - j) * (m + j - 20), 2)
    return lower / upper


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    samples = [15634, 15635, 17000, 19000, 20617]
    values = [ratio(p, k) for k in samples]
    require(values[0] < 1 < values[1], "adjacent crossing")
    require(all(a < b for a, b in zip(values[1:], values[2:])), "ratio monotonicity")

    factor_checks = 0
    for k in range(12, p["closed_K_prime_maximum"] + 1):
        # The nine Reed--Solomon factors have forward cross-difference n'-m'=D.
        n, m = p["n_offset"] + k, p["m_offset"] + k
        for i in range(9):
            require((m + 1 - i) * (n - i) - (m - i) * (n + 1 - i) == p["support_complement"], "RS factor")
            factor_checks += 1
        # The remaining factor cancels one positive term before this identity.
        raw = (k + 67464) * (k + 67463) * (2 * k + 67451) - (k + 67463) * (k + 67462) * (2 * k + 67453)
        require(raw == 2 * (k - 11) * (k + 67463) > 0, "terminal factor")
        factor_checks += 1

    core_checks = 0
    for k in (10, 1000, 15634, 15635, 20617):
        n, m = p["n_offset"] + k, p["m_offset"] + k
        previous = (n - 9) * (m - 11)
        for j in range(9, k - 1):
            current = (n - (j + 1)) * (m + (j + 1) - 20)
            require(current > previous, f"core monotonicity K'={k}, j={j}")
            previous = current
            core_checks += 1

    proof = (HERE / "proof.md").read_text()
    for pin in ("J subset Z(u)", "s_p(j-9)+C(s_p,2)", "petals `P_p` are pairwise disjoint", "D-2j+19", "2(K'-11)"):
        require(pin in proof, f"proof pin {pin}")
    require("134944" not in proof, "no original-row floor")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_RESIDUAL_PETAL_CAPACITY_CUT_AUDIT_PASS "
        f"samples={len(samples)} factor_checks={factor_checks} "
        f"core_checks={core_checks} proof_pins=5/5"
    )


if __name__ == "__main__":
    main()
