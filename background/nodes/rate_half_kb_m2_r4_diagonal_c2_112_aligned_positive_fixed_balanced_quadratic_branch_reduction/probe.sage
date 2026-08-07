#!/usr/bin/env sage
"""Exact structural probe for the two balanced fixed quadratic orbits."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")


def load_library():
    namespace = dict(globals())
    namespace.update({"__name__": "branch_core_library", "__file__": str(LIBRARY)})
    raw = LIBRARY.read_text()
    exec(compile(raw, str(LIBRARY), "exec"), namespace)
    return namespace


def canonical_json(value):
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=lambda item: int(item) if item in ZZ else str(item),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", choices=("F04-R11", "F05-R11"), required=True)
    args = parser.parse_args()
    library = load_library()
    branch = library["build_branch"](args.cell)
    metric = library["metric"]
    equations = branch["equations"]
    factors = branch["factors"]

    records = {}
    for name, value in equations.items():
        records[name] = {
            "metric": metric(value),
            "factors": [
                {
                    "exponent": record["exponent"],
                    "metric": record["metric"],
                    "named_unit_factor": record["named_unit_factor"],
                    "polynomial": (
                        str(record["factor"])
                        if record["metric"]["terms"] <= 300
                        else None
                    ),
                }
                for record in factors[name]
            ],
        }

    gcds = {}
    for left, right in (("R", "E2"), ("R", "E3"), ("E2", "E3"), ("U", "V")):
        common = equations[left].gcd(equations[right])
        gcds[f"{left}_{right}"] = {
            "metric": metric(common),
            "polynomial": str(common) if len(common.monomials()) <= 300 else None,
        }

    result = {
        "schema": "kb-c2-112-fixed-balanced-quadratic-branch-probe-v1",
        "cell": args.cell,
        "row_w_degrees": [int(row.degree()) for row in branch["converted"]],
        "quadratic_pair": [0, 1],
        "generic_reconstruction": "w=-U/V",
        "equations": records,
        "essential_metrics": {
            name: metric(branch["essential"][name]) for name in ("R", "E2", "E3")
        },
        "gcds": gcds,
        "transported_unit_count": len(branch["transported_units"]),
        "transported_unit_factor_count": len(branch["unit_keys"]),
        "terminal": "EXACT_FACTORED_BRANCH_DATA_NO_EMPTINESS_CLAIM",
    }
    payload = canonical_json(result)
    result["payload_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
    print(canonical_json(result))


if __name__ == "__main__":
    main()
