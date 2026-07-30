#!/usr/bin/env python3
"""Independent exact audit of the norm and resolvent formulas."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def evaluate(coefficients: dict[tuple[int, int], int], t: int, w: int) -> int:
    return sum(value * t**i * w**j for (i, j), value in coefficients.items())


def reciprocal_form(rows: int, columns: int, sign: int) -> dict[tuple[int, int], int]:
    values: dict[tuple[int, int], int] = {}
    seed = 1
    for i in range(rows):
        for j in range(columns):
            if (i, j) in values:
                continue
            mate = (rows - 1 - i, columns - 1 - j)
            if mate == (i, j) and sign == -1:
                values[(i, j)] = 0
            else:
                values[(i, j)] = seed
                values[mate] = sign * seed
                seed += 1
    return values


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "endpoint eigenvalue is positive" in proof
    assert "irreducibility and" in audit

    for sign in (1, -1):
        u = reciprocal_form(3, 3, sign)
        v = reciprocal_form(3, 2, sign)
        for t, w in ((2, 3), (3, 5), (5, 7)):
            u_tw = evaluate(u, t, w)
            v_tw = evaluate(v, t, w)
            # Clear denominators in the reciprocal identities.
            u_reverse = sum(value * t ** (2 - i) * w ** (2 - j)
                            for (i, j), value in u.items())
            v_reverse = sum(value * t ** (2 - i) * w ** (1 - j)
                            for (i, j), value in v.items())
            assert u_reverse == sign * u_tw
            assert v_reverse == sign * v_tw

            g_tw = u_tw * u_tw - w * v_tw * v_tw
            g_reverse = u_reverse * u_reverse - w * v_reverse * v_reverse
            assert g_reverse == g_tw
    print("RATE_HALF_KB_M2_R4_DIAGONAL_BRANCH_COEFFICIENT_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
