#!/usr/bin/env python3
"""Replay the cell-9 xi=3 pairing-5 certificate independently."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_chart_result"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_"
    "frobenius_roots_result.json"
)
TEMPLATE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing5_"
    "nested_signfree_modal.py"
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
    "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_"
    "direct_audit_result.json"
)
REMOTE_PRIMARY = "/root/primary"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TEMPLATE = "/root/template.py"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_BASE = "/root/base.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-xi3-pairing5-direct-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0", "python-flint==0.8.0")
    .add_local_dir(PRIMARY, REMOTE_PRIMARY)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TEMPLATE, REMOTE_TEMPLATE)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(BASE, REMOTE_BASE)
    .add_local_file(CORE, "/root/audit_core.py")
    .add_local_file(SHARDED, "/root/sharded_result.py")
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300, max_containers=6)
def audit(chart_case):
    import sys

    sys.path.insert(0, "/root")
    from flint import fmpz_mod_poly_ctx
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
            "Exact six-chart execution of the pinned nested sign-free "
            "compiler for cell-9 xi=3, pairing=5."
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
        == "rate-half-kb-positive-433-1b-cell9-xi3-pairing5-frobenius-roots-v1"
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
        core.require(hashlib.sha256(text.encode()).hexdigest() == key, "profile digest")
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

    tower = {}
    for row in json.loads(Path(REMOTE_TOWER).read_text())["rows"]:
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
            if item["pairing_index"] == 5 and item["xi_index"] == 3
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

    context = fmpz_mod_poly_ctx(PRIME)

    def trim(values):
        values = [int(value) % PRIME for value in values]
        while values and values[-1] == 0:
            values.pop()
        return values

    def poly_sub(left, right):
        return trim([
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
            for index in range(max(len(left), len(right)))
        ])

    def poly_mul(left, right):
        output = [0] * (len(left) + len(right) - 1)
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                output[i + j] = (output[i + j] + left_value * right_value) % PRIME
        return trim(output)

    def paired_coefficients(a_values, b_values, left_scale, right_scale):
        p = [
            [b_value, -left_scale * a_value]
            for a_value, b_value in zip(a_values, b_values)
        ]
        q = [
            [b_values[0], -right_scale * a_values[0]],
            [-b_values[1], right_scale * a_values[1]],
            [b_values[2], -right_scale * a_values[2]],
        ]
        first = poly_sub(poly_mul(p[2], q[0]), poly_mul(p[0], q[2]))
        second = poly_sub(poly_mul(p[2], q[1]), poly_mul(p[1], q[2]))
        third = poly_sub(poly_mul(p[1], q[0]), poly_mul(p[0], q[1]))
        return poly_sub(poly_mul(first, first), poly_mul(second, third))

    def paired_left_coefficients(a_values, b_values, right):
        p = [
            [b_value, -a_value]
            for a_value, b_value in zip(a_values, b_values)
        ]
        q = [
            [b_values[0] - right * a_values[0]],
            [-b_values[1] + right * a_values[1]],
            [b_values[2] - right * a_values[2]],
        ]
        first = poly_sub(poly_mul(p[2], q[0]), poly_mul(p[0], q[2]))
        second = poly_sub(poly_mul(p[2], q[1]), poly_mul(p[1], q[2]))
        third = poly_sub(poly_mul(p[1], q[0]), poly_mul(p[0], q[1]))
        return poly_sub(poly_mul(first, first), poly_mul(second, third))

    def field_roots(coefficients, label):
        coefficients = trim(coefficients)
        if not coefficients:
            return None
        polynomial = context(coefficients)
        if polynomial.degree() == 0:
            return []
        x_value = context([0, 1])
        root_part = polynomial.gcd(pow(x_value, PRIME, polynomial) - x_value)
        _, factors = root_part.factor()
        output = []
        for factor, multiplicity in factors:
            core.require(
                int(factor.degree()) == 1 and int(multiplicity) == 1,
                f"{label} squarefree linear root part",
            )
            output.append(
                -int(factor[0]) * pow(int(factor[1]), -1, PRIME) % PRIME
            )
        output = sorted(output)
        core.require(
            len(output) == int(root_part.degree())
            and all(polynomial(value) == 0 for value in output),
            f"{label} root census",
        )
        return output

    def intersect(left, right):
        if left is None:
            return right
        if right is None:
            return left
        return sorted(set(left) & set(right))

    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    selected_b, selected_c = chart_case
    expected = {
        (epsilon, sigma_c, selected_b, selected_c)
        for epsilon in signs
        for sigma_c in (-1, 1)
    }
    seen = set()
    total_names = (
        "target_norm_root_count",
        "candidate_root_count",
        "source_point_count",
        "route_point_count",
        "z_candidate_count",
        "q_candidate_count",
        "final_pair_solution_count",
        "r_boundaries",
        "t_boundaries",
        "no_lifts",
        "missing_impossible",
        "missing_free",
        "product_boundaries",
        "checked",
        "missing_z_roots",
        "d_lifts",
        "q_intersections",
        "common_q_roots",
        "lane_checks",
        "third_pair_nonzero",
        "chart_b_paid",
        "chart_c_paid",
        "regularized_paid",
        "target_boundaries",
    )
    totals = {name: 0 for name in total_names}
    profile_visits = 0

    for row in iter_records(manifest):
        if (row["b_row_index"], row["c_row_index"]) != chart_case:
            continue
        key = (
            tuple(row["epsilon"]),
            row["sigma_c"],
            row["b_row_index"],
            row["c_row_index"],
        )
        core.require(key in expected and key not in seen, "Cartesian row cover")
        seen.add(key)
        epsilon, sigma_c, b_index, c_index = key
        chart = tower[(epsilon, b_index, c_index)]
        core.require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 5
            and row["missing_cut_degree"] == 2
            and row["antipodal_u_degree"] == 2
            and row["second_target_z_degree"] == 8
            and row["z_sign_free_degree"] == 3
            and row["remainder_z_degree"] == 3
            and row["remainder_u_z_degrees"] == [4, 4]
            and row["remainder_degree"] == 1
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
        core.require(target_roots == row["target_norm_roots"], "target-root replay")
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
                    item["r"] in {0, 1, PRIME - 1, core.IOTA, PRIME - core.IOTA},
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
                    and core.value(sp.sympify(chart["b_leading"]["expression"]), item)
                    == 0,
                    "b-leading payment",
                )
                totals["chart_b_paid"] += 1
            elif item["stage"] == "CHART_C_LEADING":
                core.require(
                    item["reason"] == "FREE_C"
                    and core.value(base_relation, item) == 0
                    and core.value(b_relation, item) == 0
                    and core.value(sp.sympify(chart["c_leading"]["expression"]), item)
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
        local_z_candidates = set()
        local_q_candidates = set()
        local_missing_free = set()
        local_product_boundaries = set()
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
            core.require(all(value % PRIME for value in guards), "finite route guards")
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
                core.require(a_missing == 0 and b_missing != 0, "missing impossible")
                totals["missing_impossible"] += 1
                continue
            if finite["status"] == "MISSING_FREE":
                point_key = (rv, tv, bv, cv)
                core.require(
                    a_missing == b_missing == 0 and point_key in paid_base_points,
                    "missing free",
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
                (finite["missing"], finite["source_sum"]) == (missing, source_sum),
                "missing-record replay",
            )
            if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                core.require(missing == 0 and finite["z_rows"] == [], "product boundary")
                local_product_boundaries.add((rv, tv, bv, cv, finite["status"]))
                totals["product_boundaries"] += 1
                continue
            core.require(finite["status"] == "CHECKED" and missing != 0, "checked route")
            totals["checked"] += 1

            missing_roots = field_roots(
                [1, 0, 2 * missing - source_sum, 0, missing * missing],
                "missing quartic",
            )
            antipodal_roots = field_roots(
                paired_coefficients(a_values, b_values, 1, -1),
                "antipodal q quartic",
            )
            core.require(
                finite["missing_z_roots"] == missing_roots
                and finite["antipodal_q_roots"] == antipodal_roots,
                "nested sign-free root replay",
            )
            totals["missing_z_roots"] += len(missing_roots)
            reported_z = {item["z"]: item for item in finite["z_rows"]}
            core.require(set(reported_z) == set(missing_roots), "complete z ledger")
            for z_value in missing_roots:
                z_row = reported_z[z_value]
                y_value = z_value * z_value % PRIME
                d_value = pow(z_value, -1, PRIME)
                f_value = missing * z_value % PRIME
                core.require(
                    z_value != 0
                    and z_row["y"] == y_value
                    and z_row["d"] == d_value
                    and z_row["f"] == f_value,
                    "z/d lift",
                )
                second_roots = field_roots(
                    paired_left_coefficients(
                        a_values, b_values,
                        sigma_c * cv * f_value % PRIME,
                    ),
                    "second q quartic",
                )
                common_q = intersect(antipodal_roots, second_roots)
                core.require(
                    common_q is not None
                    and z_row["second_q_roots"] == second_roots
                    and z_row["common_q_roots"] == common_q,
                    "q intersection",
                )
                if common_q:
                    local_z_candidates.add(
                        (rv, tv, bv, cv, z_value, y_value, len(common_q))
                    )
                reported_q = {item["q"]: item for item in z_row["q_rows"]}
                core.require(set(reported_q) == set(common_q), "complete q ledger")
                for q_value in common_q:
                    e_value = q_value * z_value % PRIME
                    q_row = reported_q[q_value]
                    core.require(
                        q_row["e"] == e_value
                        and q_row["antipodal_pair_cut"] == 0
                        and q_row["second_pair_cut"] == 0
                        and core.paired(
                            a_values, b_values, q_value, -q_value % PRIME
                        ) == 0
                        and core.paired(
                            a_values, b_values, q_value,
                            sigma_c * cv * f_value % PRIME,
                        ) == 0,
                        "common q-root replay",
                    )
                    local_q_candidates.add(
                        (
                            rv, tv, bv, cv, q_value, z_value, y_value,
                            d_value, e_value, f_value,
                        )
                    )
                    lanes = {item["sigma"][1]: item for item in q_row["lanes"]}
                    core.require(
                        set(lanes) == {-1, 1}
                        and all(item["sigma"][0] == sigma_c for item in lanes.values()),
                        "target lane cover",
                    )
                    for sigma_o, lane in lanes.items():
                        final_pair = core.paired(
                            a_values, b_values,
                            sigma_o * e_value * f_value % PRIME,
                            bv * f_value % PRIME,
                        )
                        core.require(
                            final_pair != 0
                            and lane["final_pair_cut"] == final_pair
                            and lane["status"] == "THIRD_PAIR_NONZERO",
                            "third-pair exclusion",
                        )
                        totals["lane_checks"] += 1
                        totals["third_pair_nonzero"] += 1
                totals["d_lifts"] += 1
                totals["q_intersections"] += 1
                totals["common_q_roots"] += len(common_q)

        core.require(local_missing_free == paid_base_points, "regularized exactness")
        reported_z_candidates = {
            tuple(
                item[name]
                for name in ("r", "t", "b", "c", "z", "y", "q_count")
            )
            for item in row["z_candidates"]
        }
        core.require(reported_z_candidates == local_z_candidates, "z-candidate ledger")
        reported_q_candidates = {
            tuple(
                item[name]
                for name in ("r", "t", "b", "c", "q", "z", "y", "d", "e", "f")
            )
            for item in row["q_candidates"]
        }
        core.require(
            reported_q_candidates == local_q_candidates,
            "q-candidate ledger",
        )
        reported_boundaries = {
            (item["r"], item["t"], item["b"], item["c"], item["status"])
            for item in row["target_boundary_rows"]
        }
        core.require(
            reported_boundaries == local_product_boundaries,
            "target-boundary ledger",
        )
        totals["target_boundaries"] += len(reported_boundaries)
        for field in (
            "target_norm_root_count",
            "candidate_root_count",
            "source_point_count",
            "route_point_count",
            "z_candidate_count",
            "q_candidate_count",
            "final_pair_solution_count",
        ):
            totals[field] += row[field]

    core.require(seen == expected and counts["records"] == 48, "complete cover")
    return {
        "schema": (
            "rate-half-kb-positive-433-1b-cell9-xi3-pairing5-direct-audit-v1"
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
        if len({json.dumps(row[field], sort_keys=True) for row in chart_rows}) != 1:
            raise RuntimeError(f"chart audit disagreement: {field}")
    summed = (
        "rows",
        "profile_visits",
        "target_norm_root_count",
        "candidate_root_count",
        "source_point_count",
        "route_point_count",
        "z_candidate_count",
        "q_candidate_count",
        "final_pair_solution_count",
        "r_boundaries",
        "t_boundaries",
        "no_lifts",
        "missing_impossible",
        "missing_free",
        "product_boundaries",
        "checked",
        "missing_z_roots",
        "d_lifts",
        "q_intersections",
        "common_q_roots",
        "lane_checks",
        "third_pair_nonzero",
        "chart_b_paid",
        "chart_c_paid",
        "regularized_paid",
        "target_boundaries",
    )
    output = {field: chart_rows[0][field] for field in shared_fields}
    output.update({field: sum(row[field] for row in chart_rows) for field in summed})
    output["chart_rows"] = chart_rows
    if output["rows"] != 48:
        raise RuntimeError("aggregate row cover")
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, sort_keys=True))
