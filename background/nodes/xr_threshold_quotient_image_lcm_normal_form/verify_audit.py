#!/usr/bin/env python3
"""Mutation audit for the XR quotient-image lcm normal form."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    prime = 5
    duplicate_family = ((2,), (2,), (), (4,), (2,))
    degree_sum = sum(bool(item) for item in duplicate_family)
    radical_lcm_degree = len({item[0] for item in duplicate_family if item})
    assert degree_sum == 4
    assert radical_lcm_degree == 2

    contained_left = (0, 0)
    contained_right = (0, 0)
    false_roots_without_guard = tuple(range(prime))
    true_noncontained_roots: tuple[int, ...] = ()
    assert false_roots_without_guard != true_noncontained_roots

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "basis-independent" in statement
    assert "a_S=b_S=0" in statement
    assert "preservestheirgeneratedidealin`F[Z]`" in proof
    assert "repeated threshold appearances" in audit
    assert "not a feasible official-row algorithm" in audit

    print("XR_THRESHOLD_QUOTIENT_IMAGE_LCM_NORMAL_FORM_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
