#!/usr/bin/env python3
"""Replay the cell-9 xi=3 pairing-0 certificate independently."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_chart_result"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_"
    "frobenius_roots_result.json"
)
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_modal.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_four_basis_tower_result.json"
)
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
)
BASE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
)
CORE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit.py"
)
SHARDED = (
    DIRECTORY.parents[1] / "tools/sharded_result.py"
    if DIRECTORY.name == "prize_resolution"
    else Path("/root/sharded_result.py")
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_"
    "direct_audit_result.json"
)
REMOTE_PRIMARY = "/root/primary"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_BASE = "/root/base.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-xi3-pairing0-direct-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_dir(PRIMARY, REMOTE_PRIMARY)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(BASE, REMOTE_BASE)
    .add_local_file(CORE, "/root/audit_core.py")
    .add_local_file(SHARDED, "/root/sharded_result.py")
)


@app.function(
    image=image, cpu=1.0, memory=2048, timeout=300, max_containers=6
)
def audit(chart_case):
    import sys

    sys.path.insert(0, "/root")
    import sympy as sp

    import audit_core as core
    from sharded_result import iter_records, verify

    chart_case = tuple(chart_case)
    manifest = Path(REMOTE_PRIMARY) / "manifest.json"
    counts = verify(manifest)
    manifest_payload = json.loads(manifest.read_text())

    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    expected_metadata = {
        "field": PRIME,
        "scope": (
            "Exact six-chart execution of the pinned reciprocal-square "
            "compiler for cell-9 xi=3, pairing=0."
        ),
        "source_template_sha256": digest(REMOTE_TEMPLATE),
        "source_tower_sha256": digest(REMOTE_TOWER),
        "source_kernel_sha256": digest(REMOTE_KERNEL),
        "source_base_sha256": digest(REMOTE_BASE),
    }
    for key, value in expected_metadata.items():
        core.require(
            manifest_payload["metadata"].get(key) == value,
            f"manifest metadata {key}",
        )

    profiles = {}
    for row in iter_records(manifest):
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    roots = json.loads(Path(REMOTE_ROOTS).read_text())
    core.require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell9-xi3-pairing0-frobenius-roots-v1"
        and roots["field"] == PRIME
        and roots["method"]
        == "external FLINT gcd(P,x^p-x), factor squarefree root part"
        and roots["source_manifest_sha256"] == digest(manifest)
        and roots["source_sharded_counts"] == counts,
        "external root custody",
    )
    root_rows = {row["sha256"]: row for row in roots["rows"]}
    core.require(set(root_rows) == set(profiles), "external root profile cover")
    root_cache = {}
    for key, profile in profiles.items():
        text = profile["expression"]
        core.require(
            hashlib.sha256(text.encode()).hexdigest() == key,
            "profile digest",
        )
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
            and checked["frobenius_root_degree"] == len(checked["roots"])
            and checked["roots"] == sorted(set(checked["roots"]))
            and all(
                core.evaluate_sparse(coefficients, value) == 0
                for value in checked["roots"]
            ),
            "external root row",
        )
        root_cache[key] = checked["roots"]

    tower_payload = json.loads(Path(REMOTE_TOWER).read_text())
    tower = {}
    for row in tower_payload["rows"]:
        key = (tuple(row["epsilon"]), row["b_row_index"], row["c_row_index"])
        core.require(
            key not in tower
            and row["status"] == "COMPLETE"
            and row["exact"]
            and row["b_cover_complete"]
            and row["c_cover_complete"]
            and row["b_cover_boundary_dimension"] == -1
            and row["c_cover_boundary_dimension"] == -1
            and row["b_cover_boundary_basis_size"] == 1
            and row["c_cover_boundary_basis_size"] == 1,
            "tower chart custody",
        )
        tower[key] = row
    core.require(len(tower) == 24, "six-chart tower cover")

    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(item["expression"]) for item in row["kernel"]
        )
        for row in json.loads(Path(REMOTE_KERNEL).read_text())["rows"]
    }
    core.require(len(kernels) == 4, "kernel sign cover")

    regularized = set()
    for row in json.loads(Path(REMOTE_BASE).read_text())["rows"]:
        point = tuple(row["point"][name] for name in ("r", "t", "b", "c"))
        relevant = [
            item
            for item in row["rows"]
            if item["pairing_index"] == 0 and item["xi_index"] == 3
        ]
        core.require(
            row["status"] == "COMPLETE"
            and row["section_is_zero"]
            and row["point"]["guard_nonzero"]
            and not row["nonunit_systems"]
            and len(relevant) == 1
            and relevant[0]["unit"]
            and relevant[0]["dimension"] == -1
            and relevant[0]["basis_size"] == 1,
            "regularized base custody",
        )
        regularized.add((tuple(row["epsilon"]), point))
    core.require(len(regularized) == 8, "regularized base cover")

    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    selected_b, selected_c = chart_case
    expected = {
        (epsilon, branch_index, sigma_o, selected_b, selected_c)
        for epsilon in signs
        for branch_index in range(3)
        for sigma_o in (-1, 1)
    }
    seen = set()
    totals = {
        key: 0
        for key in (
            "target_norm_root_count",
            "candidate_root_count",
            "source_point_count",
            "route_point_count",
            "yd_candidate_count",
            "final_pair_solution_count",
            "r_boundaries",
            "t_boundaries",
            "no_lifts",
            "missing_impossible",
            "missing_free",
            "product_boundaries",
            "empty_q_branches",
            "checked",
            "common_y_roots",
            "d_lifts",
            "third_pair_nonzero",
            "chart_b_paid",
            "chart_c_paid",
            "regularized_paid",
            "target_boundaries",
        )
    }
    profile_visits = 0
    for row in iter_records(manifest):
        if (row["b_row_index"], row["c_row_index"]) != chart_case:
            continue
        key = (
            tuple(row["epsilon"]),
            row["branch_index"],
            row["sigma_o"],
            row["b_row_index"],
            row["c_row_index"],
        )
        core.require(key in expected and key not in seen, "Cartesian row cover")
        seen.add(key)
        epsilon, branch_index, sigma_o, b_index, c_index = key
        chart = tower[(epsilon, b_index, c_index)]
        core.require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 0
            and (row["missing_cut_degree"], row["outside_cut_degree"])
            == (2, 2)
            and not row["witnesses"]
            and not row["unresolved"]
            and not row["final_pair_solutions"],
            "complete result row",
        )
        target_num = row["target_norm"]["numerator"]
        target_den = row["target_norm"]["denominator"]
        target_roots = [
            value
            for value in root_cache[target_num["sha256"]]
            if value not in set(root_cache[target_den["sha256"]])
        ]
        core.require(
            target_roots == row["target_norm_roots"], "target-root replay"
        )
        candidate_roots = set()
        for item in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                candidate_roots.update(root_cache[item[side]["sha256"]])
                profile_visits += 1
        core.require(
            sorted(candidate_roots) == row["candidate_roots"],
            "candidate-root union",
        )
        covered = {
            item["r"]
            for field in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[field]
        }
        core.require(covered == candidate_roots, "candidate terminal cover")

        base_relation = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        core.require(
            base_relation == sp.sympify(chart["base"]["expression"])
            and b_relation == sp.sympify(chart["b_relation"]["expression"])
            and c_relation == sp.sympify(chart["c_relation"]["expression"]),
            "row/chart relation join",
        )
        for item in row["boundary_rows"]:
            if item["stage"] == "R_GUARD":
                core.require(
                    item["r"]
                    in {0, 1, PRIME - 1, core.IOTA, PRIME - core.IOTA},
                    "r boundary",
                )
                totals["r_boundaries"] += 1
            elif item["stage"] == "T_GUARD":
                rv, tv = item["r"], item["t"]
                core.require(
                    core.value(base_relation, item) == 0
                    and tv
                    * (tv * tv - 1)
                    * (tv * tv + 1)
                    * (tv * tv - rv * rv)
                    * (tv * tv + rv * rv)
                    % PRIME
                    == 0,
                    "t boundary",
                )
                totals["t_boundaries"] += 1
            else:
                raise RuntimeError(f"unexpected boundary {item['stage']}")
        b_polynomial = sp.Poly(b_relation, core.b)
        for item in row["no_lift_rows"]:
            core.require(
                item["stage"] == "NO_B_ROOT"
                and core.value(base_relation, item) == 0,
                "no-b lift row",
            )
            leading, linear, constant = (
                core.value(coefficient, item)
                for coefficient in b_polynomial.all_coeffs()
            )
            discriminant = (linear * linear - 4 * leading * constant) % PRIME
            core.require(
                leading
                and pow(discriminant, (PRIME - 1) // 2, PRIME) == PRIME - 1,
                "no-b nonsquare",
            )
            totals["no_lifts"] += 1

        paid_base_points = set()
        for item in row["paid_rows"]:
            if item["stage"] == "CHART_B_LEADING":
                core.require(
                    item["reason"] == "FREE_B"
                    and core.value(base_relation, item) == 0
                    and core.value(
                        sp.sympify(chart["b_leading"]["expression"]), item
                    )
                    == 0,
                    "b-leading payment",
                )
                totals["chart_b_paid"] += 1
            elif item["stage"] == "CHART_C_LEADING":
                core.require(
                    item["reason"] == "FREE_C"
                    and core.value(base_relation, item) == 0
                    and core.value(b_relation, item) == 0
                    and core.value(
                        sp.sympify(chart["c_leading"]["expression"]), item
                    )
                    == 0,
                    "c-leading payment",
                )
                totals["chart_c_paid"] += 1
            elif item["stage"] == "REGULARIZED_BASE":
                point = tuple(item[name] for name in ("r", "t", "b", "c"))
                core.require(
                    item["reason"] == "MISSING_FREE"
                    and (epsilon, point) in regularized
                    and core.value(base_relation, item) == 0
                    and core.value(b_relation, item) == 0
                    and core.value(c_relation, item) == 0,
                    "regularized-base payment",
                )
                paid_base_points.add(point)
                totals["regularized_paid"] += 1
            else:
                raise RuntimeError(f"unexpected payment {item}")

        kernel = kernels[epsilon]
        local_candidates = set()
        local_boundaries = set()
        local_missing_free = set()
        core.require(
            row["source_point_count"]
            == row["route_point_count"]
            == len(row["finite_rows"]),
            "source route count",
        )
        for finite in row["finite_rows"]:
            core.require(
                core.value(base_relation, finite)
                == core.value(b_relation, finite)
                == core.value(c_relation, finite)
                == 0,
                "finite source relations",
            )
            rv, tv, bv, cv = (
                finite[name] for name in ("r", "t", "b", "c")
            )
            guards = (
                bv,
                cv,
                rv,
                tv,
                bv - 1,
                bv + 1,
                cv - 1,
                cv + 1,
                bv - cv,
                bv + cv,
                rv * rv - 1,
                rv * rv + 1,
                tv * tv - 1,
                tv * tv + 1,
                tv * tv - rv * rv,
                tv * tv + rv * rv,
            )
            core.require(
                all(value % PRIME for value in guards), "finite route guards"
            )
            point = {core.r: rv, core.t: tv, core.b: bv, core.c: cv}
            values = [int(expression.subs(point)) % PRIME for expression in kernel]
            a_values, b_values = values[:3], values[3:6]
            beta_0, beta_1 = values[6:]
            label = -tv * tv % PRIME
            a_missing = sum(
                value * pow(label, index, PRIME)
                for index, value in enumerate(a_values)
            ) % PRIME
            b_missing = sum(
                value * pow(label, index, PRIME)
                for index, value in enumerate(b_values)
            ) % PRIME
            if finite["status"] == "MISSING_IMPOSSIBLE":
                core.require(
                    a_missing == 0 and b_missing != 0,
                    "missing-impossible terminal",
                )
                totals["missing_impossible"] += 1
                continue
            if finite["status"] == "MISSING_FREE":
                point_key = (rv, tv, bv, cv)
                core.require(
                    a_missing == b_missing == 0
                    and point_key in paid_base_points,
                    "missing-free terminal",
                )
                local_missing_free.add(point_key)
                totals["missing_free"] += 1
                continue
            core.require(a_missing != 0, "missing denominator")
            missing = b_missing * pow(a_missing, -1, PRIME) % PRIME
            source_sum = (
                label
                * pow((beta_0 + beta_1 * label) % PRIME, 2, PRIME)
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            core.require(
                (finite["missing"], finite["source_sum"])
                == (missing, source_sum),
                "missing-record replay",
            )
            if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                core.require(
                    missing == 0 and finite["yd_rows"] == [],
                    "product boundary",
                )
                local_boundaries.add(
                    (rv, tv, bv, cv, branch_index, sigma_o, finite["status"])
                )
                totals["product_boundaries"] += 1
                continue
            a_branch = a_values[branch_index]
            b_branch = b_values[branch_index]
            core.require(
                (finite["a_branch"], finite["b_branch"])
                == (a_branch, b_branch),
                "q-branch values",
            )
            if finite["status"] == "EMPTY_Q_BRANCH":
                core.require(
                    a_branch == 0 and b_branch != 0 and finite["yd_rows"] == [],
                    "empty q branch",
                )
                totals["empty_q_branches"] += 1
                continue
            core.require(
                finite["status"] == "CHECKED" and a_branch != 0,
                "checked source terminal",
            )
            totals["checked"] += 1
            q_value = b_branch * pow(a_branch, -1, PRIME) % PRIME
            same_pair_cut = core.paired(a_values, b_values, q_value, q_value)
            core.require(
                (finite["q"], finite["same_pair_cut"])
                == (q_value, same_pair_cut)
                and same_pair_cut == 0,
                "q branch paired cut",
            )
            missing_roots = core.quadratic_roots(
                [1, (2 * missing - source_sum) % PRIME, missing * missing],
                "missing reciprocal-square cut",
            )
            outside_coefficients = core.paired_coefficients(
                a_values,
                b_values,
                -q_value % PRIME,
                sigma_o * q_value * missing % PRIME,
            )
            outside_roots = (
                None
                if not any(outside_coefficients)
                else core.quadratic_roots(
                    outside_coefficients, "outside reciprocal-square cut"
                )
            )
            common_roots = (
                missing_roots
                if outside_roots is None
                else sorted(set(missing_roots) & set(outside_roots))
            )
            core.require(
                finite["missing_y_roots"] == missing_roots
                and finite["outside_y_roots"] == outside_roots
                and finite["common_y_roots"] == common_roots,
                "common-y root replay",
            )
            totals["common_y_roots"] += len(common_roots)
            reported_y = {item["y"]: item for item in finite["yd_rows"]}
            core.require(
                set(reported_y) == set(common_roots), "complete common-y ledger"
            )
            for y_value in common_roots:
                y_row = reported_y[y_value]
                relation = (
                    1
                    + (2 * missing - source_sum) * y_value
                    + missing * missing * y_value * y_value
                ) % PRIME
                core.require(relation == 0 and y_value != 0, "missing y relation")
                d_squared = pow(y_value, -1, PRIME)
                d_roots = core.quadratic_roots(
                    [-d_squared % PRIME, 0, 1], "reciprocal-square lift"
                )
                core.require(
                    y_row["d_squared"] == d_squared
                    and y_row["d_roots"] == d_roots,
                    "d-root replay",
                )
                reported_d = {item["d"]: item for item in y_row["d_rows"]}
                core.require(set(reported_d) == set(d_roots), "complete d ledger")
                for d_value in d_roots:
                    d_row = reported_d[d_value]
                    inverse_d = pow(d_value, -1, PRIME)
                    e_value = q_value * inverse_d % PRIME
                    f_value = missing * inverse_d % PRIME
                    outside_pair_cut = core.paired(
                        a_values,
                        b_values,
                        -q_value % PRIME,
                        sigma_o * e_value * f_value % PRIME,
                    )
                    core.require(
                        (d_row["e"], d_row["f"], d_row["outside_pair_cut"])
                        == (e_value, f_value, outside_pair_cut)
                        and d_value * d_value % PRIME == d_squared
                        and outside_pair_cut == 0,
                        "d/e/f lift replay",
                    )
                    local_candidates.add(
                        (
                            rv,
                            tv,
                            bv,
                            cv,
                            branch_index,
                            sigma_o,
                            q_value,
                            y_value,
                            d_value,
                            e_value,
                            f_value,
                        )
                    )
                    totals["d_lifts"] += 1
                    lanes = {tuple(item["sigma"]): item for item in d_row["lanes"]}
                    core.require(
                        set(lanes) == {(-1, sigma_o), (1, sigma_o)},
                        "two-color lane cover",
                    )
                    for sigma_c in (-1, 1):
                        lane = lanes[(sigma_c, sigma_o)]
                        final_pair_cut = core.paired(
                            a_values,
                            b_values,
                            bv * f_value % PRIME,
                            sigma_c * cv * f_value % PRIME,
                        )
                        core.require(
                            lane["final_pair_cut"] == final_pair_cut
                            and final_pair_cut != 0
                            and lane["status"] == "THIRD_PAIR_NONZERO",
                            "final colored-pair terminal",
                        )
                        totals["third_pair_nonzero"] += 1
        core.require(
            local_missing_free == paid_base_points,
            "regularized payment exactness",
        )
        reported_candidates = {
            tuple(
                item[name]
                for name in (
                    "r",
                    "t",
                    "b",
                    "c",
                    "branch_index",
                    "sigma_o",
                    "q",
                    "y",
                    "d",
                    "e",
                    "f",
                )
            )
            for item in row["yd_candidates"]
        }
        core.require(
            reported_candidates == local_candidates, "yd-candidate ledger"
        )
        reported_boundaries = {
            (
                item["r"],
                item["t"],
                item["b"],
                item["c"],
                item["branch_index"],
                item["sigma_o"],
                item["status"],
            )
            for item in row["target_boundary_rows"]
        }
        core.require(
            reported_boundaries == local_boundaries, "target-boundary ledger"
        )
        for field in (
            "target_norm_root_count",
            "candidate_root_count",
            "source_point_count",
            "route_point_count",
            "yd_candidate_count",
            "final_pair_solution_count",
        ):
            totals[field] += row[field]
        totals["target_boundaries"] += len(local_boundaries)
    core.require(
        seen == expected and counts["records"] == 144,
        "complete Cartesian cover",
    )
    return {
        "schema": (
            "rate-half-kb-positive-433-1b-cell9-xi3-pairing0-"
            "direct-audit-v1"
        ),
        "field": PRIME,
        "source_manifest_sha256": digest(manifest),
        "source_roots_sha256": digest(REMOTE_ROOTS),
        "source_template_sha256": digest(REMOTE_TEMPLATE),
        "source_tower_sha256": digest(REMOTE_TOWER),
        "source_kernel_sha256": digest(REMOTE_KERNEL),
        "source_base_sha256": digest(REMOTE_BASE),
        "sharded_counts": counts,
        "chart": list(chart_case),
        "rows": len(seen),
        "profiles": len(profiles),
        "profile_visits": profile_visits,
        **totals,
        "status": "PASS",
    }


@app.local_entrypoint()
def main():
    charts = tuple(
        (b_index, c_index)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    )
    chart_rows = list(audit.map(charts, order_outputs=True))
    if [tuple(row["chart"]) for row in chart_rows] != list(charts):
        raise RuntimeError("chart audit cover")
    shared_fields = (
        "schema",
        "field",
        "source_manifest_sha256",
        "source_roots_sha256",
        "source_template_sha256",
        "source_tower_sha256",
        "source_kernel_sha256",
        "source_base_sha256",
        "sharded_counts",
        "profiles",
        "status",
    )
    for field in shared_fields:
        if len(
            {json.dumps(row[field], sort_keys=True) for row in chart_rows}
        ) != 1:
            raise RuntimeError(f"chart audit disagreement: {field}")
    summed = (
        "rows",
        "profile_visits",
        "target_norm_root_count",
        "candidate_root_count",
        "source_point_count",
        "route_point_count",
        "yd_candidate_count",
        "final_pair_solution_count",
        "r_boundaries",
        "t_boundaries",
        "no_lifts",
        "missing_impossible",
        "missing_free",
        "product_boundaries",
        "empty_q_branches",
        "checked",
        "common_y_roots",
        "d_lifts",
        "third_pair_nonzero",
        "chart_b_paid",
        "chart_c_paid",
        "regularized_paid",
        "target_boundaries",
    )
    output = {field: chart_rows[0][field] for field in shared_fields}
    output.update(
        {field: sum(row[field] for row in chart_rows) for field in summed}
    )
    output["chart_rows"] = chart_rows
    if output["rows"] != 144:
        raise RuntimeError("aggregate row cover")
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, sort_keys=True))
