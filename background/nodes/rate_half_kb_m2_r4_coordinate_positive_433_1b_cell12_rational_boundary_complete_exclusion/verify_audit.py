#!/usr/bin/env python3
"""Independent low-degree arithmetic audit of the boundary exclusion."""

import ast
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
BOUNDARY = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
AUDIT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_audit_result.json"
)
PRIME = 2130706433
t, r, c, b = sp.symbols("t r c b")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    ast.parse((NODE / "verify.py").read_text())
    kernel_payload = json.loads(KERNEL.read_text())
    kernel = [sp.sympify(item["expression"])
              for item in kernel_payload["rows"][0]["kernel"]]
    boundary = json.loads(BOUNDARY.read_text())
    audit = json.loads(AUDIT.read_text())
    audit_values = {
        (row["point_index"], *row["sigma"]): row
        for row in audit["rows"]
    }
    point_index = 0
    endpoint_values = set()
    for boundary_row in boundary["rows"]:
        for point in boundary_row["rational_points"]:
            substitutions = {t: point["t"], r: point["r"],
                             c: point["c"], b: point["b"]}
            values = [int(value.subs(substitutions)) % PRIME for value in kernel]
            label = -point["t"]*point["t"] % PRIME
            a_value = sum(values[index]*pow(label, index, PRIME)
                          for index in range(3)) % PRIME
            b_value = sum(values[index+3]*pow(label, index, PRIME)
                          for index in range(3)) % PRIME
            require(a_value != 0, "missing denominator")
            missing = b_value*pow(a_value, -1, PRIME) % PRIME
            source_sum = (
                label*pow((values[6]+values[7]*label) % PRIME, 2, PRIME)
                * pow(a_value, -2, PRIME)
            ) % PRIME
            for value in (source_sum, source_sum-4*missing):
                require(pow(value % PRIME, (PRIME-1)//2, PRIME) == 1,
                        "missing lift nonsquare")
            obstructions = tuple(
                (pow((point[name]*point[name]+missing) % PRIME, 2, PRIME)
                 - source_sum*point[name]*point[name]) % PRIME
                for name in ("b", "c")
            )
            require(all(obstructions), "endpoint obstruction vanishes")
            endpoint_values.add(obstructions)
            for sigma_c in (-1, 1):
                for sigma_o in (-1, 1):
                    row = audit_values[(point_index, sigma_c, sigma_o)]
                    require(row["missing"] == missing and
                            row["source_sum"] == source_sum and
                            all(root*root % PRIME == source_sum
                                for root in row["sum_roots"]) and
                            all(root*root % PRIME ==
                                (source_sum-4*missing) % PRIME
                                for root in row["delta_roots"]),
                            "audit square-root ledger")
            point_index += 1
    statement = (NODE / "statement.md").read_text()
    require(point_index == 8 and len(endpoint_values) == 2 and
            "generic elliptic" in statement and "3,360" in statement,
            "scope and endpoint totals")
    print("audit=ok points=8 endpoint_profiles=2 square_ledgers=32")


if __name__ == "__main__":
    main()
