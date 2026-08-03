#!/usr/bin/env python3
"""Independent audit of the cell-3 negative-DE exclusion."""

import ast
import collections
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
CUT_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_modal.py"
REPLAY_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_modal.py"
SOLVER_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_modal.py"
SOLVER = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_source(path, snippets):
    source = path.read_text()
    ast.parse(source)
    for snippet in snippets:
        require(snippet in source, f"{path.name}: missing {snippet}")


def main():
    check_source(CUT_SCRIPT, (
        "if xi_index != 2 or pairing_index != 0:",
        "de_record = -missing_record",
        "target_free = paired(de_record, de_record)",
        "target_free_tower_norm = target_free_pair_determinant.norm()",
        "numerator.gcd(pow(variable, PRIME, numerator)-variable)",
    ))
    check_source(REPLAY_SCRIPT, (
        "de_value = -missing_record % PRIME",
        "left, right = de_value, de_value",
        'b_row["source_missing_record"] = missing_record',
        'b_row["de_value"] = de_value',
        '"nonzero_cofactor_indices"',
    ))
    check_source(SOLVER_SCRIPT, (
        "de_value = -source_missing_record % PRIME",
        "a_values, b_values, de_value, de_value",
        "- (u-v)**2*a_missing*a_missing",
        "substitution = de_value*f*f/u",
        "outside_u.gcd(sum_u)",
        'raise ValueError("direct target-equation replay failed")',
    ))

    payload = json.loads(SOLVER.read_text())
    signs = set(itertools.product((-1, 1), repeat=2))
    lanes = set(itertools.product((-1, 1), repeat=2))
    require({tuple(row["epsilon"]) for row in payload["rows"]} == signs,
            "four source signs")
    total_rows = 0
    total_f = 0
    for row in payload["rows"]:
        require(row["case_excluded"] and not row["witnesses"] and
                not row["boundary_solutions"] and not row["unresolved"],
                "finite exclusion")
        require({tuple(item["sigma"]) for item in row["rows"]} == lanes,
                "four target lanes")
        require(collections.Counter(len(item["f_roots"])
                                    for item in row["rows"]) == {0: 4, 2: 4},
                "colored-root partition")
        require(all(entry["u_gcd_degree"] == 0 and entry["u_roots"] == []
                    for item in row["rows"] for entry in item["f_rows"]),
                "coprime residual cuts")
        total_rows += len(row["rows"])
        total_f += sum(len(item["f_roots"]) for item in row["rows"])
    require((total_rows, total_f) == (32, 32), "finite totals")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("target product is `de=-m`" in statement and
            "missing squared-sum row `(d-e)^2`" in proof and
            "Losing this sign" in audit, "sign discipline")
    require("`xi=3,...,6`" in statement and "another matching" in statement,
            "nonclaim boundary")
    print("audit=ok xi=2 pairing=0 de=-m squared_sum=(d-e)^2 raw_cases=16")


if __name__ == "__main__":
    main()
