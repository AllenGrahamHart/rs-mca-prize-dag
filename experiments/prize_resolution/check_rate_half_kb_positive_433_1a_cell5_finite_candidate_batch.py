#!/usr/bin/env python3
"""Check the first 23 exact cell-5 finite-fiber exclusions."""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber as probe
import probe_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch as batch


RESULT = HERE / "rate_half_kb_positive_433_1a_cell5_finite_candidate_batch_result.json"
EXPECTED_RESULT_SHA256 = (
    "d74aa015c557d9497090b6085a4280e8a43d9dd5f4ec109e3e31b736271cd8c8"
)
EXPECTED_PROGRAM_SHA256 = (
    "b6e2aa64df5923c3d2e696842cfbc53d7d3011f3f013995dbcbd719208ca55fb"
)
EXPECTED_REASON_COUNTS = {
    "bezout_guard": 383,
    "nonbase_primitive": 16,
    "target_collision": 34,
}
EXPECTED_PARENT_DEGREES = {1: 4, 2: 4, 3: 4, 4: 8, 5: 4}


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def scalar_roots(polynomial):
    require(
        polynomial and all(len(coefficient) == 1 for coefficient in polynomial),
        "nonscalar gcd in target-collision row",
    )
    e = sp.symbols("e")
    value = sp.Poly(
        sum(coefficient[0] * e**index for index, coefficient in enumerate(polynomial)),
        e,
        modulus=probe.P,
    )
    _, factors = sp.factor_list(value)
    roots = []
    for factor, _multiplicity in factors:
        if factor.degree() == 1:
            roots.append(
                (-int(factor.nth(0)) * pow(int(factor.nth(1)), -1, probe.P))
                % probe.P
            )
    return sorted(set(roots))


def verify(path=RESULT):
    raw = path.read_bytes()
    if path == RESULT:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_RESULT_SHA256, "result hash mismatch")
    payload = json.loads(raw)
    require(payload["schema"].endswith("finite-candidate-v1"), "schema mismatch")
    require(payload["status"] == "COMPLETE" and payload["characteristic"] == probe.P, "packet incomplete")
    expected_routes = [{"fiber": value, "chart": batch.ROUTES[value]} for value in batch.ROUTES]
    require(payload["routes"] == expected_routes, "route coverage mismatch")
    require(
        hashlib.sha256((HERE / "probe_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch.py").read_bytes()).hexdigest()
        == EXPECTED_PROGRAM_SHA256,
        "batch program hash mismatch",
    )
    expected_sources = {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in batch.SOURCE_FILES
    }
    require(payload["source_sha256"] == expected_sources, "source provenance mismatch")
    records = payload.get("records")
    require(isinstance(records, list) and len(records) == 23, "fiber count mismatch")
    require([record["fiber"] for record in records] == list(batch.ROUTES), "fiber order mismatch")
    reasons = Counter()
    total_rows = 0
    guard = [[probe.P - 1], [0], [1]]
    for record in records:
        fiber = record["fiber"]
        require(record["chart"] == batch.ROUTES[fiber], "chart mismatch")
        require(record["classification"] == "EXCLUDED", "unexcluded fiber")
        rows = record.get("rows")
        require(isinstance(rows, list) and rows, "empty fiber row ledger")
        total_rows += len(rows)
        parents = {index: [] for index in range(1, 6)}
        for row in rows:
            factor = row["factor"]
            require(factor in parents, "factor outside 1..5")
            parents[factor].append(row)
            modulus = row["finite_factor_polynomial"]
            require(len(modulus) - 1 == row["finite_factor_degree"], "factor degree mismatch")
            require(modulus[-1] == 1 and probe.irreducible(modulus), "bad finite factor")
            coordinates = row["coordinates"]
            require(set(coordinates) == {"b", "x0", "x1", "r", "c"}, "coordinate names mismatch")
            relation = probe.guards.reduce_mod(
                probe.guards.add(
                    coordinates["x1"],
                    probe.guards.add(
                        [2 * value for value in coordinates["x0"]],
                        [3 * value for value in coordinates["b"]],
                    ),
                ),
                modulus,
            )
            require(relation == probe.guards.reduce_mod([0, 1], modulus), "primitive coordinate identity fails")
            gcd = row["gcd"]
            require(len(gcd) - 1 == row["gcd_degree"] and gcd[-1] == [1], "bad monic gcd")
            reason = row["closure_reason"]
            reasons[reason] += 1
            require(not row["admissible_roots"], "admissible root survived")
            if reason == "bezout_guard":
                require(gcd in ([[1]], guard), "Bezout row has outside gcd")
                require(not row["base_roots"], "unexpected root ledger")
            elif reason == "nonbase_primitive":
                require(row["finite_factor_degree"] > 1, "nonbase reason on linear factor")
                require(not row["base_roots"], "unexpected nonbase root ledger")
            elif reason == "target_collision":
                require(row["finite_factor_degree"] == 1, "target collision outside base field")
                roots = scalar_roots(gcd)
                require(roots == row["base_roots"] and roots, "base-root ledger mismatch")
                require(all(len(value) == 1 for value in coordinates.values()), "nonscalar coordinates")
                forbidden_squares = {
                    1,
                    coordinates["b"][0] ** 2 % probe.P,
                    coordinates["c"][0] ** 2 % probe.P,
                }
                require(
                    all(root == 0 or root * root % probe.P in forbidden_squares for root in roots),
                    "target-collision reason fails",
                )
            else:
                raise CertificateError("unknown closure reason")
        for factor, factor_rows in parents.items():
            require(factor_rows, "missing parent factor")
            require(
                [row["finite_factor"] for row in factor_rows]
                == list(range(1, len(factor_rows) + 1)),
                "finite-factor indexing mismatch",
            )
            require(
                sum(row["finite_factor_degree"] for row in factor_rows)
                == EXPECTED_PARENT_DEGREES[factor],
                "parent factor degree coverage mismatch",
            )
    require(total_rows == 433, "total row count mismatch")
    require(dict(reasons) == EXPECTED_REASON_COUNTS, "closure-reason census mismatch")
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, default=RESULT)
    args = parser.parse_args()
    records = verify(args.result)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_FINITE_CANDIDATES_PASS "
        f"fibers={len(records)} rows=433 reasons=383,16,34"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_FINITE_CANDIDATES_FAIL {error}")
        raise SystemExit(1)
