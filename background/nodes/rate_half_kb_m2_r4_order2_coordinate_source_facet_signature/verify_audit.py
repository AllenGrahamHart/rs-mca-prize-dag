#!/usr/bin/env python3
"""Independent audit of the order-two source-facet count."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()

    k_j_incidence = 5 * 2 * 2
    total_j_incidence = 6 * 4
    outside_j = total_j_incidence - k_j_incidence
    eta_i_incidence = 2 * 2
    total_i_incidence = 6 * 4
    lc_i = total_i_incidence - eta_i_incidence
    lc_edges = 12
    ij = outside_j
    ii_lc = lc_edges - ij
    assert (k_j_incidence // 2, 2 + ii_lc, ij) == (10, 10, 4)

    pair_complements = {(2, 0, 0), (1, 1, 0)}
    profiles = {
        tuple(sorted((4 - c for c in values for _ in range(2)), reverse=True))
        for values in pair_complements
    }
    assert profiles == {(4, 4, 4, 4, 2, 2), (4, 4, 3, 3, 3, 3)}
    assert "Not claimed" in contract
    assert "bar(I)=I" in statement and "bar(J)=J" in statement
    print("RATE_HALF_KB_M2_R4_ORDER2_COORDINATE_SOURCE_FACET_SIGNATURE_AUDIT_PASS")


if __name__ == "__main__":
    main()
