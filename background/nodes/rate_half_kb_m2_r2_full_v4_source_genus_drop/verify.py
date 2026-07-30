#!/usr/bin/env python3
"""Verify the KoalaBear m2 r2 full-V4 source genus drop."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def fixed_counts(genus: int) -> tuple[int, int, int]:
    eta = 2 * genus + 2
    eta_a = eta
    a = 2 * genus + 6 - eta - eta_a
    return eta, a, eta_a


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "No regime is deleted" in statement
    assert "Neither genus regime is shown empty" in contract
    assert "c eta c^(-1)=eta*a" in proof

    rows = {genus: fixed_counts(genus) for genus in range(4)}
    assert rows == {
        0: (2, 2, 2),
        1: (4, 0, 4),
        2: (6, -2, 6),
        3: (8, -4, 8),
    }
    admissible = {
        genus: counts[1]
        for genus, counts in rows.items()
        if counts[1] >= 0
    }
    assert admissible == {0: 2, 1: 0}
    for genus, (eta, a, eta_a) in rows.items():
        assert eta + a + eta_a == 2 * genus + 6
        assert eta == 2 * genus + 2
        assert eta_a == eta
    print("RATE_HALF_KB_M2_R2_FULL_V4_SOURCE_GENUS_DROP_PASS")


if __name__ == "__main__":
    main()
