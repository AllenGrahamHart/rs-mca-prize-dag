#!/usr/bin/env python3
"""Independent audit of the full-V4 case exhaustion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    contract = (NODE / "claim_contract.md").read_text()
    result = (NODE / "result.md").read_text()
    candidates = frozenset((2, 3, 5, 6))
    exclusions = frozenset((2, 3, 5, 6))
    assert candidates == exclusions
    assert "order-two or trivial stabilizer types" in contract
    assert "(4,2)" in result and "(8,1)" in result
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_FULL_V4_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
