#!/usr/bin/env python3
"""Verify the rank-10 margin/interleaving threshold split certificate."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "065d60255d1338120f80b3f8d0fa248a05e0f14c620ed1b4fa81888ec1202c57"
PINS = {
    "statement.md": "6d6963608492d85119f2cadd3f7810f2de8e55e8ed39ee6a9a5c95a18799f059",
    "proof.md": "11f950f680200119f9453d14290c8cc636512cfe686cc93019b192d7751cdaac",
}
DEPENDENCY_FILES = {
    "support_local_transversality": (
        ROOT / "background/nodes/rate_half_mca_support_local_transversality_compiler/statement.md",
        ROOT / "background/nodes/rate_half_mca_support_local_transversality_compiler/proof.md",
    ),
    "error_rank_router": (
        ROOT / "background/nodes/rate_half_mca_support_local_error_rank_router/statement.md",
        ROOT / "background/nodes/rate_half_mca_support_local_error_rank_router/proof.md",
    ),
    "affine_span_list": (
        ROOT / "background/nodes/upstream_gfv4_affine_span_list_compiler/statement.md",
        ROOT / "background/nodes/upstream_gfv4_affine_span_list_compiler/proof.md",
    ),
    "interleaving_collapse": (
        ROOT / "critical/nodes/list_subsqrt_interleaving_collapse/statement.md",
        ROOT / "critical/nodes/list_subsqrt_interleaving_collapse/proof.md",
    ),
}


class Reject(ValueError):
    pass


def falling(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value - offset
    return out


def rising(value: int, length: int) -> int:
    out = 1
    for offset in range(length):
        out *= value + offset
    return out


def high_cap(n: int, K: int, m: int, rank: int, threshold: int) -> int:
    w = m - K
    first = Fraction(
        falling(n, rank + 1),
        m * threshold * rising(w + 1, rank - 1),
    )
    second = Fraction(
        falling(n - K + rank, rank + 1),
        threshold * rising(w + 1, rank),
    )
    value = max(first, second)
    return value.numerator // value.denominator


def split_row(row: dict[str, int], rank: int, threshold: int) -> dict[str, int | bool | list[int]]:
    n, K, m, w = row["n"], row["K"], row["m"], row["w"]
    q = threshold - 1
    agreement = m - q
    residual = agreement - K
    if threshold < 2 or threshold > w + 1 or agreement <= K:
        raise Reject("illegal threshold")
    ordinary = comb(n - K + rank, rank) // comb(residual + rank, rank)
    caps = [n // threshold]
    caps.extend(high_cap(n, K, m, r, threshold) for r in range(1, rank + 1))
    high = max(caps)
    low = (n - agreement) * ordinary
    total = row["near_charge"] + high + low
    field = row["p"] ** row["extension_degree"]
    return {
        "q": q,
        "agreement": agreement,
        "residual_agreement": residual,
        "ordinary_list_cap": ordinary,
        "high_cap": high,
        "rank_caps": caps,
        "low_cap": low,
        "total": total,
        "slack": row["budget"] - total,
        "subsqrt": ordinary * ordinary < field,
    }


def scan(row: dict[str, int], rank: int) -> list[tuple[int, int, dict[str, int | bool | list[int]]]]:
    values = []
    for threshold in range(2, row["w"] + 1):
        item = split_row(row, rank, threshold)
        if item["subsqrt"]:
            values.append((item["total"], threshold, item))
    return values


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "source_head", "dependencies", "koalabear"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-rank10-margin-interleaving-split-payment-v1":
        raise Reject("version")
    if contract["source_head"] != "af0e7c63b3d60873bf3fe2fc898edad85848deb5":
        raise Reject("source")

    dependencies = contract["dependencies"]
    if set(dependencies) != set(DEPENDENCY_FILES):
        raise Reject("dependency keys")
    for name, paths in DEPENDENCY_FILES.items():
        expected = dependencies[name]
        if set(expected) != {"statement_sha256", "proof_sha256"}:
            raise Reject(f"dependency schema {name}")
        got = [hashlib.sha256(path.read_bytes()).hexdigest() for path in paths]
        if got != [expected["statement_sha256"], expected["proof_sha256"]]:
            raise Reject(f"dependency pin {name}")

    row = contract["koalabear"]
    required = {
        "p", "extension_degree", "n", "K", "m", "w", "near_charge",
        "budget", "explanation_rank", "first_paying_threshold",
        "optimal_threshold", "optimal", "neighbor_totals", "next_rank_minima",
    }
    if set(row) != required or row["w"] != row["m"] - row["K"]:
        raise Reject("row schema")
    if row["near_charge"] != 2 * row["w"]:
        raise Reject("near charge")

    rank = row["explanation_rank"]
    values = scan(row, rank)
    paying = [entry for entry in values if entry[0] <= row["budget"]]
    if not paying or paying[0][1] != row["first_paying_threshold"]:
        raise Reject("first paying threshold")
    optimum = min(values)
    if optimum[1] != row["optimal_threshold"]:
        raise Reject("optimal threshold")
    if sum(entry[0] == optimum[0] for entry in values) != 1:
        raise Reject("nonunique optimum")
    item = optimum[2]
    expected_optimal = row["optimal"]
    for key in (
        "q", "agreement", "residual_agreement", "ordinary_list_cap",
        "high_cap", "low_cap", "total", "slack",
    ):
        if item[key] != expected_optimal[key]:
            raise Reject(f"optimal {key}")
    if not item["subsqrt"] or item["rank_caps"][-1] != item["high_cap"]:
        raise Reject("rank maximum or field guard")

    for threshold_text, expected in row["neighbor_totals"].items():
        if split_row(row, rank, int(threshold_text))["total"] != expected:
            raise Reject(f"neighbor {threshold_text}")

    for rank_text, expected in row["next_rank_minima"].items():
        next_rank = int(rank_text)
        next_optimum = min(scan(row, next_rank))
        if (next_optimum[1], next_optimum[0]) != (
            expected["threshold"], expected["total"]
        ):
            raise Reject(f"next rank {rank_text}")
        if next_optimum[0] <= row["budget"]:
            raise Reject(f"unexpected payment rank {rank_text}")
    return len(values) + len(paying) + len(row["next_rank_minima"])


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for name, digest in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {name}")
    contract = json.loads(CONTRACT.read_text())
    checks = validate(contract)
    controls = []
    for path, delta in (
        (("optimal_threshold",), 1),
        (("first_paying_threshold",), 1),
        (("optimal", "total"), 1),
        (("next_rank_minima", "10", "total"), -1),
    ):
        changed = copy.deepcopy(contract)
        target = changed["koalabear"]
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_RANK10_MARGIN_INTERLEAVING_SPLIT_PAYMENT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
