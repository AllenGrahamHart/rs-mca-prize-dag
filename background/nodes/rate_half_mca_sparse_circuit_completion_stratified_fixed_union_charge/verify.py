#!/usr/bin/env python3
"""Verify the completion-stratified fixed-union charge contract."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "92f7f651f2b2b5cbae938d9bd0ced7e8d9c765eac8679bc1b937a49b8bbe902e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def choose(n: int, r: int) -> int:
    return 0 if r < 0 or r > n else comb(n, r)


def inside_count(u: int, b: int, r: int) -> int:
    return choose(u - b, r) + b * choose(u - b, r - 1)


def circuit_cap(
    K: int,
    m: int,
    u: int,
    g: int,
    d: int,
    maximum: int,
    parallel: int | None = None,
) -> tuple[int, tuple[int, ...]]:
    count = choose if parallel is None else lambda n, r: inside_count(n, parallel, r)
    terms = []
    total = count(u, d)
    for outside in range(1, d + 1):
        budget = maximum
        if outside <= g:
            budget = min(maximum, max(0, K - g - u))
        term = (
            count(u, d - outside)
            * choose(m - u, outside - 1)
            * budget
            // outside
        )
        terms.append(term)
        total += term
    return total, tuple(terms)


def validate(data: object) -> dict[str, object]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"] == "rate-half-mca-completion-stratified-fixed-union-charge-v1", "schema")
    require(data["ambient_dimension"] == 10, "ambient")
    require(data["selected_set_size"] == 11, "selected size")
    require(data["formula"]["controlled_stratum"] == "j<=g", "stratum")
    require(data["formula"]["fixed_completion_budget"] == "min(M_d,K-g-u)", "budget")

    expected = (
        (1500, (40, 300, 700, 455), 1455, (28, 270, 700, 455)),
        (1051, (2, 48, 264, 440, 297), 981, (0, 24, 220, 440, 297)),
    )
    checks = 0
    for row, want in zip(data["toy_rows"], expected):
        generic = circuit_cap(row["K"], row["m"], row["u"], row["g"], row["d"], row["M"])
        structured = circuit_cap(
            row["K"], row["m"], row["u"], row["g"], row["d"], row["M"], row["b"]
        )
        require(generic == want[:2], "generic toy")
        require(structured == want[2:], "parallel toy")
        require(structured[0] <= generic[0], "refinement direction")
        checks += 3
    return {"toy_rows": len(expected), "checks": checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("ambient_dimension", 11),
        lambda item: item["formula"].__setitem__("controlled_stratum", "j<g"),
        lambda item: item["formula"].__setitem__("fixed_completion_budget", "M_d"),
        lambda item: item["toy_rows"][0].__setitem__("u", 6),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    result["contract_sha256"] = CONTRACT_SHA256
    result["tamper_rejected"] = tamper_selftest(data)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
