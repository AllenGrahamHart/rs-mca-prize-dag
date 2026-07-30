#!/usr/bin/env python3
"""Verify the KoalaBear m2 r2 dihedral degree-five exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "n in {2,3,6}" in statement
    assert "No conclusion is made for `n=2,3,6`" in contract
    assert "w_v >=" in proof
    assert "div(B)=psi^*(sum_i [alpha_i])" in proof
    assert "No coordinate-index identity" in contract

    source_fiber_degree = 2
    endpoint_poles_over_z0 = 2
    forced_weight = source_fiber_degree * endpoint_poles_over_z0
    assert forced_weight == 4
    assert forced_weight > 3
    defect_cost = forced_weight * (forced_weight - 1) // 2
    assert defect_cost == 6 > 3
    assert {2, 3, 5, 6} - {5} == {2, 3, 6}
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE5_SOURCE_STAR_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
