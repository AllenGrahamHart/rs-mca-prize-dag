#!/usr/bin/env python3
"""Verify the exact 128-row WCL ell=1 weight-six extension packet."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "experiments/prize_resolution"
SOURCE = BASE / "dli_wcl_ell1_weight6_extension_row_mitm.cpp"
LAUNCHER = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_modal.py"
RESULT = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_result.json"
PREREG = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_prereg.md"
AUDIT_SOURCE = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_audit.cpp"
AUDIT_LAUNCHER = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_audit_modal.py"
AUDIT_RESULT = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_audit_result.json"

HASHES = {
    SOURCE: "72e3ffccf0490aeb35416ba84faadee9e021fae463dd1013d8a99f04ed841f84",
    LAUNCHER: "7adf691b6417e1a0fab0c17a6dc18eb3ec27f80dacf426e74549e06f2b226405",
    RESULT: "7e5e0579d3e4d00a46897f29331780fe98f1e5fa1666da6c51612aa5568a7cd9",
    PREREG: "4f27922d87488d8ae08ec23fbfa050712da4259eb645fd8af74f17738e512792",
    AUDIT_SOURCE: "c2b877ded7e60ed347fbdb925306b581c1e9e60b9e41f4d9f092a0d350a045ea",
    AUDIT_LAUNCHER: "fa6f575b022b55f6810e737bedd81331f4a4d8b2847995d4e3e7f341a5799055",
    AUDIT_RESULT: "b99d200e4457b89ed27c83d977647ef3df540a8389c2c45302df5880b7f887c6",
}

COUNT = 128
PAIR_COUNT = 129_540
TRIPLE_COUNT = 21_849_080
OFFICIAL_ORDER = 1 << 41
TOP_KEYS = {"schema", "status", "panel", "rows", "worker_errors", "relation_count"}
PANEL_KEYS = {"p", "q", "k", "degree", "valuation"}
ROW_KEYS = PANEL_KEYS | {
    "omega",
    "seed",
    "status",
    "pair_count",
    "triples_scanned",
    "seconds",
}
AUDIT_TOP_KEYS = {"schema", "status", "indices", "rows", "worker_errors"}
AUDIT_ROW_KEYS = {
    "index",
    "p",
    "omega",
    "seed",
    "status",
    "pair_count",
    "triples_scanned",
}


class Reject(ValueError):
    pass


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def prime_factors_small(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def prove_prime_pocklington(p: int, k: int, valuation: int) -> None:
    if p - 1 != k * (1 << valuation) or k <= 0 or k % 2 == 0:
        raise Reject("p-1 factorization")
    factors = [2, *prime_factors_small(k)]
    for prime in factors:
        witness_found = False
        for witness in range(2, 1000):
            if (
                pow(witness, p - 1, p) == 1
                and math.gcd(pow(witness, (p - 1) // prime, p) - 1, p) == 1
            ):
                witness_found = True
                break
        if not witness_found:
            raise Reject(f"Pocklington witness for factor {prime}")


def validate(data: object) -> list[dict[str, object]]:
    if not isinstance(data, dict) or set(data) != TOP_KEYS:
        raise Reject("top-level schema")
    if (
        data["schema"] != "dli-wcl-ell1-weight6-extension-row-mitm-panel-v1"
        or data["status"] != "COMPLETE"
        or data["worker_errors"] != []
        or integer(data["relation_count"]) != 0
    ):
        raise Reject("header")
    panel = data["panel"]
    rows = data["rows"]
    if not isinstance(panel, list) or not isinstance(rows, list):
        raise Reject("panel types")
    if len(panel) != COUNT or len(rows) != COUNT:
        raise Reject("panel size")

    seen: set[int] = set()
    for index, (expected, row) in enumerate(zip(panel, rows)):
        if not isinstance(expected, dict) or set(expected) != PANEL_KEYS:
            raise Reject("panel row schema")
        if not isinstance(row, dict) or set(row) != ROW_KEYS:
            raise Reject("result row schema")
        p = integer(expected["p"])
        q = integer(expected["q"])
        k = integer(expected["k"])
        degree = integer(expected["degree"])
        valuation = integer(expected["valuation"])
        if index < 64:
            class_ok = valuation == 39 and degree == 4
        else:
            class_ok = valuation == 40 and degree == 2
        if (
            not class_ok
            or p in seen
            or p >= 1 << 64
            or q != p**degree
            or q >= 1 << 256
            or pow(p, degree, OFFICIAL_ORDER) != 1
            or pow(p, degree // 2, OFFICIAL_ORDER) == 1
            or (p - 1) % 512 != 0
        ):
            raise Reject("official row contract")
        prove_prime_pocklington(p, k, valuation)
        seen.add(p)

        if any(row[key] != expected[key] for key in PANEL_KEYS):
            raise Reject("row identity")
        seed = integer(row["seed"])
        omega = integer(row["omega"])
        seconds = row["seconds"]
        if (
            row["status"] != "EXHAUSTED"
            or integer(row["pair_count"]) != PAIR_COUNT
            or integer(row["triples_scanned"]) != TRIPLE_COUNT
            or not isinstance(seconds, (int, float))
            or isinstance(seconds, bool)
            or seconds < 0
            or not 2 <= seed < p
            or pow(seed, (p - 1) // 2, p) != p - 1
            or any(pow(base, (p - 1) // 2, p) != 1 for base in range(2, seed))
            or omega != pow(seed, (p - 1) // 512, p)
            or pow(omega, 512, p) != 1
            or pow(omega, 256, p) != p - 1
        ):
            raise Reject("search row payload")
    return rows


def validate_audit(data: object, rows: list[dict[str, object]]) -> None:
    indices = [0, 63, 64, 127]
    if not isinstance(data, dict) or set(data) != AUDIT_TOP_KEYS:
        raise Reject("audit top-level schema")
    if (
        data["schema"] != "dli-wcl-ell1-weight6-extension-row-mitm-audit-v1"
        or data["status"] != "COMPLETE"
        or data["worker_errors"] != []
        or data["indices"] != indices
        or not isinstance(data["rows"], list)
        or len(data["rows"]) != len(indices)
    ):
        raise Reject("audit header")
    for index, audit_row in zip(indices, data["rows"]):
        if not isinstance(audit_row, dict) or set(audit_row) != AUDIT_ROW_KEYS:
            raise Reject("audit row schema")
        primary = rows[index]
        if audit_row["index"] != index:
            raise Reject("audit index")
        for key in ("p", "omega", "seed", "status", "pair_count", "triples_scanned"):
            if audit_row[key] != primary[key]:
                raise Reject(f"audit mismatch {index}: {key}")


def main() -> None:
    for path, expected in HASHES.items():
        if digest(path) != expected:
            raise Reject(f"artifact hash: {path.name}")
    if PAIR_COUNT != math.comb(510, 2) - 255:
        raise Reject("pair ledger")
    if TRIPLE_COUNT != math.comb(510, 3) - 255 * 508:
        raise Reject("triple ledger")

    data = json.loads(RESULT.read_text())
    rows = validate(data)
    validate_audit(json.loads(AUDIT_RESULT.read_text()), rows)

    mutations = (
        lambda item: item["rows"].pop(),
        lambda item: item["rows"][0].__setitem__("status", "FOUND"),
        lambda item: item["rows"][0].__setitem__("triples_scanned", TRIPLE_COUNT - 1),
        lambda item: item["rows"][0].__setitem__("omega", 1),
        lambda item: item["panel"][0].__setitem__("degree", 2),
        lambda item: item["panel"][0].__setitem__("q", item["panel"][0]["q"] + 1),
        lambda item: item.__setitem__("relation_count", 1),
        lambda item: item["worker_errors"].append({"error": "control"}),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")

    print(
        "DLI_WCL_ELL1_WEIGHT6_FIRST128_EXTENSION_PASS "
        f"rows={len(rows)} pairs={PAIR_COUNT*COUNT} triples={TRIPLE_COUNT*COUNT} "
        f"pocklington=128 audit_replays=4 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
