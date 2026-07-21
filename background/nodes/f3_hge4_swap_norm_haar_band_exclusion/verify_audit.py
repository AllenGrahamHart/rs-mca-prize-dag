#!/usr/bin/env python3
"""Independent audit for the HGE4 swap norm exclusion."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "background" / "nodes" / "f3_hge4_swap_norm_haar_band_exclusion"


def endpoint_audit() -> None:
    order = 1 << 41
    cap = order // 82 - 1
    assert cap == 26_817_356_774
    assert 41 * (cap + 1) <= order // 2
    assert 41 * (cap + 2) > order // 2


def parseval_audit() -> None:
    # One point from each occupied antipodal pair gives exact odd energy h.
    values = [1, 0, -1, 0, 0, 0, 0, 0]
    half = len(values) // 2
    occupied = sum(value * value for value in values)
    odd_energy = sum(
        (values[index] - values[index + half]) ** 2 for index in range(half)
    )
    assert occupied == odd_energy == 2

    # Occupying both antipodes breaks the load-bearing equality.
    mutation = [1, 0, -1, 0, 1, 0, 0, 0]
    occupied_mutation = sum(value * value for value in mutation)
    odd_mutation = sum(
        (mutation[index] - mutation[index + half]) ** 2 for index in range(half)
    )
    assert occupied_mutation == 3 and odd_mutation == 1


def strict_prime_audit() -> None:
    order, width = 16, 3
    lower_at_equality = (order * order) ** ((width - 1) // 2)
    comparison = order ** (width - 1)
    assert lower_at_equality == comparison
    assert (order * order + 1) ** ((width - 1) // 2) > comparison


def packet_language_audit() -> None:
    statement = (BASE / "statement.md").read_text()
    proof = (BASE / "proof.md").read_text()
    result = (BASE / "result.md").read_text()
    assert "only if" in statement and "m^(h-1)<h^(m/4)" in statement
    assert "Parseval and AM--GM" in proof
    assert "full Haar band" in statement
    assert "only the free class" in result and "Vandermonde-defect" in result
    assert "HGE4 is proved" not in statement + proof + result


def main() -> None:
    endpoint_audit()
    parseval_audit()
    strict_prime_audit()
    packet_language_audit()
    print("F3_HGE4_SWAP_NORM_HAAR_BAND_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
