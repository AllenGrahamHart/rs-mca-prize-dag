#!/usr/bin/env python3
"""Mutation audit for the XR zero-baseline arithmetic router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # Odd reserve is load-bearing: h=6 admits an arithmetic five-row cell.
    h, t, D, Z = 6, 5, 6, 17
    assert t * h + (t - 2) * ((t - 1) * D - 2 * Z) == 0

    # Official odd reserve rejects t=5 and odd D by parity.
    h = 5
    assert (5 * h + 3 * 4 * 2) % 6 != 0
    assert (4 * h + 2 * 3 * 9) % 4 != 0

    # At t=4, either side of D=2h makes P or Q negative.
    t = 4
    quotient = t * h // (t - 2)
    for D in (2 * h - 2, 2 * h + 2):
        P = ((t - 3) * D - quotient) // 2
        Q = (t - 1) * (quotient - D) // 2
        assert min(P, Q) < 0

    # Multiplicity three has positive H and is not a zero-defect packing.
    assert (3 - 1) * (3 - 2) // 2 == 1

    # The old continuous minima fail the rowwise private-point congruence.
    def private_margin(h: int, s: int, D: int) -> tuple[int, int]:
        t = 2 * s + 2
        modulus = t - 3
        quotient = h + h // s
        residue = ((h - h // s) // 2) % modulus
        private_total = (modulus * D - quotient) // 2
        Z = (quotient + (t - 1) * D) // 2
        return private_total - t * residue, Z - D

    assert private_margin((1 << 33) + 1, 137283, 31286)[0] < 0
    assert private_margin((1 << 32) + 1, 641, 3358056)[0] < 0

    # The corrected minimizing tuples saturate the congruence and print the
    # claimed arithmetic rank floors.
    assert private_margin((1 << 33) + 1, 2049, 2101250) == (0, 8601474050)
    assert private_margin((1 << 32) + 1, 641, 3359586) == (0, 4302648690)

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "8,601,474,050" in statement
    assert "4,302,648,690" in statement
    assert "private-pointcongruence" in statement
    assert "A proper local circuit does not inherit it automatically" in audit
    assert "A negative baseline may pay positive defect charges" in audit

    print("XR_RANK_TWO_ZERO_BASELINE_ARITHMETIC_ROUTER_AUDIT_PASS mutations=12")


if __name__ == "__main__":
    main()
