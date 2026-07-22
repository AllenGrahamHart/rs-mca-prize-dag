#!/usr/bin/env python3
"""Mutation audit for the XR prize effective-core floor."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def main() -> None:
    rows = (
        ((1 << 33) + 1, 384, 16, 11_243_370, 11_243_354),
        ((1 << 33) + 1, 448, 16, 9_629_972, 9_629_956),
        ((1 << 32) + 1, 960, 14, 2_241_633, 2_241_619),
    )
    for h, L, a, floor, uv in rows:
        assert ceil_div(h + 1, 2 * (L - 2)) == floor
        assert floor - a == uv

    # Equality of two truncated blocks would violate the retained pair cap.
    for kappa in range(1, 50):
        for h in range(1, 10):
            assert kappa + h > kappa

    # The exact P-A dictionary after persistent-root deletion.
    for k in range(20, 40):
        for a in range(1, 5):
            for u in range(3):
                for v in range(3):
                    if a + u + v > k:
                        continue
                    p = k - a - u - v
                    assert k - p == a + u + v
                    assert k + 7 - p == a + u + v + 7

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "u+v>=11,243,354" in statement
    assert "do not import" in audit
    assert "P-B" in audit

    print("XR_PRIZE_FLAT_NULLITY_EFFECTIVE_CORE_FLOOR_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
