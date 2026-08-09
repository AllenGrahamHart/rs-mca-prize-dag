#!/usr/bin/env python3
"""Independently replay the cell-5 xi=3 pairings-1/2 certificate."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_"
    "template_adapter_result.json"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_"
    "independent_roots_result.json"
)
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_"
    "reciprocal_linear_modal.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
)
CORE = DIRECTORY / "rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit.py"
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_"
    "direct_audit_result.json"
)
REMOTE_PRIMARY = "/root/primary.json"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell5-xi3-pairings1-2-direct-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRIMARY, REMOTE_PRIMARY)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(CORE, "/root/audit_core.py")
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300)
def audit():
    import sys

    sys.path.insert(0, "/root")
    import sympy as sp

    import audit_core as core

    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    payload = json.loads(Path(REMOTE_PRIMARY).read_text())
    core.require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-adapter-v1"
        and payload["field"] == PRIME
        and payload["source_template_sha256"] == digest(REMOTE_TEMPLATE)
        and payload["source_tower_sha256"] == digest(REMOTE_TOWER)
        and payload["source_kernel_sha256"] == digest(REMOTE_KERNEL),
        "primary custody",
    )

    profiles = {}
    for row in payload["rows"]:
        for item in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = item[side]
                profiles.setdefault(profile["sha256"], profile)
    roots = json.loads(Path(REMOTE_ROOTS).read_text())
    core.require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-independent-roots-v1"
        and roots["field"] == PRIME
        and roots["source_primary_sha256"] == digest(REMOTE_PRIMARY),
        "external root custody",
    )
    root_rows = {row["sha256"]: row for row in roots["rows"]}
    core.require(set(root_rows) == set(profiles), "external root profile cover")
    root_cache = {}
    for key, profile in profiles.items():
        text = profile["expression"]
        core.require(hashlib.sha256(text.encode()).hexdigest() == key,
                     "profile digest")
        coefficients = core.parse_flint(text)
        core.require(
            (max(coefficients, default=-1), len(coefficients))
            == (profile["degree"], profile["terms"]),
            "profile shape",
        )
        checked = root_rows[key]
        core.require(
            (checked["degree"], checked["terms"])
            == (profile["degree"], profile["terms"])
            and checked["roots"] == sorted(set(checked["roots"]))
            and all(core.evaluate_sparse(coefficients, value) == 0
                    for value in checked["roots"]),
            "external root row",
        )
        root_cache[key] = checked["roots"]

    tower = {}
    for row in json.loads(Path(REMOTE_TOWER).read_text())["rows"]:
        if row["c_row_index"] != 6:
            continue
        key = tuple(row["epsilon"])
        core.require(
            key not in tower and row["status"] == "COMPLETE"
            and row["exact"] and row["b_boundary_unit"]
            and row["c_boundary_unit"] and row["b_boundary_dimension"] == -1
            and row["c_boundary_dimension"] == -1
            and row["b_boundary_basis_size"] == 1
            and row["c_boundary_basis_size"] == 1,
            "boundary-free tower custody",
        )
        tower[key] = row
    core.require(len(tower) == 4, "tower sign cover")
    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(item["expression"]) for item in row["kernel"]
        )
        for row in json.loads(Path(REMOTE_KERNEL).read_text())["rows"]
    }
    core.require(len(kernels) == 4, "kernel sign cover")

    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    expected = {
        (epsilon, branch_index, 0, 1)
        for epsilon in signs for branch_index in range(3)
    } | {
        (epsilon, branch_index, sigma_c_anchor, 2)
        for epsilon in signs for branch_index in range(3)
        for sigma_c_anchor in (-1, 1)
    }
    fields = (
        "rows", "profile_visits", "target_norm_root_count",
        "candidate_root_count", "source_point_count", "route_point_count",
        "z_candidate_count", "final_pair_solution_count", "r_boundaries",
        "t_boundaries", "no_lifts", "missing_impossible",
        "product_boundaries", "empty_q_branches", "checked",
        "common_z_roots", "z_lifts", "final_color_nonzero",
        "target_boundaries",
    )
    totals = {field: 0 for field in fields}
    by_pairing = {str(pairing): {field: 0 for field in fields}
                  for pairing in (1, 2)}

    def bump(pairing, field, amount=1):
        totals[field] += amount
        by_pairing[str(pairing)][field] += amount

    seen = set()
    for row in payload["rows"]:
        key = (
            tuple(row["epsilon"]), row["branch_index"],
            row["sigma_c_anchor"], row["pairing_index"],
        )
        core.require(key in expected and key not in seen,
                     "Cartesian row cover")
        seen.add(key)
        epsilon, branch_index, sigma_c_anchor, pairing = key
        expected_lanes = (
            [[-1, -1], [-1, 1], [1, -1], [1, 1]]
            if pairing == 1
            else [[sigma_c_anchor, -1], [sigma_c_anchor, 1]]
        )
        core.require(
            row["status"] == "COMPLETE" and row["target_excluded"]
            and row["xi_index"] == 3 and pairing in (1, 2)
            and row["target_lanes_covered"] == expected_lanes
            and row["remainder_degree"] == 1
            and (row["missing_cut_degree"], row["next_cut_degree"])
            == (4, 2) and row["witness_count"] == 0
            and not row["witnesses"] and not row["unresolved"]
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"],
            "complete result row",
        )
        bump(pairing, "rows")
        target_num = row["target_norm"]["numerator"]
        target_den = row["target_norm"]["denominator"]
        target_roots = [
            value for value in root_cache[target_num["sha256"]]
            if value not in set(root_cache[target_den["sha256"]])
        ]
        core.require(target_roots == row["target_norm_roots"],
                     "target-root replay")
        candidate_roots = set()
        for item in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                candidate_roots.update(root_cache[item[side]["sha256"]])
                bump(pairing, "profile_visits")
        core.require(sorted(candidate_roots) == row["candidate_roots"],
                     "candidate-root union")
        covered = {
            item["r"]
            for name in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[name]
        }
        core.require(covered == candidate_roots, "candidate terminal cover")

        chart = tower[epsilon]
        base_relation = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        core.require(
            base_relation == sp.sympify(chart["base"]["expression"])
            and b_relation == sp.sympify(chart["b_relation"]["expression"])
            and c_relation == sp.sympify(chart["c_relation"]["expression"]),
            "row/tower relation join",
        )
        for item in row["boundary_rows"]:
            if item["stage"] == "R_GUARD":
                core.require(
                    item["r"]
                    in {0, 1, PRIME - 1, core.IOTA, PRIME - core.IOTA},
                    "r boundary",
                )
                bump(pairing, "r_boundaries")
            elif item["stage"] == "T_GUARD":
                rv, tv = item["r"], item["t"]
                core.require(
                    core.value(base_relation, item) == 0
                    and tv * (tv*tv - 1) * (tv*tv + 1)
                    * (tv*tv - rv*rv) * (tv*tv + rv*rv) % PRIME == 0,
                    "t boundary",
                )
                bump(pairing, "t_boundaries")
            else:
                raise RuntimeError(f"unexpected boundary {item['stage']}")
        b_polynomial = sp.Poly(b_relation, core.b)
        for item in row["no_lift_rows"]:
            core.require(item["stage"] == "NO_B_ROOT"
                         and core.value(base_relation, item) == 0,
                         "no-b lift row")
            leading, linear, constant = (
                core.value(coefficient, item)
                for coefficient in b_polynomial.all_coeffs()
            )
            discriminant = (linear*linear - 4*leading*constant) % PRIME
            core.require(
                leading
                and pow(discriminant, (PRIME - 1)//2, PRIME) == PRIME - 1,
                "no-b nonsquare",
            )
            bump(pairing, "no_lifts")

        kernel = kernels[epsilon]
        local_candidates = set()
        local_boundaries = set()
        core.require(
            row["source_point_count"] == row["route_point_count"]
            == len(row["finite_rows"]),
            "source route count",
        )
        for finite in row["finite_rows"]:
            core.require(
                core.value(base_relation, finite)
                == core.value(b_relation, finite)
                == core.value(c_relation, finite) == 0,
                "finite source relations",
            )
            rv, tv, bv, cv = (
                finite[name] for name in ("r", "t", "b", "c")
            )
            guards = (
                bv, cv, rv, tv, bv - 1, bv + 1, cv - 1, cv + 1,
                bv - cv, bv + cv, rv*rv - 1, rv*rv + 1,
                tv*tv - 1, tv*tv + 1, tv*tv - rv*rv, tv*tv + rv*rv,
            )
            core.require(all(value % PRIME for value in guards),
                         "finite route guards")
            point = {core.r: rv, core.t: tv, core.b: bv, core.c: cv}
            values = [int(expression.subs(point)) % PRIME
                      for expression in kernel]
            a_values, b_values = values[:3], values[3:6]
            beta_0, beta_1 = values[6:]
            label = -tv*tv % PRIME
            a_missing = sum(value*pow(label, index, PRIME)
                            for index, value in enumerate(a_values)) % PRIME
            b_missing = sum(value*pow(label, index, PRIME)
                            for index, value in enumerate(b_values)) % PRIME
            if finite["status"] == "MISSING_IMPOSSIBLE":
                core.require(a_missing == 0 and b_missing != 0,
                             "missing-impossible terminal")
                bump(pairing, "missing_impossible")
                continue
            core.require(a_missing != 0, "missing denominator")
            missing = b_missing*pow(a_missing, -1, PRIME) % PRIME
            source_sum = (
                label * pow((beta_0 + beta_1*label) % PRIME, 2, PRIME)
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            core.require((finite["missing"], finite["source_sum"])
                         == (missing, source_sum), "missing-record replay")
            if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                core.require(missing == 0 and finite["z_rows"] == [],
                             "product boundary")
                local_boundaries.add((
                    rv, tv, bv, cv, pairing, branch_index,
                    sigma_c_anchor, finite["status"],
                ))
                bump(pairing, "product_boundaries")
                continue
            a_branch = a_values[branch_index]
            b_branch = b_values[branch_index]
            core.require((finite["a_branch"], finite["b_branch"])
                         == (a_branch, b_branch), "q-branch values")
            if finite["status"] == "EMPTY_Q_BRANCH":
                core.require(a_branch == 0 and b_branch != 0
                             and finite["z_rows"] == [], "empty q branch")
                bump(pairing, "empty_q_branches")
                continue
            core.require(finite["status"] == "CHECKED" and a_branch != 0,
                         "checked source terminal")
            bump(pairing, "checked")
            q_value = b_branch*pow(a_branch, -1, PRIME) % PRIME
            same_pair_cut = core.paired(a_values, b_values, q_value, q_value)
            core.require((finite["q"], finite["same_pair_cut"])
                         == (q_value, same_pair_cut) and same_pair_cut == 0,
                         "q branch paired cut")
            missing_roots = core.even_quartic_roots(
                [1, 0, (2*missing - source_sum) % PRIME, 0,
                 missing*missing],
                "missing reciprocal-linear cut",
            )
            next_scale = (
                bv*missing if pairing == 1
                else sigma_c_anchor*cv*missing
            ) % PRIME
            next_coefficients = core.paired_coefficients(
                a_values, b_values, -q_value % PRIME, next_scale,
            )
            next_roots = (
                None if not any(next_coefficients)
                else core.quadratic_roots(
                    next_coefficients, "next reciprocal-linear cut"
                )
            )
            common_roots = (
                missing_roots if next_roots is None
                else sorted(set(missing_roots) & set(next_roots))
            )
            core.require(
                finite["missing_z_roots"] == missing_roots
                and finite["next_z_roots"] == next_roots
                and finite["common_z_roots"] == common_roots,
                "common-z root replay",
            )
            bump(pairing, "common_z_roots", len(common_roots))
            reported_z = {item["z"]: item for item in finite["z_rows"]}
            core.require(set(reported_z) == set(common_roots),
                         "complete common-z ledger")
            for z_value in common_roots:
                z_row = reported_z[z_value]
                relation = (
                    1 + (2*missing - source_sum)*z_value*z_value
                    + missing*missing*pow(z_value, 4, PRIME)
                ) % PRIME
                core.require(relation == 0 and z_value != 0,
                             "missing z relation")
                d_value = pow(z_value, -1, PRIME)
                e_value = q_value*z_value % PRIME
                f_value = missing*z_value % PRIME
                next_right = (
                    bv*f_value if pairing == 1
                    else sigma_c_anchor*cv*f_value
                ) % PRIME
                next_pair_cut = core.paired(
                    a_values, b_values, -q_value % PRIME, next_right,
                )
                core.require(
                    (z_row["d"], z_row["e"], z_row["f"],
                     z_row["next_pair_cut"])
                    == (d_value, e_value, f_value, next_pair_cut)
                    and d_value*e_value % PRIME == q_value
                    and d_value*f_value % PRIME == missing
                    and next_pair_cut == 0,
                    "z/d/e/f lift replay",
                )
                local_candidates.add((
                    rv, tv, bv, cv, pairing, branch_index, sigma_c_anchor,
                    q_value, z_value, d_value, e_value, f_value,
                ))
                bump(pairing, "z_lifts")
                lanes = {tuple(item["sigma"]): item
                         for item in z_row["lanes"]}
                expected_lane_set = (
                    {(-1, -1), (-1, 1), (1, -1), (1, 1)}
                    if pairing == 1
                    else {(sigma_c_anchor, -1), (sigma_c_anchor, 1)}
                )
                core.require(set(lanes) == expected_lane_set,
                             "colored lane cover")
                for sigma_c, sigma_o in expected_lane_set:
                    lane = lanes[(sigma_c, sigma_o)]
                    final_left, final_right = (
                        (sigma_o*e_value*f_value, sigma_c*cv*f_value)
                        if pairing == 1
                        else (sigma_o*e_value*f_value, bv*f_value)
                    )
                    final_pair_cut = core.paired(
                        a_values, b_values, final_left % PRIME,
                        final_right % PRIME,
                    )
                    core.require(
                        lane["final_pair_cut"] == final_pair_cut
                        and final_pair_cut != 0
                        and lane["status"] == "THIRD_PAIR_NONZERO",
                        "final colored-pair terminal",
                    )
                    bump(pairing, "final_color_nonzero")
        reported_candidates = {
            tuple(item[name] for name in (
                "r", "t", "b", "c", "pairing_index", "branch_index",
                "sigma_c_anchor", "q", "z", "d", "e", "f",
            ))
            for item in row["z_candidates"]
        }
        core.require(reported_candidates == local_candidates,
                     "z-candidate ledger")
        reported_boundaries = {
            (item["r"], item["t"], item["b"], item["c"],
             item["pairing_index"], item["branch_index"],
             item["sigma_c_anchor"], item["status"])
            for item in row["target_boundary_rows"]
        }
        core.require(reported_boundaries == local_boundaries,
                     "target-boundary ledger")
        for field in (
            "target_norm_root_count", "candidate_root_count",
            "source_point_count", "route_point_count", "z_candidate_count",
            "final_pair_solution_count",
        ):
            bump(pairing, field, row[field])
        bump(pairing, "target_boundaries", len(local_boundaries))
    core.require(seen == expected, "complete Cartesian cover")
    return {
        "schema": (
            "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-"
            "direct-audit-v1"
        ),
        "field": PRIME,
        "source_primary_sha256": digest(REMOTE_PRIMARY),
        "source_roots_sha256": digest(REMOTE_ROOTS),
        "source_template_sha256": digest(REMOTE_TEMPLATE),
        "source_tower_sha256": digest(REMOTE_TOWER),
        "source_kernel_sha256": digest(REMOTE_KERNEL),
        "profiles": len(profiles),
        "pairing_totals": by_pairing,
        **totals,
        "status": "PASS",
    }


@app.local_entrypoint()
def main():
    output = audit.remote()
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, sort_keys=True))
