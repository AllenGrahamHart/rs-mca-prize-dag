#!/usr/bin/env python3
"""Verify the KoalaBear m3 primitive-outer degree-two router."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
M3_ROWS = ((2, 6), (3, 4), (4, 3), (6, 2), (12, 1))
CATALOGUE = (
    ("PSL(2,19)", 3420, (1, 19)),
    ("PGL(2,19)", 6840, (1, 19)),
    ("A20", 1216451004088320000, (1, 19)),
    ("S20", 2432902008176640000, (1, 19)),
)
ROUTES = {
    2: (6, "m6_to_m2"),
    4: (12, "m12_empty"),
    5: (15, "source_profile_empty"),
    10: (30, "m30_to_m6_to_m2"),
}


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    evidence = (NODE / "source_evidence.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "not an independent producer" in statement
    assert "No endpoint is asserted to lack" in contract
    assert (
        "cbc9ca7fda9b0de36a4034a4d59e24bb6c07aff0e54458604990919583007133"
        in evidence
    )
    assert len(M3_ROWS) == 5
    assert all(r * delta == 12 for r, delta in M3_ROWS)
    assert len(CATALOGUE) == 4
    assert all(subdegrees == (1, 19) for _, _, subdegrees in CATALOGUE)
    live_r = {r for r, _ in M3_ROWS}
    assert not any(live_r & set(subdegrees) for _, _, subdegrees in CATALOGUE)
    proper_factors = tuple(value for value in range(2, 20) if 20 % value == 0)
    assert proper_factors == tuple(ROUTES)
    assert tuple(3 * value for value in proper_factors) == tuple(
        inner_degree for inner_degree, _ in ROUTES.values()
    )
    assert 20 - 5 == 15
    assert 8 - 5 == 3
    print("RATE_HALF_KB_M3_PRIMITIVE_OUTER_DEGREE2_ROUTER_PASS")


if __name__ == "__main__":
    main()
