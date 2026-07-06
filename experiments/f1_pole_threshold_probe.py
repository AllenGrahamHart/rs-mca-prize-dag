#!/usr/bin/env python3
"""Exact arithmetic stress test for the F1 pole/list threshold import.

The critical amber lane

    f1_pole_list_threshold_location -> f1_case_pole -> f1_classification

uses the proved extension-pole floor

    N(L) = ceil( L (|F|-|B|) / (|F|-|B| + k L) ),   k = 2^40,

and reads the base list-window crossing through this numerator.  This script
does not prove the list adjacency theorem.  It attacks the arithmetic seam:
look for non-generating rows with |B| < 2^128 where N(L) crosses the MCA gate
too early, too late, or not at all.

All computations are exact Python integers and checkpointed.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "f1_pole_threshold_results.json"

EPS_BITS = 128
EPS_DEN = 1 << EPS_BITS
K_OFFICIAL = 1 << 40


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def pole_floor(L: int, F: int, B: int, k: int = K_OFFICIAL) -> int:
    X = F - B
    return ceil_div(L * X, X + k * L)


def gate_integer(F: int, eps_den: int = EPS_DEN) -> int:
    """Smallest integer N satisfying N > F / eps_den."""
    return F // eps_den + 1


def crosses(L: int, F: int, B: int, k: int = K_OFFICIAL) -> bool:
    return pole_floor(L, F, B, k) >= gate_integer(F)


def find_crossing(F: int, B: int, k: int = K_OFFICIAL) -> int | None:
    G = gate_integer(F)
    X = F - B
    # The numerator saturates at X/k from below.  If the saturation cap is
    # below the integer gate, no amount of base list mass can cross.
    if X <= 0 or ceil_div(X, k) < G:
        return None
    lo, hi = 0, max(G + 1, 2)
    while not crosses(hi, F, B, k):
        hi *= 2
        if hi > (1 << 270):
            return None
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if crosses(mid, F, B, k):
            hi = mid
        else:
            lo = mid
    return hi


def official_like_rows() -> list[dict]:
    rows: list[dict] = []
    # Powers and near-powers cover the full official range |F| < 2^256 while
    # keeping non-generating bases below both 2^128 and sqrt(F).
    offsets = [0, 1, 12345]
    for f_bits in [140, 160, 180, 200, 224, 240, 252, 256]:
        F0 = 1 << f_bits
        for off in offsets:
            if f_bits == 256 and off == 0:
                continue
            F = F0 - off
            if F <= EPS_DEN:
                continue
            sqrt_cap = math.isqrt(F) - 1
            b_candidates = {
                1 << 20,
                (1 << min(64, max(2, f_bits // 3))) - 1,
                (1 << min(96, max(2, f_bits // 2 - 3))) - 1,
                min((1 << 127) - 1, sqrt_cap),
            }
            for B in sorted(b for b in b_candidates if 0 < b < F and b < (1 << 128) and b * b < F):
                rows.append({"name": f"F=2^{f_bits}-{off},B~{B.bit_length()}b", "F": F, "B": B})
    # Deduplicate because small f_bits can collapse candidates.
    seen = set()
    uniq = []
    for row in rows:
        key = (row["F"], row["B"])
        if key not in seen:
            seen.add(key)
            uniq.append(row)
    return uniq


def invalid_controls() -> list[dict]:
    # These rows violate the non-generating separation: B is too close to F, so
    # X/k cannot reach the MCA gate.  They should be detected as non-crossing,
    # proving the harness is not vacuously green.
    return [
        {"name": "invalid_B_near_F_160", "F": 1 << 160, "B": (1 << 160) - (1 << 70)},
        {"name": "invalid_B_near_F_200", "F": (1 << 200) - 99, "B": (1 << 200) - (1 << 90)},
    ]


def monotone_sample_ok(F: int, B: int, L_star: int | None) -> bool:
    G = gate_integer(F)
    points = {0, 1, max(0, G - 1), G, G + 1, 2 * G, G + 2 * K_OFFICIAL + 4}
    if L_star is not None:
        points.update({max(0, L_star - 1), L_star, L_star + 1})
    last = -1
    for L in sorted(points):
        value = pole_floor(L, F, B)
        if value < last:
            return False
        last = value
    return True


def analyse_row(row: dict) -> dict:
    F = row["F"]
    B = row["B"]
    G = gate_integer(F)
    X = F - B
    L_star = find_crossing(F, B)
    item = {
        "name": row["name"],
        "F_bits": F.bit_length(),
        "B_bits": B.bit_length(),
        "sqrt_separated": B * B < F,
        "B_lt_2^128": B < (1 << 128),
        "gate_integer_bits": G.bit_length(),
        "saturation_cap_bits": (X // K_OFFICIAL).bit_length() if X > 0 else 0,
        "crossing_L": L_star,
        "monotone_sample_ok": monotone_sample_ok(F, B, L_star),
    }
    if L_star is None:
        item.update(
            {
                "status": "NO_CROSSING",
                "expected_for_official_geometry": False,
                "saturation_above_gate": X // K_OFFICIAL >= G,
            }
        )
        return item

    N_before = pole_floor(L_star - 1, F, B) if L_star > 0 else 0
    N_at = pole_floor(L_star, F, B)
    excess = L_star - G
    item.update(
        {
            "status": "CROSSES",
            "crossing_excess_over_gate": excess,
            "crossing_excess_bits": excess.bit_length() if excess >= 0 else None,
            "N_before_minus_gate": N_before - G,
            "N_at_minus_gate": N_at - G,
            "no_premature_crossing": L_star >= G,
            "crosses_by_gate_plus_2k": L_star <= G + 2 * K_OFFICIAL + 4,
            "within_doubled_base_reserve": L_star <= 2 * G,
        }
    )
    return item


def checkpoint(payload: dict) -> None:
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    payload = {
        "started_at_unix": time.time(),
        "time_limit_seconds": args.time_limit,
        "official_like": [],
        "invalid_controls": [],
        "summary": {
            "official_rows": 0,
            "official_failures": 0,
            "invalid_controls": 0,
            "invalid_controls_detected": 0,
        },
    }
    checkpoint(payload)

    for row in official_like_rows():
        if time.monotonic() >= deadline:
            payload["stopped_by_time_guard"] = True
            break
        item = analyse_row(row)
        ok = (
            item["status"] == "CROSSES"
            and item["monotone_sample_ok"]
            and item["sqrt_separated"]
            and item["B_lt_2^128"]
            and item["no_premature_crossing"]
            and item["crosses_by_gate_plus_2k"]
            and item["within_doubled_base_reserve"]
            and item["N_before_minus_gate"] < 0
            and item["N_at_minus_gate"] >= 0
        )
        item["ok"] = ok
        payload["official_like"].append(item)
        payload["summary"]["official_rows"] += 1
        payload["summary"]["official_failures"] += 0 if ok else 1
        checkpoint(payload)

    for row in invalid_controls():
        item = analyse_row(row)
        detected = item["status"] == "NO_CROSSING"
        item["detected_invalid_geometry"] = detected
        payload["invalid_controls"].append(item)
        payload["summary"]["invalid_controls"] += 1
        payload["summary"]["invalid_controls_detected"] += 1 if detected else 0
        checkpoint(payload)

    payload["finished_at_unix"] = time.time()
    checkpoint(payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0 if (
        payload["summary"]["official_failures"] == 0
        and payload["summary"]["invalid_controls_detected"] == payload["summary"]["invalid_controls"]
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
