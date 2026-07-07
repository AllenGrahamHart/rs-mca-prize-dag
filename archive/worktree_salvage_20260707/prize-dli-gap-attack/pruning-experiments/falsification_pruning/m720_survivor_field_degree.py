#!/usr/bin/env python3
"""Field-degree probe for known M720 non-toral calibration survivors.

The current m720_conductor_compression crux is survivor-conditioned descent:
for a non-toral survivor, does some nonzero obstruction live in a small enough
field to make the height/norm gate work?

The official h=7..20 cases do not have local survivor records.  This script
therefore attacks the nearest available object: the replayed small-h non-toral
calibration trades.  For each trade pair it computes Galois orbit degrees over
Q(zeta_n):

- degree of the e_h difference zeta^{sum A} - zeta^{sum B};
- degree of the unordered support union A union B;
- degree of the unordered pair {A,B}.

Large calibration degrees do not falsify the official h=7..20 statement, but
they do falsify any naive shortcut that known non-toral survivor structure is
automatically low-field.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_ROWS = (
    (16, 3, 17),
    (16, 3, 97),
    (16, 4, 17),
    (32, 5, 97),
    (128, 3, 17921),
)


def parse_row(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("rows must have form n,h,p")
    n, h, p = map(int, parts)
    if n <= 0 or h <= 0 or p <= 2 or (p - 1) % n != 0:
        raise argparse.ArgumentTypeError("need n,h,p with n|(p-1)")
    if n & (n - 1):
        raise argparse.ArgumentTypeError("this probe currently expects power-of-two n")
    return n, h, p


def mu_n_generator(p: int, n: int) -> int:
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def sig_general(exps: tuple[int, ...], pw: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
    coef = [1] + [0] * h
    for a in exps:
        r = pw[a]
        for j in range(h, 0, -1):
            coef[j] = (coef[j] - r * coef[j - 1]) % p
    e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
    e_h = (-coef[h]) % p if (h & 1) else coef[h]
    return e, e_h


def is_coset(A: tuple[int, ...], h: int, n: int) -> bool:
    if n % h:
        return False
    step = n // h
    r0 = A[0] % step
    return sorted(A) == sorted((r0 + j * step) % n for j in range(h))


def units_mod(n: int) -> list[int]:
    return [u for u in range(1, n) if math.gcd(u, n) == 1]


def canonical_power2_element(n: int, terms: dict[int, int]) -> tuple[tuple[int, int], ...]:
    """Canonical vector in the basis 1,zeta,...,zeta^{n/2-1} for n=2^r."""
    half = n // 2
    coeff = defaultdict(int)
    for exp, value in terms.items():
        exp %= n
        sign = 1
        if exp >= half:
            exp -= half
            sign = -1
        coeff[exp] += sign * value
    return tuple(sorted((e, c) for e, c in coeff.items() if c))


def transform_element(n: int, element: tuple[tuple[int, int], ...], u: int) -> tuple[tuple[int, int], ...]:
    return canonical_power2_element(n, {u * exp: coeff for exp, coeff in element})


def delta_element(n: int, A: tuple[int, ...], B: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    # e_h(A)-e_h(B), up to an irrelevant sign common to degree h.
    return canonical_power2_element(n, {sum(A): 1, sum(B): -1})


def transform_set(n: int, S: tuple[int, ...], u: int) -> tuple[int, ...]:
    return tuple(sorted((u * x) % n for x in S))


def transform_pair(n: int, A: tuple[int, ...], B: tuple[int, ...], u: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    Au = transform_set(n, A, u)
    Bu = transform_set(n, B, u)
    return tuple(sorted((Au, Bu)))  # type: ignore[return-value]


def orbit_size(items) -> int:
    return len(set(items))


def enumerate_trades(n: int, h: int, p: int) -> list[dict[str, Any]]:
    z = mu_n_generator(p, n)
    pw = [pow(z, a, p) for a in range(n)]
    buckets: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = {}
    for A in itertools.combinations(range(n), h):
        sig, eh = sig_general(A, pw, p, h)
        buckets.setdefault(sig, []).append((A, eh))

    trades: list[dict[str, Any]] = []
    for lst in buckets.values():
        if len(lst) < 2:
            continue
        for i, (Ai, ea) in enumerate(lst):
            sAi = set(Ai)
            for Bj, eb in lst[i + 1:]:
                if sAi & set(Bj):
                    continue
                if ea == eb:
                    continue
                toral = is_coset(Ai, h, n) and is_coset(Bj, h, n)
                trades.append({"A": Ai, "B": Bj, "toral": toral})
    return trades


def analyze_row(n: int, h: int, p: int, max_pairs: int | None = None) -> dict[str, Any]:
    started = time.time()
    trades = enumerate_trades(n, h, p)
    units = units_mod(n)
    rows = []
    delta_hist = Counter()
    union_hist = Counter()
    pair_hist = Counter()
    toral_count = 0
    nontoral_count = 0

    for idx, trade in enumerate(trades):
        if max_pairs is not None and idx >= max_pairs:
            break
        A = tuple(trade["A"])
        B = tuple(trade["B"])
        toral = bool(trade["toral"])
        toral_count += int(toral)
        nontoral_count += int(not toral)

        delta = delta_element(n, A, B)
        delta_degree = orbit_size(transform_element(n, delta, u) for u in units)
        union = tuple(sorted(set(A) | set(B)))
        union_degree = orbit_size(transform_set(n, union, u) for u in units)
        pair_degree = orbit_size(transform_pair(n, A, B, u) for u in units)

        delta_hist[delta_degree] += 1
        union_hist[union_degree] += 1
        pair_hist[pair_degree] += 1
        if len(rows) < 12:
            rows.append(
                {
                    "A": list(A),
                    "B": list(B),
                    "toral": toral,
                    "delta_field_degree": delta_degree,
                    "support_union_field_degree": union_degree,
                    "unordered_pair_field_degree": pair_degree,
                    "delta_element": list(delta),
                }
            )

    return {
        "n": n,
        "h": h,
        "p": p,
        "cyclotomic_degree_phi_n": len(units),
        "total_trades": len(trades),
        "analyzed_trades": toral_count + nontoral_count,
        "toral": toral_count,
        "nontoral": nontoral_count,
        "delta_field_degree_histogram": dict(sorted(delta_hist.items())),
        "support_union_field_degree_histogram": dict(sorted(union_hist.items())),
        "unordered_pair_field_degree_histogram": dict(sorted(pair_hist.items())),
        "sample_trades": rows,
        "elapsed_seconds": time.time() - started,
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    out: dict[str, Any] = {
        "node": "m720_conductor_compression",
        "obligation_attacked": "survivor-conditioned descent / obstruction field degree",
        "scope": "calibration-only known non-toral replay rows; not official h=7..20",
        "rows": [],
        "verdict": "RUNNING",
    }
    for n, h, p in args.row or DEFAULT_ROWS:
        if time.time() > deadline - 2:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        out["rows"].append(analyze_row(n, h, p, args.max_pairs))
        write_checkpoint(args.output, out)
    out["elapsed_seconds"] = time.time() - started
    out["verdict"] = "COMPLETE_CALIBRATION_DEGREE_STRESS"
    write_checkpoint(args.output, out)
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--row", action="append", type=parse_row)
    parser.add_argument("--max-pairs", type=int)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/m720_survivor_field_degree.json"),
    )
    return parser


def main() -> None:
    args = make_parser().parse_args()
    payload = run(args)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
