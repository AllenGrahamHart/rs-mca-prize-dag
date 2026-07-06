#!/usr/bin/env python3
"""Bounded active-core probe for the weakened X4 use of U1.

The full U1 node asks for a broad pullback-compression theorem.  The X4
consumer only needs the fully stripped primitive exact-list residue to fit the
direct row budget.  This probe stress-tests that weaker premise by counting
anchored same-moment trades in small subgroup rows and capped windows.

It is a falsifier harness, not a proof.  Complete rows give exact local counts;
capped rows can only find excess mass or active-core witnesses.
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "u1_x4_active_core_budget_results.json"

SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in SMALL_PRIMES:
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in SMALL_PRIMES:
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def next_prime_1mod(n: int, start: int) -> int:
    t = max(1, (start - 1) // n)
    while True:
        p = 1 + n * t
        if p >= start and is_prime(p):
            return p
        t += 1


def mu_n_generator(p: int, n: int) -> int:
    if (p - 1) % n:
        raise ValueError(f"p={p} is not 1 mod n={n}")
    exponent = (p - 1) // n
    a = 2
    while True:
        z = pow(a, exponent, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            return z
        a += 1


def elementary_signature(exps: tuple[int, ...], powers: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
    coeffs = [1] + [0] * h
    for a in exps:
        root = powers[a]
        for j in range(h, 0, -1):
            coeffs[j] = (coeffs[j] - root * coeffs[j - 1]) % p
    first = tuple(((-coeffs[j]) % p if j & 1 else coeffs[j]) for j in range(1, h))
    last = (-coeffs[h]) % p if h & 1 else coeffs[h]
    return first, last


def is_coset(exps: tuple[int, ...], h: int, n: int) -> bool:
    if n % h:
        return False
    step = n // h
    residue = exps[0] % step
    return sorted(exps) == sorted((residue + j * step) % n for j in range(h))


def pack_exps(exps: tuple[int, ...]) -> int:
    value = 0
    for a in exps:
        value = (value << 11) | a
    return value


def unpack_exps(value: int, count: int) -> tuple[int, ...]:
    out = []
    for _ in range(count):
        out.append(value & 0x7FF)
        value >>= 11
    return tuple(reversed(out))


def full_census(n: int, h: int, p: int) -> dict[str, Any]:
    zeta = mu_n_generator(p, n)
    powers = [pow(zeta, a, p) for a in range(n)]
    buckets: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = {}
    for exps in itertools.combinations(range(n), h):
        sig, last = elementary_signature(exps, powers, p, h)
        buckets.setdefault(sig, []).append((exps, last))

    unordered = 0
    toral = 0
    nontoral = 0
    anchored_cores: set[tuple[int, ...]] = set()
    for entries in buckets.values():
        if len(entries) < 2:
            continue
        for i, (left, left_last) in enumerate(entries):
            left_set = set(left)
            for right, right_last in entries[i + 1 :]:
                if left_set & set(right):
                    continue
                if left_last == right_last:
                    continue
                unordered += 1
                if is_coset(left, h, n) and is_coset(right, h, n):
                    toral += 1
                else:
                    nontoral += 1
                if 0 in left:
                    anchored_cores.add(left)
                if 0 in right:
                    anchored_cores.add(right)
    return {
        "n": n,
        "h": h,
        "p": p,
        "unordered_trades": unordered,
        "toral": toral,
        "nontoral": nontoral,
        "anchored_cores": len(anchored_cores),
    }


def anchored_mitm(row: dict[str, Any], deadline: float) -> dict[str, Any]:
    n = row["n"]
    h = row["h"]
    p = row["p"]
    window = min(row.get("W", n), n)
    zeta = mu_n_generator(p, n)
    powers = [pow(zeta, a, p) for a in range(n)]
    started = time.monotonic()
    partial = False

    table: dict[tuple[int, ...], int | list[int]] = {}
    hashed = 0
    for tail in itertools.combinations(range(1, window), h - 1):
        if hashed & 0x3FFF == 0 and time.monotonic() >= deadline:
            partial = True
            break
        exps = (0,) + tail
        sig, _ = elementary_signature(exps, powers, p, h)
        packed = pack_exps(tail)
        current = table.get(sig)
        if current is None:
            table[sig] = packed
        elif isinstance(current, int):
            table[sig] = [current, packed]
        else:
            current.append(packed)
        hashed += 1

    probed = 0
    anchored_toral = 0
    anchored_nontoral = 0
    nontoral_cores: set[tuple[int, ...]] = set()
    witnesses: list[dict[str, list[int]]] = []
    if not partial:
        for right in itertools.combinations(range(1, window), h):
            if probed & 0x3FFF == 0 and time.monotonic() >= deadline:
                partial = True
                break
            sig, right_last = elementary_signature(right, powers, p, h)
            packed = table.get(sig)
            if packed is not None:
                packed_items = packed if isinstance(packed, list) else [packed]
                right_set = set(right)
                for packed_tail in packed_items:
                    left = (0,) + unpack_exps(packed_tail, h - 1)
                    if set(left) & right_set:
                        continue
                    _, left_last = elementary_signature(left, powers, p, h)
                    if left_last == right_last:
                        continue
                    if is_coset(left, h, n) and is_coset(right, h, n):
                        anchored_toral += 1
                    else:
                        anchored_nontoral += 1
                        nontoral_cores.add(left)
                        if len(witnesses) < 8:
                            witnesses.append({"P": list(left), "Q": list(right)})
            probed += 1

    complete = (window == n) and not partial
    strict_hn = h * n
    n2_budget = n * n
    n3_budget = n**3
    return {
        "name": row["name"],
        "n": n,
        "h": h,
        "p": p,
        "W": window,
        "complete": complete,
        "partial": partial,
        "hashed": hashed,
        "probed": probed,
        "total_hash_subsets": comb(window - 1, h - 1),
        "total_probe_subsets": comb(window - 1, h),
        "anchored_toral_trades": anchored_toral,
        "anchored_nontoral_trades": anchored_nontoral,
        "anchored_nontoral_cores": len(nontoral_cores),
        "old_hn_budget": strict_hn,
        "old_hn_exceeded": anchored_nontoral > strict_hn,
        "old_n2_budget": n2_budget,
        "old_n2_exceeded": anchored_nontoral > n2_budget,
        "direct_n3_budget": n3_budget,
        "direct_n3_exceeded": anchored_nontoral > n3_budget,
        "witnesses": witnesses,
        "wall_seconds": round(time.monotonic() - started, 6),
    }


def planned_rows() -> list[dict[str, Any]]:
    return [
        {"name": "exceptional_control_n16_h4_p17", "n": 16, "h": 4, "p": 17, "W": 16},
        {"name": "clean_q2_n16_h4", "n": 16, "h": 4, "p": next_prime_1mod(16, 16**2), "W": 16},
        {"name": "boundary_n32_h5_p1153", "n": 32, "h": 5, "p": 1153, "W": 32},
        {"name": "q3_n32_h5", "n": 32, "h": 5, "p": next_prime_1mod(32, 32**3), "W": 32},
        {"name": "boundary_n32_h6_p1153", "n": 32, "h": 6, "p": 1153, "W": 32},
        {"name": "boundary_n32_h7_p1153_slice28", "n": 32, "h": 7, "p": 1153, "W": 28},
        {"name": "boundary_n32_h8_p1153_slice24", "n": 32, "h": 8, "p": 1153, "W": 24},
        {"name": "q2_n64_h7_slice28", "n": 64, "h": 7, "p": next_prime_1mod(64, 64**2), "W": 28},
        {"name": "q3_n64_h8_slice26", "n": 64, "h": 8, "p": next_prime_1mod(64, 64**3), "W": 26},
    ]


def run(time_limit: float) -> dict[str, Any]:
    started = time.monotonic()
    deadline = started + time_limit
    gates = [
        {
            "name": "gate_full_n16_h3_p17",
            "result": full_census(16, 3, 17),
            "expect": {"unordered_trades": 352},
        },
        {
            "name": "gate_full_n16_h3_p97",
            "result": full_census(16, 3, 97),
            "expect": {"unordered_trades": 16},
        },
        {
            "name": "gate_full_n16_h4_p17",
            "result": full_census(16, 4, 17),
            "expect": {"nontoral": 120, "toral": 6},
        },
        {
            "name": "gate_full_n32_h5_p97",
            "result": full_census(32, 5, 97),
            "expect": {"unordered_trades": 96},
        },
    ]
    gate_failures = []
    for gate in gates:
        for key, expected in gate["expect"].items():
            got = gate["result"][key]
            if got != expected:
                gate_failures.append({"gate": gate["name"], "key": key, "expected": expected, "got": got})

    rows = []
    if not gate_failures:
        for row in planned_rows():
            if time.monotonic() >= deadline:
                break
            rows.append(anchored_mitm(row, deadline))

    direct_alarms = [r for r in rows if r["direct_n3_exceeded"]]
    controls_detected = any(r["name"] == "exceptional_control_n16_h4_p17" and r["anchored_nontoral_trades"] > 0 for r in rows)
    strict_hn_excess = [r["name"] for r in rows if r["old_hn_exceeded"]]
    result = {
        "node": "u1_x4_direct_column_budget / x4_exactlist_staircase_split",
        "status": "PASS" if not gate_failures and controls_detected and not direct_alarms else "FAIL",
        "interpretation": (
            "No direct n^3 column excess found in complete small rows or capped windows; "
            "old hn/n^2 trophies are reported only as stronger-bound diagnostics."
        ),
        "gate_failures": gate_failures,
        "positive_control_detected": controls_detected,
        "rows": rows,
        "direct_n3_alarms": [
            {"name": r["name"], "anchored_nontoral_trades": r["anchored_nontoral_trades"], "budget": r["direct_n3_budget"]}
            for r in direct_alarms
        ],
        "strict_hn_excess_rows": strict_hn_excess,
        "rows_started": len(rows),
        "completed_rows": sum(1 for r in rows if r["complete"]),
        "window_slice_rows": sum(1 for r in rows if not r["complete"] and not r["partial"]),
        "partial_rows": sum(1 for r in rows if r["partial"]),
        "max_nontoral_to_n3_ratio": max(
            (r["anchored_nontoral_trades"] / r["direct_n3_budget"] for r in rows),
            default=0.0,
        ),
        "wall_seconds": round(time.monotonic() - started, 6),
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    args = parser.parse_args()
    result = run(args.time_limit)
    print(json.dumps({
        "status": result["status"],
        "rows_started": result["rows_started"],
        "completed_rows": result["completed_rows"],
        "window_slice_rows": result["window_slice_rows"],
        "partial_rows": result["partial_rows"],
        "max_nontoral_to_n3_ratio": result["max_nontoral_to_n3_ratio"],
        "positive_control_detected": result["positive_control_detected"],
        "direct_n3_alarms": result["direct_n3_alarms"],
        "strict_hn_excess_rows": result["strict_hn_excess_rows"],
        "wall_seconds": result["wall_seconds"],
    }, indent=2, sort_keys=True))
    if result["status"] == "PASS":
        print("PASS: active-core direct-column probe found no n^3 budget excess")
        return 0
    print("FAIL: active-core direct-column probe found a gate/control/direct-budget problem")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
