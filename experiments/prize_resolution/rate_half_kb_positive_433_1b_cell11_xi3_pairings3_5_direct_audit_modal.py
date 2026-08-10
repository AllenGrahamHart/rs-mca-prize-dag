#!/usr/bin/env python3
"""Independently replay the cell-11 xi=3 pairings-3/4/5 packets."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARIES = {
    str(pairing): DIRECTORY / (
        f"rate_half_kb_positive_433_1b_cell11_xi3_pairing{pairing}_"
        "template_adapter_result.json"
    )
    for pairing in (3, 4, 5)
}
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_"
    "independent_roots_result.json"
)
TEMPLATES = {
    "3": DIRECTORY / (
        "rate_half_kb_positive_433_1b_cell4_xi3_pairing3_"
        "reciprocal_square_modal.py"
    ),
    "4": DIRECTORY / (
        "rate_half_kb_positive_433_1b_cell4_xi3_pairing4_"
        "nested_signfree_modal.py"
    ),
    "5": DIRECTORY / (
        "rate_half_kb_positive_433_1b_cell4_xi3_pairing5_"
        "nested_signfree_modal.py"
    ),
}
TOWER = DIRECTORY / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
CORE = DIRECTORY / "rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit.py"
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_"
    "direct_audit_result.json"
)
REMOTE_PRIMARY = {key: f"/root/primary-{key}.json" for key in PRIMARIES}
REMOTE_TEMPLATE = {key: f"/root/template-{key}.py" for key in TEMPLATES}
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell11-xi3-pairings3-5-direct-audit")
image = modal.Image.debian_slim(python_version="3.12").pip_install(
    "sympy==1.14.0", "python-flint==0.8.0"
)
for key, path in PRIMARIES.items():
    image = image.add_local_file(path, REMOTE_PRIMARY[key])
for key, path in TEMPLATES.items():
    image = image.add_local_file(path, REMOTE_TEMPLATE[key])
image = (
    image.add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(CORE, "/root/audit_core.py")
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300)
def audit():
    import sys

    sys.path.insert(0, "/root")
    from flint import fmpz_mod_poly_ctx
    import sympy as sp

    import audit_core as core

    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    payloads = {key: json.loads(Path(path).read_text())
                for key, path in REMOTE_PRIMARY.items()}
    for key, payload in payloads.items():
        core.require(
            payload["schema"]
            == f"rate-half-kb-positive-433-1b-cell11-xi3-pairing{key}-adapter-v1"
            and payload["field"] == PRIME
            and payload["source_template_sha256"]
            == digest(REMOTE_TEMPLATE[key])
            and payload["source_tower_sha256"] == digest(REMOTE_TOWER)
            and payload["source_kernel_sha256"] == digest(REMOTE_KERNEL),
            f"pairing-{key} primary custody",
        )

    profiles = {}
    for payload in payloads.values():
        for row in payload["rows"]:
            for item in [*row["inverse_guards"], row["target_norm"]]:
                for side in ("numerator", "denominator"):
                    profile = item[side]
                    profiles.setdefault(profile["sha256"], profile)
    roots = json.loads(Path(REMOTE_ROOTS).read_text())
    core.require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings3-5-independent-roots-v1"
        and roots["field"] == PRIME
        and roots["source_primary_sha256"]
        == {key: digest(path) for key, path in REMOTE_PRIMARY.items()},
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
            and row["exact"] and not row["b_boundary_unit"]
            and not row["c_boundary_unit"] and row["b_boundary_dimension"] == 0
            and row["c_boundary_dimension"] == 0
            and row["b_boundary_basis_size"] == 15
            and row["c_boundary_basis_size"] == 21,
            "priced-boundary tower custody",
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

    context = fmpz_mod_poly_ctx(PRIME)

    def trim(values):
        output = [int(value) % PRIME for value in values]
        while output and output[-1] == 0:
            output.pop()
        return output

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
                output[i + j] = (output[i + j] + left_value*right_value) % PRIME
        return trim(output)

    def paired_coefficients(a_values, b_values, left_scale, right_scale):
        p_values = [[b_value, -left_scale*a_value]
                    for a_value, b_value in zip(a_values, b_values)]
        q_values = [
            [b_values[0], -right_scale*a_values[0]],
            [-b_values[1], right_scale*a_values[1]],
            [b_values[2], -right_scale*a_values[2]],
        ]
        first = poly_sub(poly_mul(p_values[2], q_values[0]),
                         poly_mul(p_values[0], q_values[2]))
        second = poly_sub(poly_mul(p_values[2], q_values[1]),
                          poly_mul(p_values[1], q_values[2]))
        third = poly_sub(poly_mul(p_values[1], q_values[0]),
                         poly_mul(p_values[0], q_values[1]))
        return poly_sub(poly_mul(first, first), poly_mul(second, third))

    def paired_left_coefficients(a_values, b_values, right):
        p_values = [[b_value, -a_value]
                    for a_value, b_value in zip(a_values, b_values)]
        q_values = [
            [b_values[0] - right*a_values[0]],
            [-b_values[1] + right*a_values[1]],
            [b_values[2] - right*a_values[2]],
        ]
        first = poly_sub(poly_mul(p_values[2], q_values[0]),
                         poly_mul(p_values[0], q_values[2]))
        second = poly_sub(poly_mul(p_values[2], q_values[1]),
                          poly_mul(p_values[1], q_values[2]))
        third = poly_sub(poly_mul(p_values[1], q_values[0]),
                         poly_mul(p_values[0], q_values[1]))
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
            core.require(int(factor.degree()) == 1 and int(multiplicity) == 1,
                         f"{label} squarefree linear root part")
            output.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        output = sorted(output)
        core.require(len(output) == int(root_part.degree())
                     and all(polynomial(value) == 0 for value in output),
                     f"{label} root census")
        return output

    def intersect(left, right):
        if left is None:
            return right
        if right is None:
            return left
        return sorted(set(left) & set(right))

    fields = (
        "rows", "profile_visits", "target_norm_root_count",
        "candidate_root_count", "source_point_count", "route_point_count",
        "z_candidate_count", "q_candidate_count",
        "final_pair_solution_count", "r_boundaries", "t_boundaries",
        "no_lifts", "missing_impossible", "product_boundaries", "checked",
        "common_z_roots", "z_roots", "q_intersections", "common_q_roots",
        "q_lifts", "final_color_nonzero", "target_boundaries",
        "leading_boundaries",
    )
    totals = {field: 0 for field in fields}
    by_pairing = {str(pairing): {field: 0 for field in fields}
                  for pairing in (3, 4, 5)}

    def bump(pairing, field, amount=1):
        totals[field] += amount
        by_pairing[str(pairing)][field] += amount

    seen = set()
    for pairing in (3, 4, 5):
        for row in payloads[str(pairing)]["rows"]:
            epsilon = tuple(row["epsilon"])
            sigma_c = row.get("sigma_c", 0)
            key = (pairing, epsilon, sigma_c)
            core.require(key not in seen and pairing in (3, 4, 5)
                         and (sigma_c in (-1, 1) if pairing in (3, 5)
                              else sigma_c == 0), "Cartesian row cover")
            seen.add(key)
            core.require(
                row["status"] == "COMPLETE" and row["target_excluded"]
                and row["xi_index"] == 3 and row["pairing_index"] == pairing
                and row["witness_count"] == 0 and not row["witnesses"]
                and not row["unresolved"]
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
                        and tv*(tv*tv - 1)*(tv*tv + 1)
                        *(tv*tv - rv*rv)*(tv*tv + rv*rv) % PRIME == 0,
                        "t boundary",
                    )
                    bump(pairing, "t_boundaries")
                elif item["stage"] in (
                    "CELL11_B_LEADING", "CELL11_C_LEADING"
                ):
                    leading = chart[
                        "b_leading" if item["stage"] == "CELL11_B_LEADING"
                        else "c_leading"
                    ]["expression"]
                    core.require(core.value(sp.sympify(leading), item) == 0,
                                 "cell-11 leading boundary")
                    bump(pairing, "leading_boundaries")
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
            local_z_candidates = set()
            local_q_candidates = set()
            local_boundaries = set()
            core.require(row["source_point_count"] == row["route_point_count"]
                         == len(row["finite_rows"]), "source route count")
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
                    label*pow((beta_0 + beta_1*label) % PRIME, 2, PRIME)
                    * pow(a_missing, -2, PRIME)
                ) % PRIME
                core.require((finite["missing"], finite["source_sum"])
                             == (missing, source_sum), "missing-record replay")
                if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                    core.require(missing == 0 and finite["z_rows"] == [],
                                 "product boundary")
                    local_boundaries.add((rv, tv, bv, cv, finite["status"]))
                    bump(pairing, "product_boundaries")
                    continue
                core.require(finite["status"] == "CHECKED" and missing != 0,
                             "checked route")
                bump(pairing, "checked")
                missing_roots = field_roots(
                    [1, 0, 2*missing - source_sum, 0, missing*missing],
                    "missing quartic",
                )
                antipodal_roots = field_roots(
                    paired_coefficients(a_values, b_values, 1, -1),
                    "antipodal q quartic",
                )
                if pairing == 3:
                    colored_roots = field_roots(
                        paired_coefficients(
                            a_values, b_values, bv*missing % PRIME,
                            sigma_c*cv*missing % PRIME,
                        ), "colored quartic",
                    )
                    common_z = intersect(missing_roots, colored_roots)
                    core.require(
                        finite["missing_z_roots"] == missing_roots
                        and finite["colored_z_roots"] == colored_roots
                        and finite["common_z_roots"] == common_z
                        and finite["antipodal_q_roots"] == antipodal_roots,
                        "pairing-3 root replay",
                    )
                    bump(pairing, "common_z_roots", len(common_z))
                    reported_z = {item["z"]: item for item in finite["z_rows"]}
                    core.require(set(reported_z) == set(common_z),
                                 "complete pairing-3 z ledger")
                    for z_value in common_z:
                        z_row = reported_z[z_value]
                        y_value = z_value*z_value % PRIME
                        d_value = pow(z_value, -1, PRIME)
                        f_value = missing*z_value % PRIME
                        core.require(z_row["y"] == y_value
                                     and z_row["d_roots"] == [d_value]
                                     and len(z_row["d_rows"]) == 1,
                                     "pairing-3 z/d lift")
                        local_z_candidates.add(
                            (rv, tv, bv, cv, sigma_c, z_value, y_value)
                        )
                        d_row = z_row["d_rows"][0]
                        core.require((d_row["d"], d_row["f"])
                                     == (d_value, f_value), "pairing-3 d/f")
                        for lane in d_row["lanes"]:
                            sigma_o = lane["sigma"][1]
                            outside_roots = field_roots(
                                paired_coefficients(
                                    a_values, b_values, 1,
                                    sigma_o*missing*y_value % PRIME,
                                ), "outside q quartic",
                            )
                            common_q = intersect(antipodal_roots, outside_roots)
                            core.require(lane["outside_q_roots"] == outside_roots
                                         and lane["common_q_roots"] == common_q
                                         and common_q == []
                                         and lane["q_rows"] == [],
                                         "pairing-3 empty q intersection")
                            bump(pairing, "q_intersections")
                            bump(pairing, "common_q_roots", len(common_q))
                else:
                    core.require(finite["missing_z_roots"] == missing_roots
                                 and finite["antipodal_q_roots"]
                                 == antipodal_roots,
                                 "nested sign-free root replay")
                    bump(pairing, "z_roots", len(missing_roots))
                    reported_z = {item["z"]: item for item in finite["z_rows"]}
                    core.require(set(reported_z) == set(missing_roots),
                                 "complete nested z ledger")
                    for z_value in missing_roots:
                        z_row = reported_z[z_value]
                        y_value = z_value*z_value % PRIME
                        d_value = pow(z_value, -1, PRIME)
                        f_value = missing*z_value % PRIME
                        core.require(z_row["y"] == y_value
                                     and z_row["d"] == d_value
                                     and z_row["f"] == f_value,
                                     "nested z/d/f lift")
                        second_right = (
                            bv*f_value if pairing == 4
                            else sigma_c*cv*f_value
                        ) % PRIME
                        second_roots = field_roots(
                            paired_left_coefficients(
                                a_values, b_values, second_right
                            ), "second q quartic",
                        )
                        common_q = intersect(antipodal_roots, second_roots)
                        core.require(z_row["second_q_roots"] == second_roots
                                     and z_row["common_q_roots"] == common_q,
                                     "nested q intersection")
                        if common_q:
                            local_z_candidates.add(
                                (rv, tv, bv, cv, z_value, y_value, len(common_q))
                            )
                        reported_q = {item["q"]: item
                                      for item in z_row["q_rows"]}
                        core.require(set(reported_q) == set(common_q),
                                     "complete nested q ledger")
                        for q_value in common_q:
                            q_row = reported_q[q_value]
                            e_value = q_value*z_value % PRIME
                            core.require(q_row["e"] == e_value
                                         and q_row["antipodal_pair_cut"] == 0
                                         and q_row["second_pair_cut"] == 0
                                         and core.paired(
                                             a_values, b_values,
                                             q_value, -q_value % PRIME) == 0
                                         and core.paired(
                                             a_values, b_values,
                                             q_value, second_right) == 0,
                                         "nested common q replay")
                            local_q_candidates.add((
                                rv, tv, bv, cv, q_value, z_value, y_value,
                                d_value, e_value, f_value,
                            ))
                            lanes = {tuple(item["sigma"]): item
                                     for item in q_row["lanes"]}
                            expected_lanes = (
                                {(-1, -1), (-1, 1), (1, -1), (1, 1)}
                                if pairing == 4
                                else {(sigma_c, -1), (sigma_c, 1)}
                            )
                            core.require(set(lanes) == expected_lanes,
                                         "nested target lanes")
                            for lane_sigma, lane in lanes.items():
                                lane_c, lane_o = lane_sigma
                                final_left = lane_o*e_value*f_value % PRIME
                                final_right = (
                                    lane_c*cv*f_value if pairing == 4
                                    else bv*f_value
                                ) % PRIME
                                final = core.paired(
                                    a_values, b_values, final_left, final_right
                                )
                                core.require(final != 0
                                             and lane["final_pair_cut"] == final
                                             and lane["status"]
                                             == "THIRD_PAIR_NONZERO",
                                             "nested final colored cut")
                                bump(pairing, "final_color_nonzero")
                            bump(pairing, "q_lifts")
                        bump(pairing, "q_intersections")
                        bump(pairing, "common_q_roots", len(common_q))

            if pairing == 3:
                reported_z = {
                    tuple(item[name] for name in
                          ("r", "t", "b", "c", "sigma_c", "z", "y"))
                    for item in row["z_candidates"]
                }
                core.require(reported_z == local_z_candidates
                             and row["q_candidates"] == [],
                             "pairing-3 candidate ledgers")
            else:
                reported_z = {
                    tuple(item[name] for name in
                          ("r", "t", "b", "c", "z", "y", "q_count"))
                    for item in row["z_candidates"]
                }
                reported_q = {
                    tuple(item[name] for name in
                          ("r", "t", "b", "c", "q", "z", "y",
                           "d", "e", "f"))
                    for item in row["q_candidates"]
                }
                core.require(reported_z == local_z_candidates
                             and reported_q == local_q_candidates,
                             "nested candidate ledgers")
            reported_boundaries = {
                (item["r"], item["t"], item["b"], item["c"], item["status"])
                for item in row["target_boundary_rows"]
            }
            core.require(reported_boundaries == local_boundaries,
                         "target-boundary ledger")
            for field in (
                "target_norm_root_count", "candidate_root_count",
                "source_point_count", "route_point_count", "z_candidate_count",
                "q_candidate_count", "final_pair_solution_count",
            ):
                bump(pairing, field, row[field])
            bump(pairing, "target_boundaries", len(local_boundaries))

    expected_cover = {
        (pairing, epsilon, sigma_c)
        for pairing in (3, 5)
        for epsilon in ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for sigma_c in (-1, 1)
    } | {
        (4, epsilon, 0)
        for epsilon in ((-1, -1), (-1, 1), (1, -1), (1, 1))
    }
    core.require(seen == expected_cover, "complete family cover")
    return {
        "schema": (
            "rate-half-kb-positive-433-1b-cell11-xi3-pairings3-5-"
            "direct-audit-v1"
        ),
        "field": PRIME,
        "source_primary_sha256": {
            key: digest(path) for key, path in REMOTE_PRIMARY.items()
        },
        "source_roots_sha256": digest(REMOTE_ROOTS),
        "source_template_sha256": {
            key: digest(path) for key, path in REMOTE_TEMPLATE.items()
        },
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
