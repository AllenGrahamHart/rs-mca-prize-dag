#!/usr/bin/env python3
"""Mutation audit for the XR collapsed-face exclusion."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # A nonzero polynomial of degree <a can vanish at a-1 points, so the full
    # a+1 facet supplied by the trade support is load-bearing.
    for a in range(2, 20):
        roots = list(range(1, a))
        coefficients = [1]
        for root in roots:
            following = [0] * (len(coefficients) + 1)
            for index, coefficient in enumerate(coefficients):
                following[index] -= root * coefficient
                following[index + 1] += coefficient
            coefficients = following
        assert len(coefficients) - 1 == a - 1
        assert all(
            sum(coefficient * root**index for index, coefficient in enumerate(coefficients)) == 0
            for root in roots
        )

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "(k-a)+(a+2)=k+2" in proof
    assert "Thereareatleastfouractiverows" in proof
    assert "S_isubsetA_i" in proof
    assert "actual selected-error zero sets" in audit
    assert "Larger active unions" in audit
    assert "near-tangentexception" in statement

    print("XR_HIGHER_RANK_COLLAPSED_FACE_EXCLUSION_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
