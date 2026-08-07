#!/usr/bin/env python3
"""Shifted reciprocal normal form for h=3 repeat-boundary edges."""

from __future__ import annotations

from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


ROWS = (
    (97, 16),
    (97, 32),
    (193, 64),
    (337, 16),
    (2017, 32),
    (65537, 256),
    (91393, 256),
)


def verify_row(p: int, n: int) -> dict[str, int]:
    triples = active_ordered_triples(p, n)
    for u, v, w, lam in triples:
        x = (u - 1) % p
        y = (v - 1) % p
        z = (w - 1) % p
        if 0 in (x, y, z):
            raise AssertionError((p, n, "zero shifted coordinate", (u, v, w)))
        if (x * y + x * z + y * z) % p:
            raise AssertionError((p, n, "reciprocal equation failed", (u, v, w)))
        if (1 + x + y + z) % p != lam:
            raise AssertionError((p, n, "lambda shift failed", (u, v, w, lam)))
        denom = (x + y) % p
        if denom == 0:
            raise AssertionError((p, n, "unexpected vertical denominator", (u, v, w)))
        expected_z = (-x * y * pow(denom, -1, p)) % p
        if z != expected_z:
            raise AssertionError((p, n, "w reconstruction failed", (u, v, w)))
    return {"b_line": len(triples)}


def main() -> None:
    print("h=3 repeat edge reciprocal form")
    for p, n in ROWS:
        row = verify_row(p, n)
        print(f"p={p} n={n} B_line={row['b_line']} reciprocal_form=1")
    print("Active edges satisfy xy+xz+yz=0 for x=u-1,y=v-1,z=w-1")
    print("H3_REPEAT_EDGE_RECIPROCAL_FORM_PASS")


if __name__ == "__main__":
    main()
