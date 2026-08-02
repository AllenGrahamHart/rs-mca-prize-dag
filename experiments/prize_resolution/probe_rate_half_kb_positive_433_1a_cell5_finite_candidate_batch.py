#!/usr/bin/env python3
"""Fresh exact replays for the first 23 routed cell-5 fibers."""

import argparse
import contextlib
import hashlib
import io
import json
import sys
import time
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber as probe


PRIME = probe.P
GUARD_CANDIDATES = (
    33199819, 67070255, 461778186, 645288348, 749209962, 1117681606,
    1192073071, 1388698644, 1722212723, 1788857732, 1860858030,
    1920178763, 1995696621,
)
COEFFICIENT_CANDIDATES = (
    263415810, 282428254, 457960787, 790247430, 994619988, 1234520829,
    1310630326, 1373882361, 1660665744, 1806635209,
)
ROUTES = {
    value: 3 if value == 1860858030 else 2
    for value in GUARD_CANDIDATES + COEFFICIENT_CANDIDATES
}
SOURCE_FILES = (
    "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json",
)


class ProbeError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise ProbeError(message)


def base_roots(polynomial):
    require(
        polynomial
        and all(len(coefficient) == 1 for coefficient in polynomial),
        "non-base gcd passed to base-root extractor",
    )
    e = sp.symbols("e")
    value = sp.Poly(
        sum(coefficient[0] * e**index for index, coefficient in enumerate(polynomial)),
        e,
        modulus=PRIME,
    )
    _, factorization = sp.factor_list(value)
    roots = []
    for factor, _multiplicity in factorization:
        if factor.degree() == 1:
            root = -int(factor.nth(0)) * pow(int(factor.nth(1)), -1, PRIME)
            roots.append(root % PRIME)
    return sorted(set(roots))


def classify_row(row):
    guard = [[PRIME - 1], [0], [1]]
    if row["gcd"] == [[1]] or row["gcd"] == guard:
        return "bezout_guard", [], []
    if row["finite_factor_degree"] > 1:
        return "nonbase_primitive", [], []
    roots = base_roots(row["gcd"])
    coordinates = row["coordinates"]
    require(all(len(value) == 1 for value in coordinates.values()), "bad linear coordinates")
    forbidden_squares = {
        1,
        coordinates["b"][0] ** 2 % PRIME,
        coordinates["c"][0] ** 2 % PRIME,
    }
    admissible = [
        root
        for root in roots
        if root != 0 and root * root % PRIME not in forbidden_squares
    ]
    return (
        "survivor" if admissible else "target_collision",
        roots,
        admissible,
    )


def source_hashes():
    return {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in SOURCE_FILES
    }


def packet(records, status):
    return {
        "schema": "rate-half-kb-positive-433-1a-cell5-finite-candidate-v1",
        "status": status,
        "characteristic": PRIME,
        "routes": [{"fiber": value, "chart": ROUTES[value]} for value in ROUTES],
        "source_sha256": source_hashes(),
        "records": records,
        "scope": (
            "fresh exact finite-subfactor DE+/DE-/BE gcd replays on 23 routed "
            "fibers; no remaining-fiber, other-sign, cell, route, row, or Prize closure"
        ),
    }


def run(output=None):
    records = []
    for fiber, chart in ROUTES.items():
        started = time.monotonic()
        probe.T = fiber
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            probe.main(chart_index=chart)
        result = json.loads(stream.getvalue())
        require(result["status"] == "COMPLETE" and result["fiber"] == fiber, "probe failed")
        rows = []
        for row in result["rows"]:
            reason, roots, admissible = classify_row(row)
            rows.append(
                {
                    "factor": row["factor"],
                    "finite_factor": row["finite_factor"],
                    "finite_factor_degree": row["finite_factor_degree"],
                    "finite_factor_polynomial": row["finite_factor_polynomial"],
                    "coordinates": row["coordinates"],
                    "pair_degree": row["pair_degree"],
                    "colored_degree": row["colored_degree"],
                    "gcd": row["gcd"],
                    "gcd_degree": row["gcd_degree"],
                    "base_roots": roots,
                    "admissible_roots": admissible,
                    "closure_reason": reason,
                }
            )
        classification = (
            "EXCLUDED"
            if rows and all(row["closure_reason"] != "survivor" for row in rows)
            else "SURVIVOR"
        )
        records.append(
            {
                "fiber": fiber,
                "chart": chart,
                "classification": classification,
                "elapsed_seconds": round(time.monotonic() - started, 6),
                "rows": rows,
            }
        )
        if output:
            output.write_text(json.dumps(packet(records, "INCOMPLETE"), indent=2, sort_keys=True) + "\n")
        reasons = {reason: sum(row["closure_reason"] == reason for row in rows) for reason in {row["closure_reason"] for row in rows}}
        print(
            f"{classification} fiber={fiber} chart={chart} rows={len(rows)} "
            f"reasons={json.dumps(reasons, sort_keys=True)}",
            flush=True,
        )
    result = packet(records, "COMPLETE")
    if output:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.output)
    require(all(record["classification"] == "EXCLUDED" for record in result["records"]), "surviving fiber")
    print(f"CELL5_FINITE_CANDIDATE_BATCH_COMPLETE fibers={len(result['records'])}")


if __name__ == "__main__":
    try:
        main()
    except (ProbeError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"CELL5_FINITE_CANDIDATE_BATCH_FAIL {error}")
        raise SystemExit(1)
