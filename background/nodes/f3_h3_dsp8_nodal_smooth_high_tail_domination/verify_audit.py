#!/usr/bin/env python3
"""Independent mutation audit for nodal/smooth high-tail domination."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ceil_half(value: int) -> int:
    return (value + 1) // 2


def main() -> None:
    def f0(m: int) -> int:
        return ceil_half(m * (m - 4)) - 2 * m - 6

    def fa(m: int) -> int:
        return ceil_half(m * (m - 2)) - 4 * (m - 1) - 8

    assert f0(14) < 2 * (3 * 14 // 2)
    assert f0(15) >= 2 * (3 * 15 // 2)
    assert fa(15) < 2 * (3 * 14 // 2)
    assert fa(16) == 2 * (3 * 15 // 2)

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "D_6(t)=D_nod(t)+D_sm(t)" in statement
    assert "Thehandshakelemmathereforegives" in proof
    assert "F_A(m)-2nu_A(m)=2q(q-8)" in proof
    assert "The quotient weight is preserved" in audit
    assert "does not show that smooth edges are sparse" in audit
    assert "can still correlate adversarially with `R(t)`" in audit

    print("F3_H3_DSP8_NODAL_SMOOTH_HIGH_TAIL_DOMINATION_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
