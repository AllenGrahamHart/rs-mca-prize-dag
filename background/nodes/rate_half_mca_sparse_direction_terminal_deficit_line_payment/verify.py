#!/usr/bin/env python3
"""Verify the sparse-direction terminal-deficit line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "b0a15b8c1b86ce9729fcc0e67ec9a1a95ab7b67f2b10973972d5eb051a7d8d76"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/statement.md":
        "3724b202ad5e1b50adb1c3ae17660e9cf09a70c588110ad46c79570196ca9f57",
    "background/nodes/rate_half_mca_sparse_direction_mean_centered_gram_profile/proof.md":
        "b7e5a10b24b2ed60805d80be3e1ebcd4a47b8832800092f1c1f51123f41896bd",
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
    balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    if g < 0 or balance < 0 or T <= 0:
        return None
    return (n - 1) * n * n * (A - c) // (A * T)


def terminal_profile(R: int, d: int, K: int, e: int) -> dict[str, int] | None:
    if e < K:
        return None
    caps = [0]
    for h in range(1, e):
        cap = raw_cap(R, d, K, e, h)
        if cap is None:
            return None
        caps.append(cap)
    prefix_cap = caps[-1]
    suffix = caps[-1]
    for h in range(e - 2, 0, -1):
        suffix = min(suffix, caps[h])
        caps[h] = suffix
    if any(caps[h] < caps[h - 1] for h in range(1, e)):
        raise Reject("suffix monotonicity")
    prefix = sum(
        (caps[h] - caps[h - 1]) * (e // h)
        for h in range(1, e)
    )
    n = R + K - e
    A = d + K - e
    c = K - 1
    if A <= c:
        return None
    line = (n - c) // (A - c)
    return {
        "equivalent_defect_floor": R - e,
        "punctured_length": n,
        "outside_agreement": A,
        "prefix_cap_at_e_minus_1": prefix_cap,
        "prefix_profile": prefix,
        "terminal_cap": line,
        "total_profile": prefix + line,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "sources", "theorem", "rows"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-terminal-deficit-line-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "mean_centered_profile": "rate_half_mca_sparse_direction_mean_centered_gram_profile"
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "hypotheses": "e>=K, n=N-e, A=m-e, c=K-1, A>c",
        "terminal_cap": "floor((n-c)/(A-c))",
        "profile": "sum_(h=1)^(e-1) (B_h-B_(h-1))*floor(e/h)+terminal_cap, B_h=min_(h<=v<e) C_v",
    }:
        raise Reject("theorem")

    bases = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215),
    }
    expected_stops = {
        "KoalaBear MCA": (64049, "prefix-cap-unavailable", None),
        "Mersenne-31 MCA": (65456, "over-budget", 17119507),
    }
    if len(contract["rows"]) != 2:
        raise Reject("row count")
    checks = 0
    for row in contract["rows"]:
        name = row.get("name")
        if name not in bases:
            raise Reject("name")
        R, d, K, budget = bases[name]
        if tuple(row.get(k) for k in ("R", "d", "K", "budget")) != bases[name]:
            raise Reject("base")
        paid = row["paid_e"]
        got = terminal_profile(R, d, K, paid)
        if got is None:
            raise Reject("paid unavailable")
        for key, value in got.items():
            if row.get(key) != value:
                raise Reject(key)
            checks += 1
        if got["total_profile"] > budget:
            raise Reject("paid budget")
        adjacent, reason, value = expected_stops[name]
        if (row["adjacent_e"], row["adjacent_stop"], row["adjacent_profile"]) != (
            adjacent, reason, value
        ):
            raise Reject("adjacent record")
        next_profile = terminal_profile(R, d, K, adjacent)
        if reason == "prefix-cap-unavailable":
            if next_profile is not None:
                raise Reject("expected unavailable")
        elif next_profile is None or next_profile["total_profile"] != value or value <= budget:
            raise Reject("expected over budget")
        checks += 3
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
        (0, "terminal_cap", 1),
        (0, "prefix_profile", 1),
        (1, "total_profile", 1),
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
        "RATE_HALF_MCA_SPARSE_DIRECTION_TERMINAL_DEFICIT_LINE_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
