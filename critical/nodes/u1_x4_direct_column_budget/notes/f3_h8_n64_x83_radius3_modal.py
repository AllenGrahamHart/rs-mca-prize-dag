#!/usr/bin/env python3
"""Modal-sharded radius-three x83 shell around paid h=8 n=64 lifts.

The radius-one and radius-two shells are light enough locally.  Radius three
contains about 67.8M preimage candidates per prime, so this script shards over
the paid-support/removed-triple pairs and keeps each Modal worker below the
60-second light-compute cap.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

import modal


app = modal.App("rs-mca-f3-h8-n64-x83-radius3")
image = modal.Image.debian_slim()

ROOT = Path(os.environ.get(
    "F3_PRIZE_ROOT",
    "/home/u2470931/smooth-read-solomin/prize-codex-overnight-20260708",
))
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
OUT_ENV = os.environ.get(
    "F3_H8_RADIUS3_OUT",
    "f3_h8_n64_x83_radius3_shell_certificate.json",
)
OUT = Path(OUT_ENV)
if not OUT.is_absolute():
    OUT = NOTES / OUT

N = 64
H = 8
RADIUS = 3
DEFAULT_CHUNK_PAIRS = 20


def make_jobs(primes: tuple[int, ...], chunk_pairs: int) -> list[dict]:
    total_pairs = 7 * math.comb(16, RADIUS)
    jobs = []
    for p in primes:
        for start in range(0, total_pairs, chunk_pairs):
            jobs.append(
                {
                    "p": p,
                    "pair_start": start,
                    "pair_end": min(start + chunk_pairs, total_pairs),
                    "total_pairs": total_pairs,
                }
            )
    return jobs


@app.function(image=image, cpu=2, memory=1024, timeout=60)
def scan_radius3_job(job: dict) -> dict:
    import itertools
    import time

    def prime_factors(n: int) -> list[int]:
        out = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                out.append(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            out.append(n)
        return out

    def primitive_root(p: int) -> int:
        factors = prime_factors(p - 1)
        g = 2
        while any(pow(g, (p - 1) // r, p) == 1 for r in factors):
            g += 1
        return g

    def root_table(p: int, n: int) -> list[int]:
        z = pow(primitive_root(p), (p - 1) // n, p)
        if pow(z, n, p) != 1 or pow(z, n // 2, p) == 1:
            raise AssertionError((p, n, z))
        return [pow(z, i, p) for i in range(n)]

    def elementary_signature(exponents: tuple[int, ...], vals: list[int], p: int) -> tuple[int, ...]:
        coeffs = [1]
        for exponent in exponents:
            x = vals[exponent]
            coeffs.append(0)
            for i in range(len(coeffs) - 1, 0, -1):
                coeffs[i] = (coeffs[i] + coeffs[i - 1] * x) % p
        return tuple(coeffs[1:])

    def is_toral(exponents: tuple[int, ...], n: int, h: int) -> bool:
        if n % h:
            return False
        step = n // h
        residue = exponents[0] % step
        seen = set()
        for exponent in exponents:
            if exponent % step != residue:
                return False
            seen.add((exponent - residue) // step)
        return len(seen) == h

    def h4_anchored_trades(p: int) -> list[tuple[tuple[int, ...], tuple[int, ...], bool]]:
        vals = root_table(p, 32)
        lefts: dict[tuple[int, int, int], list[tuple[tuple[int, ...], int, bool]]] = {}
        for tail in itertools.combinations(range(1, 32), 3):
            left = (0,) + tail
            sig = elementary_signature(left, vals, p)
            lefts.setdefault(sig[:3], []).append((left, sig[3], is_toral(left, 32, 4)))

        out = []
        for right in itertools.combinations(range(1, 32), 4):
            sig = elementary_signature(right, vals, p)
            right_toral = is_toral(right, 32, 4)
            for left, last, left_toral in lefts.get(sig[:3], []):
                if set(left) & set(right):
                    continue
                if last == sig[3]:
                    continue
                out.append((left, right, left_toral and right_toral))
        return out

    def antipodal_lift(side: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(sorted(side + tuple(e + 32 for e in side)))

    def paid_lift_supports(p: int) -> list[tuple[int, ...]]:
        supports = []
        for left4, right4, paid in h4_anchored_trades(p):
            if not paid:
                continue
            support = tuple(sorted(set(antipodal_lift(left4)) | set(antipodal_lift(right4))))
            if len(support) != 16:
                raise AssertionError((p, support))
            supports.append(support)
        return sorted(set(supports))

    def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x == 0:
                continue
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
        return out

    def locator_from_exponents(exponents: tuple[int, ...], vals: list[int], p: int) -> list[int]:
        coeffs = [1]
        for exponent in exponents:
            root = vals[exponent]
            nxt = [0] * (len(coeffs) + 1)
            for i, coeff in enumerate(coeffs):
                nxt[i] = (nxt[i] - coeff * root) % p
                nxt[i + 1] = (nxt[i + 1] + coeff) % p
            coeffs = nxt
        return coeffs

    def square_shift_root(L: list[int], p: int, h: int) -> list[int]:
        inv2 = pow(2, -1, p)
        s = [0] * (h + 1)
        s[h] = 1
        for degree in range(2 * h - 1, h - 1, -1):
            unknown = degree - h
            known = 0
            lo = max(0, degree - h)
            hi = min(h, degree)
            for i in range(lo, hi + 1):
                j = degree - i
                if not (0 <= j <= h):
                    continue
                if i == unknown or j == unknown:
                    continue
                known = (known + s[i] * s[j]) % p
            s[unknown] = ((L[degree] - known) * inv2) % p
        return s

    def forced_obstructions(L: list[int], p: int, h: int) -> tuple[list[int], list[int], int]:
        S = square_shift_root(L, p, h)
        S2 = poly_mul(S, S, p)
        obs = [(S2[i] - L[i]) % p for i in range(1, h)]
        lam = (S2[0] - L[0]) % p
        return S, obs, lam

    def is_square_mod(a: int, p: int) -> bool:
        return a % p == 0 or pow(a, (p - 1) // 2, p) == 1

    p = int(job["p"])
    start = int(job["pair_start"])
    end = int(job["pair_end"])
    vals = root_table(p, N)
    bases = paid_lift_supports(p)
    pairs = []
    for base_index, support in enumerate(bases):
        for removed in itertools.combinations(support, RADIUS):
            pairs.append((base_index, support, removed))
    if len(pairs) != int(job["total_pairs"]):
        raise AssertionError((p, len(pairs), job["total_pairs"]))

    t0 = time.monotonic()
    processed = 0
    first_zero = 0
    full_zero = 0
    examples = []
    complete = True
    for _, support, removed in pairs[start:end]:
        support_set = set(support)
        outside = [e for e in range(N) if e not in support_set]
        reduced = support_set - set(removed)
        for added in itertools.combinations(outside, RADIUS):
            candidate = tuple(sorted(reduced | set(added)))
            L = locator_from_exponents(candidate, vals, p)
            _, obs, lam = forced_obstructions(L, p, H)
            processed += 1
            first_zero += int(obs[-1] == 0)
            if all(v == 0 for v in obs) and lam != 0 and is_square_mod(lam, p):
                full_zero += 1
                if len(examples) < 4:
                    examples.append(list(candidate))
        if time.monotonic() - t0 > 54.0:
            complete = False
            break

    return {
        "p": p,
        "radius": RADIUS,
        "pair_start": start,
        "pair_end": end,
        "processed": processed,
        "first_obstruction_zero": first_zero,
        "full_zero": full_zero,
        "examples": examples,
        "complete": complete,
        "elapsed_sec": time.monotonic() - t0,
    }


@app.local_entrypoint()
def main():
    mode = os.environ.get("F3_H8_RADIUS3_MODE", "gate")
    primes = tuple(
        int(item)
        for item in os.environ.get("F3_H8_RADIUS3_PRIMES", "262337").split(",")
        if item
    )
    chunk_pairs = int(os.environ.get("F3_H8_RADIUS3_CHUNK_PAIRS", str(DEFAULT_CHUNK_PAIRS)))
    jobs = make_jobs(primes, chunk_pairs)
    if mode != "full":
        jobs = jobs[: min(4, len(jobs))]

    results = []
    errors = []
    for item in scan_radius3_job.map(jobs, return_exceptions=True):
        if isinstance(item, Exception):
            errors.append(repr(item))
            print(f"SHARD_ERROR {item!r}")
            continue
        results.append(item)
        print(
            f"p={item['p']} pairs={item['pair_start']}:{item['pair_end']} "
            f"processed={item['processed']} full_zero={item['full_zero']} "
            f"first_zero={item['first_obstruction_zero']} "
            f"complete={item['complete']} elapsed={item['elapsed_sec']:.3f}s"
        )

    cert = {
        "name": "h8_n64_x83_radius3_shell",
        "mode": mode,
        "radius": RADIUS,
        "primes": list(primes),
        "chunk_pairs": chunk_pairs,
        "jobs_expected": len(jobs),
        "jobs_completed": len(results),
        "errors": errors,
        "rows": results,
    }
    cert["processed"] = sum(row["processed"] for row in results)
    cert["first_obstruction_zero"] = sum(row["first_obstruction_zero"] for row in results)
    cert["full_zero"] = sum(row["full_zero"] for row in results)
    cert["complete"] = (
        mode == "full"
        and not errors
        and len(results) == len(jobs)
        and all(row["complete"] for row in results)
        and cert["full_zero"] == 0
    )
    if mode == "full":
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
        print(f"wrote {OUT}")

    print(
        f"TOTAL mode={mode} jobs={len(results)}/{len(jobs)} "
        f"processed={cert['processed']} full_zero={cert['full_zero']} "
        f"first_zero={cert['first_obstruction_zero']}"
    )
    if cert["complete"]:
        print("H8_N64_X83_RADIUS3_SHELL_PASS")
    elif mode == "gate" and not errors and results and cert["full_zero"] == 0:
        print("H8_N64_X83_RADIUS3_GATE_PASS")
