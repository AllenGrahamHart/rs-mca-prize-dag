#!/usr/bin/env python3
"""Audit the finite h=5 certificate coverage banked for F3/T4.

This verifier does not run a new search.  It treats the existing JSON
certificates as pinned data, checks their internal consistency, and prints the
exact finite-row coverage they currently provide.
"""

from __future__ import annotations

import json
from pathlib import Path


NOTES = Path(__file__).resolve().parent

EXPECTED_PRIMES = {
    32: [
        1153,
        1217,
        1249,
        1409,
        1601,
        1697,
        1889,
        2017,
        2081,
        2113,
        2273,
        2593,
        2657,
        2689,
        2753,
        3041,
        3137,
        3169,
        3329,
        3361,
        3457,
        3617,
        4001,
        4129,
        4289,
        4481,
        4513,
        4673,
        4801,
        4993,
        5153,
        5281,
        5441,
        5569,
        5857,
        5953,
        6113,
        6337,
        6529,
        6689,
        6977,
        7297,
        7393,
        7457,
        7489,
        7649,
        7681,
        7841,
        7873,
        7937,
        8161,
        12289,
        32801,
        40961,
        61441,
        65537,
    ],
    64: [4289, 12289, 40961, 65537, 262337],
    96: [9601],
    128: [17921, 18049, 18433, 19073, 19457, 19841, 20353],
}


def load_json(name: str):
    return json.loads((NOTES / name).read_text())


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    # Deterministic for n < 2^64.
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def admissible_primes(n: int, hi: int) -> list[int]:
    lo = n * n
    return [p for p in range(lo + 1, hi + 1) if (p - 1) % n == 0 and is_prime(p)]


def require_zero_common(row: dict, n: int, p: int) -> None:
    expected = {
        "n": n,
        "h": 5,
        "W": n,
        "p": p,
        "anchored_toral_trades": 0,
        "anchored_nontoral_trades": 0,
        "direct_n3_budget": n**3,
        "direct_n3_exceeded": False,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    if (p - 1) % n != 0:
        raise AssertionError((n, p, "p is not 1 mod n"))
    if p <= n * n:
        raise AssertionError((n, p, "p is not above n^2"))
    if not is_prime(p):
        raise AssertionError((n, p, "p is not prime"))


def require_complete_unsharded(row: dict, n: int, p: int) -> None:
    require_zero_common(row, n, p)
    if row.get("complete") is not True or row.get("partial") is not False:
        raise AssertionError(row)


def require_complete_sharded(row: dict, n: int, p: int) -> None:
    require_zero_common(row, n, p)
    expected = {
        "complete": True,
        "partial": False,
        "shards": 32,
        "shards_completed": 32,
        "hashed_per_shard": 10334625,
        "probed": 254231775,
    }
    for key, value in expected.items():
        if row.get(key) != value:
            raise AssertionError((key, row.get(key), value, row))
    shards = row.get("rows")
    if not isinstance(shards, list) or len(shards) != 32:
        raise AssertionError(row)
    if [shard.get("shard") for shard in shards] != list(range(32)):
        raise AssertionError(shards)
    if sum(shard.get("probed", 0) for shard in shards) != row["probed"]:
        raise AssertionError(row)
    for shard in shards:
        require_zero_common(shard, n, p)
        if shard.get("complete") is not False or shard.get("partial") is not True:
            raise AssertionError(shard)
        if shard.get("shards") != row["shards"]:
            raise AssertionError(shard)
        if shard.get("hashed") != row["hashed_per_shard"]:
            raise AssertionError(shard)


def certificate_rows() -> dict[int, list[dict]]:
    n32 = load_json("f3_h5_n32_multirow_certificate.json")
    n64 = load_json("f3_h5_n64_multirow_certificate.json")
    n96 = [load_json("f3_h5_n96_boundary_certificate.json")]
    n128 = [load_json("f3_h5_n128_boundary_certificate.json")]
    n128.extend(load_json("f3_h5_n128_extra_primes_certificate.json"))
    return {32: n32, 64: n64, 96: n96, 128: n128}


def audit() -> list[dict]:
    summaries = []
    for n, rows in certificate_rows().items():
        primes = [row.get("p") for row in rows]
        if primes != EXPECTED_PRIMES[n]:
            raise AssertionError((n, primes, EXPECTED_PRIMES[n]))
        for row in rows:
            if n == 128:
                require_complete_sharded(row, n, row["p"])
            else:
                require_complete_unsharded(row, n, row["p"])
        admissible_to_max = admissible_primes(n, max(primes))
        missing = [p for p in admissible_to_max if p not in set(primes)]
        summaries.append(
            {
                "n": n,
                "certified_primes": len(primes),
                "first_certified_prime": min(primes),
                "max_certified_prime": max(primes),
                "admissible_primes_to_max": len(admissible_to_max),
                "missing_admissible_primes_to_max": len(missing),
                "total_right_probes": sum(row["probed"] for row in rows),
            }
        )
    return summaries


def main() -> None:
    summaries = audit()
    print("h=5 certificate coverage audit")
    print(" n  cert  first_p  max_p   admiss<=max  missing<=max  right_probes")
    total_rows = 0
    total_probes = 0
    for row in summaries:
        total_rows += row["certified_primes"]
        total_probes += row["total_right_probes"]
        print(
            f"{row['n']:3d} {row['certified_primes']:5d} "
            f"{row['first_certified_prime']:8d} {row['max_certified_prime']:7d} "
            f"{row['admissible_primes_to_max']:12d} "
            f"{row['missing_admissible_primes_to_max']:12d} "
            f"{row['total_right_probes']:13d}"
        )
    print(f"total certified zero rows: {total_rows}")
    print(f"total right-side probes: {total_probes}")
    print("H5_CERTIFICATE_COVERAGE_AUDIT_PASS")


if __name__ == "__main__":
    main()
