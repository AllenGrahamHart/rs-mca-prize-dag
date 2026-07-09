#!/usr/bin/env python3
"""Exception ledger for the h=3 repeat-boundary LP4 line-pencil gate."""

from __future__ import annotations


Q0_RESIDUE_CONSTANT = 1584
OFFICIAL_MIN_N = 2**13


def coefficient_collision_parameters(p: int) -> set[int]:
    if p in (2, 3):
        raise AssertionError("LP4 exception ledger assumes characteristic not 2 or 3")
    inv2 = pow(2, -1, p)
    return {0, (-1) % p, 1, (-inv2) % p, (-2) % p}


def observed_coefficient_collisions(p: int) -> set[int]:
    observed: set[int] = set()
    for r in range(p):
        if (r + 1) % p == 0:
            observed.add(r)
            continue
        c1 = 1
        c2 = r
        c3 = (-r * pow((r + 1) % p, -1, p)) % p
        if len({c1, c2, c3}) != 3:
            observed.add(r)
    return observed


def q0_roots(p: int) -> set[int]:
    return {r for r in range(p) if (r * r + r + 1) % p == 0}


def verify_finite_fields() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 97)
    q0_max = 0
    for p in primes:
        expected = coefficient_collision_parameters(p)
        observed = observed_coefficient_collisions(p)
        if observed != expected:
            raise AssertionError((p, observed, expected))
        q0 = q0_roots(p)
        if len(q0) > 2:
            raise AssertionError((p, q0))
        if q0 & expected:
            raise AssertionError((p, q0, expected, "q0 should be separate from coefficient collisions"))
        q0_max = max(q0_max, len(q0))
    return {"primes": len(primes), "q0_max": q0_max}


def q0_residue_paid(n: int) -> bool:
    # (1584*n^(5/3) < n^3)^3 is 1584^3*n^5 < n^9.
    return Q0_RESIDUE_CONSTANT**3 * n**5 < n**9


def main() -> None:
    print("h=3 repeat LP4 exception ledger")
    print("coefficient collisions among 1, r, -r/(r+1):")
    print("  r in {0, -1, 1, -1/2, -2}")
    print("  r=0 and r=-1 are invalid; r=1,-1/2,-2 force duplicate u,v,w")
    print("q0 cell: r^2+r+1=0, paid separately by B_q0 <= 132*n^(2/3)")
    guardrails = verify_finite_fields()
    print(
        f"finite_guardrails: primes={guardrails['primes']} "
        f"q0_roots_max={guardrails['q0_max']}"
    )
    official_ns = [2**s for s in range(13, 42)]
    bad = [n for n in official_ns if not q0_residue_paid(n)]
    if bad:
        raise AssertionError(("q0 residue payment failed official range", bad[:5]))
    print(
        "q0 residue contribution 1584*n^(5/3) is below n^3 "
        f"for official n=2^13..2^41; first_n={OFFICIAL_MIN_N}"
    )
    print("H3_REPEAT_LP4_EXCEPTION_LEDGER_PASS")


if __name__ == "__main__":
    main()
