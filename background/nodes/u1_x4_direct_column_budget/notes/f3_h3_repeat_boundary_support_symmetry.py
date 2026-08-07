#!/usr/bin/env python3
"""Verify the repeat-boundary support S3 symmetry ledger."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table


def mobius_orbit(r: int, p: int) -> set[int]:
    if r in (0, p - 1):
        raise ValueError((p, r))
    return {
        r % p,
        pow(r, -1, p),
        (-r * pow((r + 1) % p, -1, p)) % p,
        (-(r + 1) * pow(r, -1, p)) % p,
        (-(r + 1)) % p,
        (-pow((r + 1) % p, -1, p)) % p,
    }


def active_support(p: int, n: int) -> set[int]:
    hset = set(root_table(p, n))
    support: set[int] = set()
    for r in range(p):
        if r in (0, p - 1):
            continue
        inv_r1 = pow((r + 1) % p, -1, p)
        c3 = (-r * inv_r1) % p
        c4 = ((r * r + r + 1) * inv_r1) % p
        if (r * r + r + 1) % p == 0:
            continue
        for t in range(1, p):
            v = (1 + t) % p
            u = (1 + r * t) % p
            w = (1 + c3 * t) % p
            lam = (1 + c4 * t) % p
            if v not in hset or u not in hset or w not in hset or lam not in hset:
                continue
            if len({u, v, w}) != 3:
                continue
            support.add(r)
            break
    return support


def verify_row(p: int, n: int) -> dict[str, int]:
    support = active_support(p, n)
    seen: set[int] = set()
    orbits = 0
    for r in sorted(support):
        orbit = mobius_orbit(r, p)
        if len(orbit) != 6:
            raise AssertionError((p, n, r, orbit))
        if not orbit <= support:
            raise AssertionError((p, n, r, orbit - support))
        if r not in seen:
            seen |= orbit
            orbits += 1
    if seen != support:
        raise AssertionError((p, n, len(seen), len(support)))
    if len(support) != 6 * orbits:
        raise AssertionError((p, n, len(support), orbits))
    return {"support": len(support), "orbits": orbits}


def main() -> None:
    print("h=3 repeat-boundary support S3 symmetry")
    for p, n in ((97, 16), (97, 32), (193, 64), (257, 128)):
        row = verify_row(p, n)
        print(
            f"p={p} n={n} genuine_support={row['support']} "
            f"s3_orbits={row['orbits']}"
        )
    print("non-q0 active support is a union of six-element S3 Mobius orbits")
    print("H3_REPEAT_BOUNDARY_SUPPORT_SYMMETRY_PASS")


if __name__ == "__main__":
    main()
