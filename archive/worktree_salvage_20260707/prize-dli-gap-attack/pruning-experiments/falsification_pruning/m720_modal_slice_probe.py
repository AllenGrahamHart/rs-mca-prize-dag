#!/usr/bin/env python3
"""Bounded Modal slice probe for M720 h=7..20 residual active cores.

This targets the current M720 manifest gap by searching for unpaid non-toral
anchored active cores in residual window slices.  A slice witness is not a
complete official certificate, but a non-toral witness would be a serious
falsification signal for the bounded-band exclusion strategy.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from math import comb
from pathlib import Path
from typing import Any

import modal


sys.dont_write_bytecode = True

APP_NAME = "rs-mca-m720-slice-probe-20260705"
DEFAULT_CONFIGS = (
    (64, 7, 2),
    (64, 7, 3),
    (128, 7, 2),
    (128, 7, 3),
    (128, 8, 2),
    (128, 8, 3),
    (128, 9, 2),
    (128, 10, 2),
)

app = modal.App(APP_NAME)


def parse_config(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("config must be n,h,q_exp")
    return tuple(map(int, parts))  # type: ignore[return-value]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


@app.function(image=modal.Image.debian_slim(), cpu=2, memory=2048, timeout=58)
def run_remote(configs: list[tuple[int, int, int]], count_ceiling: int, seconds: float) -> dict[str, Any]:
    started = time.time()
    deadline = started + seconds
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for q in small_primes:
            if m % q == 0:
                return m == q
        d = m - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for a in small_primes:
            x = pow(a, d, m)
            if x == 1 or x == m - 1:
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
        e = (p - 1) // n
        a = 2
        while True:
            z = pow(a, e, p)
            if pow(z, n // 2, p) != 1:
                return z
            a += 1

    def sig_general(exps: tuple[int, ...], powers: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
        coef = [1] + [0] * h
        for a in exps:
            r = powers[a]
            for j in range(h, 0, -1):
                coef[j] = (coef[j] - r * coef[j - 1]) % p
        e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
        e_h = (-coef[h]) % p if (h & 1) else coef[h]
        return e, e_h

    def is_coset(exps: tuple[int, ...], h: int, n: int) -> bool:
        if n % h:
            return False
        step = n // h
        r0 = exps[0] % step
        return sorted(exps) == sorted((r0 + j * step) % n for j in range(h))

    def pack(exps: tuple[int, ...]) -> int:
        out = 0
        for a in exps:
            out = (out << 11) | a
        return out

    def unpack(value: int, k: int) -> tuple[int, ...]:
        out = []
        for _ in range(k):
            out.append(value & 0x7FF)
            value >>= 11
        return tuple(reversed(out))

    def chosen_window(n: int, h: int) -> tuple[int, int]:
        best = 2 * h
        best_cost = comb(best - 1, h - 1) + comb(best, h)
        w = 2 * h
        while w <= n:
            cost = comb(w - 1, h - 1) + comb(w, h)
            if cost <= count_ceiling:
                best = w
                best_cost = cost
                w += 1
            else:
                break
        return best, best_cost

    def mitm_slice(n: int, h: int, p: int, w: int) -> dict[str, Any]:
        z = mu_n_generator(p, n)
        powers = [pow(z, a, p) for a in range(n)]
        cell_started = time.time()
        table: dict[tuple[int, ...], int | list[int]] = {}
        n_hash = 0
        n_probe = 0
        anchored_toral = 0
        anchored_nontoral = 0
        witnesses: list[dict[str, list[int]]] = []
        aborted = False

        for tri in itertools.combinations(range(1, w), h - 1):
            exps = (0,) + tri
            sig, _ = sig_general(exps, powers, p, h)
            packed = pack(tri)
            cur = table.get(sig)
            if cur is None:
                table[sig] = packed
            elif isinstance(cur, int):
                table[sig] = [cur, packed]
            else:
                cur.append(packed)
            n_hash += 1
            if (n_hash & 0x1FFF) == 0 and time.time() > deadline - 2:
                aborted = True
                break

        if not aborted:
            for q_exps in itertools.combinations(range(1, w), h):
                sig, e_h = sig_general(q_exps, powers, p, h)
                n_probe += 1
                packed = table.get(sig)
                if packed is not None:
                    for cand in (packed if isinstance(packed, list) else [packed]):
                        p_tail = unpack(cand, h - 1)
                        p_exps = (0,) + p_tail
                        p_sig, p_e_h = sig_general(p_exps, powers, p, h)
                        if p_sig != sig:
                            continue
                        if set(p_exps) & set(q_exps):
                            continue
                        if p_e_h == e_h:
                            continue
                        if is_coset(p_exps, h, n) and is_coset(q_exps, h, n):
                            anchored_toral += 1
                        else:
                            anchored_nontoral += 1
                            if len(witnesses) < 8:
                                witnesses.append({"P": list(p_exps), "Q": list(q_exps)})
                if (n_probe & 0x1FFF) == 0 and time.time() > deadline - 2:
                    aborted = True
                    break

        return {
            "n": n,
            "h": h,
            "p": p,
            "W": w,
            "complete": w == n and not aborted,
            "aborted": aborted,
            "n_hash": n_hash,
            "n_probe": n_probe,
            "anchored_toral": anchored_toral,
            "anchored_nontoral": anchored_nontoral,
            "witnesses": witnesses,
            "elapsed_seconds": time.time() - cell_started,
        }

    rows = []
    for n, h, q_exp in configs:
        if time.time() > deadline - 2:
            break
        if n < 2 * h:
            rows.append({"n": n, "h": h, "q_exp": q_exp, "skipped": "n_lt_2h"})
            continue
        p = next_prime_1mod(n, n**q_exp)
        w, cost = chosen_window(n, h)
        row = mitm_slice(n, h, p, w)
        row["q_exp"] = q_exp
        row["combination_cost"] = cost
        rows.append(row)
        if row["anchored_nontoral"]:
            break

    falsifiers = [r for r in rows if r.get("anchored_nontoral", 0) > 0]
    aborted = [r for r in rows if r.get("aborted")]
    return {
        "node": "m720_official_norm_gate_case_manifest_payload",
        "obligation_attacked": "residual h=7..20 window-slice unpaid non-toral active-core search",
        "scope": "calibration/window-slice evidence only; not complete official manifest",
        "app_name": APP_NAME,
        "count_ceiling": count_ceiling,
        "requested_configs": [list(c) for c in configs],
        "rows": rows,
        "elapsed_seconds": time.time() - started,
        "verdict": (
            "SLICE_FALSIFIER_NONTORAL_ACTIVE_CORE_FOUND"
            if falsifiers
            else "NO_NONTORAL_SLICE_WITNESS_FOUND"
            if not aborted
            else "TIME_BUDGET_PARTIAL_NO_NONTORAL_FOUND"
        ),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    configs = args.config or list(DEFAULT_CONFIGS)
    initial = {
        "node": "m720_official_norm_gate_case_manifest_payload",
        "obligation_attacked": "residual h=7..20 window-slice unpaid non-toral active-core search",
        "verdict": "RUNNING",
        "requested_configs": [list(c) for c in configs],
    }
    write_json(args.output, initial)
    with app.run():
        result = run_remote.remote(configs, args.count_ceiling, args.seconds)
    write_json(args.output, result)
    return result


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=50.0)
    parser.add_argument("--count-ceiling", type=int, default=1_500_000)
    parser.add_argument("--config", action="append", type=parse_config)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/m720_modal_slice_probe.json"),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
