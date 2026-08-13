#!/usr/bin/env python3
"""Verify the sparse-direction mean-centered Gram profile."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "4e233dcdc3a51a92b2c8124ae8667e3cabdaa49c4bea9640903b467621c8f135"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/statement.md": "3cf121f53d306a72c6e624da54d7488a8036272e9013f54eceb87617923a2fdb",
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/proof.md": "109d04f93c9d4f0d506a5d5826f7a37241be174b96f8cb751dd3ca73e958092b",
    "background/nodes/rate_half_mca_sparse_direction_near_johnson_gram_rank_payment/statement.md": "5ef6875c80b2634397a0ab9963c0a868fa85210dc2c240ae2d4e8e1d543c85ba",
    "background/nodes/rate_half_mca_sparse_direction_near_johnson_gram_rank_payment/proof.md": "c67b8a386c2f2cfb9673f351dd1faaef2b1b83c3d348a64481a5c5f824150f7c",
}


class Reject(ValueError):
    pass


def raw_cap(R: int, d: int, K: int, e: int, h: int) -> int | None:
    n = R + K - e
    A = d + K - h
    c = K - 1
    johnson_den = A * A - n * c
    if johnson_den > 0:
        return n * (A - c) // johnson_den
    g = -johnson_den
    chord_balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    if g < 0 or chord_balance < 0 or T <= 0:
        return None
    return (n - 1) * n * n * (A - c) // (A * T)


def profile(R: int, d: int, K: int, e: int) -> int | None:
    caps = [0]
    for h in range(1, e + 1):
        current = raw_cap(R, d, K, e, h)
        if current is None:
            return None
        caps.append(current)
    suffix = caps[-1]
    for h in range(e - 1, 0, -1):
        suffix = min(suffix, caps[h])
        caps[h] = suffix
    if any(caps[h] < caps[h - 1] for h in range(1, e + 1)):
        raise Reject("suffix monotonicity")
    return sum((caps[h] - caps[h - 1]) * (e // h) for h in range(1, e + 1))


def endpoint(R: int, d: int, K: int, e: int) -> dict[str, int | None]:
    n = R + K - e
    A = d + K - e
    c = K - 1
    g = n * c - A * A
    balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    cap = None
    if g >= 0 and balance >= 0 and T > 0:
        cap = (n - 1) * n * n * (A - c) // (A * T)
    return {
        "punctured_length": n,
        "agreement": A,
        "johnson_defect": g,
        "chord_balance": balance,
        "mean_gram_denominator": T,
        "ordinary_cap": cap,
        "profile": profile(R, d, K, e),
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-mean-centered-gram-profile-v1":
        raise Reject("version")
    if contract["sources"] != {
        "punctured_johnson_profile": "rate_half_mca_sparse_direction_punctured_johnson_profile",
        "centered_gram_rung": "rate_half_mca_sparse_direction_near_johnson_gram_rank_payment",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "mean_center": "p=A^2/n",
        "hypotheses": "g=nc-A^2>=0, 2A^2>=nc, T=(n-A)^2-(n-1)g>0",
        "ordinary_list_cap": "floor((n-1)n^2(A-c)/(A*T))",
        "profile": "sum_(h=1)^e (B_h-B_(h-1))*floor(e/h), B_h=min_(h<=v<=e) C_v",
    }:
        raise Reject("theorem")

    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 14, 274980728111395087, 64038, 64047, 984529,
            984543, 3439, 972338, 10854383, 5257459620, 180835154,
            181731868, 64048, -1499457466, None,
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 6, 16777215, 65419, 65454, 983122,
            983128, 2000, 915640, 3084360, 62421746104, 15184718,
            16101127, 65455, 58496056500, 17120123,
        ),
    }
    keys = (
        "R", "d", "K", "budget", "first_new_e", "last_paid_e",
        "equivalent_defect_floor", "punctured_length_at_last",
        "agreement_at_last", "johnson_defect_at_last",
        "chord_balance_at_last", "mean_gram_denominator_at_last",
        "ordinary_cap_at_last", "profile_at_last", "adjacent_e",
        "adjacent_mean_gram_denominator", "adjacent_profile",
    )
    if len(contract["rows"]) != 2:
        raise Reject("row count")
    checks = 0
    for row in contract["rows"]:
        record = tuple(row.get(key) for key in keys)
        if record != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, K, budget, first, last, defect, nlast, Alast, glast, balance, Tlast, Qlast, Plast, adjacent, Tnext, Pnext = record
        if defect != R - last or adjacent != last + 1:
            raise Reject("coordinates")
        if endpoint(R, d, K, last) != {
            "punctured_length": nlast,
            "agreement": Alast,
            "johnson_defect": glast,
            "chord_balance": balance,
            "mean_gram_denominator": Tlast,
            "ordinary_cap": Qlast,
            "profile": Plast,
        }:
            raise Reject("endpoint")
        if Plast > budget:
            raise Reject("endpoint budget")
        next_record = endpoint(R, d, K, adjacent)
        if next_record["mean_gram_denominator"] != Tnext or next_record["profile"] != Pnext:
            raise Reject("adjacent")
        if row["name"] == "KoalaBear MCA":
            if Tnext >= 0 or Pnext is not None:
                raise Reject("KoalaBear stop")
        elif Tnext <= 0 or Pnext is None or Pnext <= budget:
            raise Reject("Mersenne stop")
        for e in range(first, last + 1):
            value = profile(R, d, K, e)
            if value is None or value > budget:
                raise Reject("strip")
            checks += 1
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for row_index, key, delta in (
        (0, "mean_gram_denominator_at_last", 1),
        (0, "adjacent_mean_gram_denominator", 1),
        (1, "profile_at_last", 1),
        (1, "adjacent_profile", -1),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_MEAN_CENTERED_GRAM_PROFILE_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
