#!/usr/bin/env python3
"""Verify the full-lift mean-centered global-line profile."""

from __future__ import annotations

import copy
import hashlib
import json
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "12b70130eee9f99192a07d730de15006455229ff192f60f46788464ff1846c73"
PINS = {
    "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/statement.md":
        "3724b202ad5e1b50adb1c3ae17660e9cf09a70c588110ad46c79570196ca9f57",
    "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/proof.md":
        "b7e5a10b24b2ed60805d80be3e1ebcd4a47b8832800092f1c1f51123f41896bd",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md":
        "8d103c4c092961387fa02ee18ff851a084c0f7774c0b4b238d1e7fba42dbe02d",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md":
        "5abca3dd268f99b38c483fb12b22c9c7d91e0908b5a4ef389195b648651e3cb2",
}


class Reject(ValueError):
    pass


def raw_cap(R: int, d: int, K: int, e: int, h: int) -> dict[str, int | None]:
    n, m, c = R + K - e, d + K, K - 1
    A = m - h
    D = A * A - n * c
    if D > 0:
        return {
            "cap": n * (A - c) // D, "kind": 1, "A": A,
            "g": -D, "balance": 2 * A * A - n * c, "T": None,
        }
    g = -D
    balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    cap = None
    if g >= 0 and balance >= 0 and T > 0:
        cap = (n - 1) * n * n * (A - c) // (A * T)
    return {"cap": cap, "kind": 2, "A": A, "g": g,
            "balance": balance, "T": T}


@lru_cache(maxsize=None)
def profile(R: int, d: int, K: int, e: int) -> tuple[int | None, dict[str, int | None]]:
    N, m = R + K, d + K
    H = e - (e - K) // 3 - 1
    caps = [0]
    for h in range(1, H + 1):
        record = raw_cap(R, d, K, e, h)
        if record["cap"] is None:
            return None, {
                "H": H, "failure_h": h, "A": record["A"],
                "g": record["g"], "balance": record["balance"],
                "T": record["T"],
            }
        caps.append(int(record["cap"]))
    suffix = caps[-1]
    for h in range(H - 1, 0, -1):
        suffix = min(suffix, caps[h])
        caps[h] = suffix
    if any(caps[h] < caps[h - 1] for h in range(1, H + 1)):
        raise Reject("suffix monotonicity")
    prefix = sum(
        (caps[h] - caps[h - 1]) * (e // h) for h in range(1, H + 1)
    )
    return prefix + N - m + 1, {
        "H": H, "prefix": prefix, "B_H": caps[H],
        "breaks": sum(caps[h] != caps[h - 1] for h in range(1, H + 1)),
        "failure_h": None,
    }


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
        "schema", "sources", "profile", "rows"
    }:
        raise Reject("schema")
    if payload["schema"] != "rate-half-mca-full-lift-mean-centered-global-line-profile-v1":
        raise Reject("version")
    if payload["profile"] != "sum_(h=1)^H (B_h-B_(h-1))*floor(e/h)+(N-m+1)":
        raise Reject("profile")
    expected_sources = {
        "mean_centered_statement_sha256": PINS[
            "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/statement.md"
        ],
        "mean_centered_proof_sha256": PINS[
            "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/proof.md"
        ],
        "global_line_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md"
        ],
        "global_line_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md"
        ],
    }
    if payload["sources"] != expected_sources or len(payload["rows"]) != 2:
        raise Reject("sources")
    checks = 0
    for row in payload["rows"]:
        R, d, K, budget = row["R"], row["d"], row["K"], row["budget"]
        maximum = (-1, -1)
        for e in range(row["first_new_e"], row["last_paid_e"] + 1):
            total, detail = profile(R, d, K, e)
            if total is None or total > budget:
                raise Reject("paid strip")
            maximum = max(maximum, (total, e))
            if e == row["first_new_e"] and total != row["first_total"]:
                raise Reject("first")
            if e == row["last_paid_e"]:
                if (detail["H"], detail["prefix"], detail["B_H"],
                    detail["breaks"], total) != (
                    row["last_H"], row["last_prefix"], row["last_B_H"],
                    row["last_breaks"], row["last_total"]
                ):
                    raise Reject("last")
            checks += 1
        if maximum != (row["max_total"], row["max_total_e"]):
            raise Reject("maximum")
        adjacent, detail = profile(R, d, K, row["adjacent_e"])
        if adjacent != row["adjacent_total"]:
            raise Reject("adjacent total")
        if row["adjacent_failure_h"] is not None:
            got = (detail["failure_h"], detail["A"], detail["g"],
                   detail["balance"], detail["T"])
            expected = (row["adjacent_failure_h"], row["adjacent_A"],
                        row["adjacent_g"], row["adjacent_balance"],
                        row["adjacent_T"])
            if got != expected or adjacent is not None:
                raise Reject("adjacent theorem wall")
        else:
            h = detail["H"]
            record = raw_cap(R, d, K, row["adjacent_e"], h)
            got = (record["A"], record["g"], record["balance"], record["T"])
            expected = (row["adjacent_A"], row["adjacent_g"],
                        row["adjacent_balance"], row["adjacent_T"])
            if got != expected or adjacent is None or adjacent <= budget:
                raise Reject("adjacent budget wall")
        if row["residual_ceiling"] < row["adjacent_e"]:
            raise Reject("residual")
        checks += 10
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for row, key, delta in (
        (0, "last_total", 1), (0, "adjacent_T", 1),
        (1, "max_total", -1), (1, "adjacent_total", -1),
    ):
        changed = copy.deepcopy(payload)
        changed["rows"][row][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_FULL_LIFT_MEAN_CENTERED_GLOBAL_LINE_PROFILE_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
