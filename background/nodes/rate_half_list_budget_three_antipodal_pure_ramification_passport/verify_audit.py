#!/usr/bin/env python3
"""Audit the official arithmetic and nonclaims of the passport theorem."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_ramification_passport"


def defect(parts: list[tuple[int, int]]) -> int:
    return sum(count * (size - 1) for size, count in parts)


def size(parts: list[tuple[int, int]]) -> int:
    return sum(count * value for value, count in parts)


def official_profile_check() -> None:
    r = (1 << 37) - 1
    d = 1 << 39
    degree = d - 4
    assert degree == 4 * r

    zero = [(3, r), (1, r)]
    pole = [(3, r - 1), (1, r + 3)]
    one = [(degree, 1)]
    extra = [(2, 1), (1, degree - 2)]
    u_collision = [(4, 1), (3, r - 1), (1, r - 1)]
    double_t = [(3, r), (2, 1), (1, r - 2)]
    v_collision = [(4, 1), (3, r - 2), (1, r + 2)]
    double_c = [(3, r - 1), (2, 1), (1, r + 1)]

    for profile in (
        zero,
        pole,
        one,
        extra,
        u_collision,
        double_t,
        v_collision,
        double_c,
    ):
        assert size(profile) == degree

    total = defect(zero) + defect(pole) + defect(one) + defect(extra)
    assert total == 2 * degree - 2
    assert defect(u_collision) + defect(pole) + defect(one) == total
    assert defect(double_t) + defect(pole) + defect(one) == total
    assert defect(zero) + defect(v_collision) + defect(one) == total
    assert defect(zero) + defect(double_c) + defect(one) == total


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "exclusive and exhaustive" in statement
    assert "does not classify covers" in statement
    assert "no passport is declared empty" in contract
    assert "No Modal or other remote computation was used" in audit


def main() -> None:
    official_profile_check()
    scope_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_RAMIFICATION_PASSPORT_AUDIT_PASS "
        "official=1 cases=5 tame_scope=kept nonclaim=kept"
    )


if __name__ == "__main__":
    main()
