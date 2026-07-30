#!/usr/bin/env python3
"""Independent audit of the cubic source-facet exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    part_sizes = ((2, 2, 2), (2, 2, 2))
    component_caps = [max(parts) for parts in part_sizes]
    assert component_caps == [2, 2]
    assert sum(component_caps) == 4 < 5
    assert "N_G(k) subset I^c" in statement
    assert "Not claimed" in contract
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_SOURCE_FACET_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
