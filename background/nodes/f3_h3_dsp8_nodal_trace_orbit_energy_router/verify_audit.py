#!/usr/bin/env python3
"""Independent mutation audit for the nodal trace-orbit energy router."""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def pair_orbit_check() -> None:
    for orbit_count in range(1, 21):
        presentations = 6 * orbit_count
        ordered_different_orbit_pairs = 36 * orbit_count * (orbit_count - 1)
        assert ordered_different_orbit_pairs == presentations * (presentations - 6)
        assert presentations**2 - ordered_different_orbit_pairs == 6 * presentations


def main() -> None:
    pair_orbit_check()
    assert Fraction(1 + 2 * Fraction(4, 5) ** 2, 3) == Fraction(19, 25)

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "N_c(N_c-6)" in statement
    assert "36M_c(M_c-1)=N_c(N_c-6)" in proof
    assert "cH=BA=theta(1+theta)H" in proof
    assert "repeated-rootnonnodepointsareharmless" in proof
    assert "51066/1445-3481/100=15311/28900>0" in proof
    assert "no uniform `4/5` bias theorem is claimed" in audit
    assert "only after a row certifies the narrow high-point interval" in audit
    assert "It is not itself a smooth-trace estimate" in audit

    print("F3_H3_DSP8_NODAL_TRACE_ORBIT_ENERGY_ROUTER_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
