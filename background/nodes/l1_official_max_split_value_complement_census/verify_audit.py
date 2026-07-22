#!/usr/bin/env python3
"""Mutation audit for the maximal split-value complement census."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "background" / "nodes" / "l1_official_max_split_value_complement_census"


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    audit = (NODE / "audit.md").read_text()
    checks = 0

    for anchor in (
        "m=floor(n/p)",
        "s=n-mp",
        "Q(0)=0",
        "ell_h=u-d+p",
        "nine `m>=3` rows",
        "seven broad official",
        "p=1 mod m",
        "p=-1 mod m",
    ):
        assert anchor in statement
        checks += 1

    for anchor in (
        "First suppose `Q=0`",
        "The coefficient matrix is Vandermonde",
        "deg P'=p-m-1",
        "`m+1` distinct roots",
        "G(T)=(T-gamma)^m+delta",
        "R(Z)=Z^u S(Z^m)",
    ):
        assert anchor in proof
        checks += 1

    assert "for every actual split-value degree" in contract
    assert "growing exponent" in contract
    assert "binom(u,ell_h)" in contract
    assert "No Modal run" in (NODE / "lineage.md").read_text()
    assert "Lower split-value degrees" in audit
    checks += 5

    print(f"L1_OFFICIAL_MAX_SPLIT_VALUE_COMPLEMENT_CENSUS_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
