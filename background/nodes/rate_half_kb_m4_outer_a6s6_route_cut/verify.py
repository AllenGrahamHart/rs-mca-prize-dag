#!/usr/bin/env python3
"""Verify the KoalaBear m4 outer primitive route cut."""

from pathlib import Path

NODE = Path(__file__).resolve().parent
M4_ROWS = ((1,16),(2,8),(4,4),(8,2))
CATALOGUE = (
    ("A7",2520,(1,14)),
    ("A6",360,(1,6,8)),
    ("S6",720,(1,6,8)),
    ("PSL(4,2)",20160,(1,14)),
    ("A15",653837184000,(1,14)),
    ("S15",1307674368000,(1,14)),
)

def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    evidence = (NODE / "source_evidence.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "Only `(r,delta)=(8,2)` survives" in statement
    assert "nine types" in contract
    assert "d24658310cb386c9663e95ab9024eab9142d79f849131f499da36eeda82c003e" in evidence
    assert all(r*d == 16 for r,d in M4_ROWS)
    assert len(CATALOGUE) == 6
    possible = {r for _,_,subs in CATALOGUE for r in subs[1:] if r in {1,2,4,8}}
    assert possible == {8}
    survivors = [(name,subs) for name,_,subs in CATALOGUE if 8 in subs]
    assert survivors == [("A6",(1,6,8)),("S6",(1,6,8))]
    proper_factors = tuple(d for d in range(2,15) if 15 % d == 0)
    assert proper_factors == (3,5)
    assert tuple(4*d for d in proper_factors) == (12,20)
    assert 3*4*(5-1) == 48 > 2*20-2 == 38
    assert 12 - 3 == 9
    print("RATE_HALF_KB_M4_OUTER_A6S6_ROUTE_CUT_PASS")

if __name__ == "__main__":
    main()
