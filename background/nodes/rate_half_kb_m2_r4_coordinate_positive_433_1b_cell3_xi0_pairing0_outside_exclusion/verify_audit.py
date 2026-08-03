#!/usr/bin/env python3
"""Independent audit of the cell-3 xi0/pairing0 exclusion packet."""

import ast
import collections
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
PILOT_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_pilot_modal.py"
PILOT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_census_result.json"
REPLAY_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_modal.py"
REPLAY = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_census_result.json"
SOLVER_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi0_pairing0_outside_solver_modal.py"
SOLVER = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi0_pairing0_outside_solver_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_source(path, snippets):
    source = path.read_text()
    ast.parse(source)
    for snippet in snippets:
        require(snippet in source, f"{path.name}: missing {snippet}")


def main():
    check_source(PILOT_SCRIPT, (
        "if xi_index != 0 or pairing_index != 0:",
        "base_field = sp.GF(PRIME).frac_field(r)",
        "inverse, _, gcd = sp.gcdex(polynomial, base_modulus)",
        "basis = tuple(Pair(value) for value in cubic_basis)",
        "columns = [(self*value).vector() for value in basis]",
        "target_free = paired(missing_record, -missing_record)",
        "target_free_tower_norm = target_free_pair_determinant.norm()",
        "if not field_equal(target_free_norm, target_free_tower_norm):",
        "numerator.gcd(pow(variable, PRIME, numerator)-variable)",
    ))
    check_source(REPLAY_SCRIPT, (
        '"r2_minus_1": r_value*r_value-1',
        '"t2_plus_r2": t_value*t_value+r_value*r_value',
        '"b_plus_c": b_value+c_value',
        "cofactor_terms = [",
        '"nonzero_cofactor_indices"',
        "left, right = missing_record, -missing_record % PRIME",
        '"TARGET_FREE_ZERO" if target_free == 0',
    ))
    check_source(SOLVER_SCRIPT, (
        "def target_guards(representatives):",
        "de_value*f*f-u*v",
        "a_values, b_values, u, sigma_o*v",
        "a_values, b_values, b_value*f, sigma_c*c_value*f",
        "f*f*missing_label",
        "substitution = de_value*f*f/u",
        "outside_u.gcd(sum_u)",
        'raise ValueError("direct target-equation replay failed")',
    ))

    pilot = json.loads(PILOT.read_text())
    replay = json.loads(REPLAY.read_text())
    solver = json.loads(SOLVER.read_text())
    signs = set(itertools.product((-1, 1), repeat=2))
    lanes = set(itertools.product((-1, 1), repeat=2))
    require({tuple(row["epsilon"]) for row in pilot["rows"]} == signs,
            "pilot sign cover")
    require({tuple(row["epsilon"]) for row in replay["rows"]} == signs,
            "replay sign cover")
    require({tuple(row["epsilon"]) for row in solver["rows"]} == signs,
            "solver sign cover")

    total_rows = 0
    total_f = 0
    for row in solver["rows"]:
        require(row["case_excluded"] and not row["witnesses"] and
                not row["boundary_solutions"] and not row["unresolved"],
                "unconditional finite exclusion")
        require({tuple(item["sigma"]) for item in row["rows"]} == lanes,
                "four target lanes")
        counts = collections.Counter(len(item["f_roots"])
                                     for item in row["rows"])
        require(counts == {0: 12, 4: 4}, "colored-root partition")
        require(all(
            entry["u_gcd_degree"] == 0 and entry["u_roots"] == []
            for item in row["rows"] for entry in item["f_rows"]
        ), "all residual u cuts coprime")
        total_rows += len(row["rows"])
        total_f += sum(len(item["f_roots"]) for item in row["rows"])
    require((total_rows, total_f) == (64, 64), "finite totals")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("does not cover `xi=1,...,6`" in statement and
            "necessary target-free equation" in proof and
            "only `16` raw outside cases" in audit and
            "Do not build a dense" in frontier,
            "scope and no-go documentation")
    print("audit=ok xi=0 pairing=0 signs=4 lanes=4 raw_cases=16")


if __name__ == "__main__":
    main()
