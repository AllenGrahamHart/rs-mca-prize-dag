#!/usr/bin/env python3
"""Replay the cell-9 positive-DE pairing-9 certificate."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMARY = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_chart_result"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_"
    "frobenius_roots_result.json"
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
    "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_direct_audit_result.json"
)
REMOTE_PRIMARY = "/root/primary"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_TOWER = "/root/tower.json"
REMOTE_KERNEL = "/root/kernel.json"
REMOTE_BASE = "/root/base.json"
PRIME = 2130706433

app = modal.App(
    "rs-mca-positive-433-1b-cell9-positive-de-pairing9-direct-audit"
)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_dir(PRIMARY, REMOTE_PRIMARY)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(TOWER, REMOTE_TOWER)
    .add_local_file(KERNEL, REMOTE_KERNEL)
    .add_local_file(BASE, REMOTE_BASE)
    .add_local_file(CORE, "/root/audit_core.py")
    .add_local_file(SHARDED, "/root/sharded_result.py")
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=6)
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
            "Exact six-chart execution of the pinned nested-quadratic "
            "positive-DE pairing-9 compiler for cell-9 xi=0."
        ),
        "source_tower_sha256": digest(REMOTE_TOWER),
        "source_kernel_sha256": digest(REMOTE_KERNEL),
        "source_base_sha256": digest(REMOTE_BASE),
    }
    for key, value in expected_metadata.items():
        core.require(manifest_payload["metadata"].get(key) == value,
                     f"manifest metadata {key}")

    profiles = {}
    for row in iter_records(manifest):
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                profile = value[side]
                profiles.setdefault(profile["sha256"], profile)
    roots = json.loads(Path(REMOTE_ROOTS).read_text())
    core.require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell9-positive-de-pairing9-frobenius-roots-v1"
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
        core.require(hashlib.sha256(text.encode()).hexdigest() == key,
                     "profile digest")
        coefficients = core.parse_flint(text)
        core.require(
            (max(coefficients, default=-1), len(coefficients))
            == (profile["degree"], profile["terms"]), "profile shape")
        checked = root_rows[key]
        core.require(
            (checked["degree"], checked["terms"])
            == (profile["degree"], profile["terms"])
            and checked["frobenius_root_degree"] == len(checked["roots"])
            and checked["roots"] == sorted(set(checked["roots"]))
            and all(core.evaluate_sparse(coefficients, value) == 0
                    for value in checked["roots"]), "external root row")
        root_cache[key] = checked["roots"]

    tower = {}
    for row in json.loads(Path(REMOTE_TOWER).read_text())["rows"]:
        key = (tuple(row["epsilon"]), row["b_row_index"], row["c_row_index"])
        core.require(
            key not in tower and row["status"] == "COMPLETE" and row["exact"]
            and row["b_cover_complete"] and row["c_cover_complete"]
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
            item for item in row["rows"]
            if item["pairing_index"] == 9 and item["xi_index"] == 0
        ]
        core.require(
            row["status"] == "COMPLETE" and row["section_is_zero"]
            and row["point"]["guard_nonzero"] and not row["nonunit_systems"]
            and len(relevant) == 1
            and all(item["unit"] and item["dimension"] == -1
                    and item["basis_size"] == 1 for item in relevant),
            "regularized base custody",
        )
        regularized.add((tuple(row["epsilon"]), tuple(row["sigma"]), point))
    core.require(len(regularized) == 32, "regularized base cover")

    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    selected_b, selected_c = chart_case
    expected = {
        (epsilon, sigma, xi, selected_b, selected_c)
        for epsilon in signs for sigma in signs for xi in (0,)
    }
    matching = ((0, 4), (1, 2), (3, 5))
    seen = set()
    totals = {
        key: 0 for key in (
            "target_root_count", "candidate_root_count", "source_point_count",
            "route_point_count", "uf_candidate_count", "colored_solution_count",
            "r_boundaries", "t_boundaries", "no_lifts", "missing_impossible",
            "missing_free", "product_boundaries", "checked",
            "missing_relation_nonzero", "uf_checked", "f_boundaries",
            "d_boundaries", "colored_nonzero", "chart_b_paid", "chart_c_paid",
            "regularized_paid", "target_boundaries",
        )
    }
    profile_visits = 0
    for row in iter_records(manifest):
        if (row["b_row_index"], row["c_row_index"]) != chart_case:
            continue
        key = (
            tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"],
            row["b_row_index"], row["c_row_index"],
        )
        core.require(key in expected and key not in seen, "Cartesian row cover")
        seen.add(key)
        epsilon, sigma, xi, b_index, c_index = key
        sigma_c, sigma_o = sigma
        chart = tower[(epsilon, b_index, c_index)]
        core.require(
            row["status"] == "COMPLETE" and row["excluded"]
            and tuple(map(tuple, row["matching"])) == matching
            and row["pairing_index"] == 9
            and (row["p_u_degree"], row["p_f_degree"],
                 row["uf_eliminant_degree"], row["remainder_degree"])
            == (2, 2, 8, 1)
            and not row["witnesses"] and not row["unresolved"]
            and not row["colored_solutions"], "complete result row")

        target_roots = root_cache[row["target_norm"]["numerator"]["sha256"]]
        core.require(target_roots == row["target_roots"], "target-root replay")
        candidate_roots = set(target_roots)
        for item in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                candidate_roots.update(root_cache[item[side]["sha256"]])
                profile_visits += 1
        core.require(sorted(candidate_roots) == row["candidate_roots"],
                     "candidate-root union")
        covered = {
            item["r"] for field in ("boundary_rows", "no_lift_rows", "finite_rows")
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
            "row/chart relation join")
        for item in row["boundary_rows"]:
            if item["stage"] == "R_GUARD":
                core.require(item["r"] in {0, 1, PRIME - 1, core.IOTA,
                                            PRIME - core.IOTA}, "r boundary")
                totals["r_boundaries"] += 1
            elif item["stage"] == "T_GUARD":
                rv, tv = item["r"], item["t"]
                core.require(
                    core.value(base_relation, item) == 0
                    and tv * (tv * tv - 1) * (tv * tv + 1)
                    * (tv * tv - rv * rv) * (tv * tv + rv * rv) % PRIME == 0,
                    "t boundary")
                totals["t_boundaries"] += 1
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
            discriminant = (linear * linear - 4 * leading * constant) % PRIME
            core.require(leading and pow(discriminant, (PRIME - 1) // 2, PRIME)
                         == PRIME - 1, "no-b nonsquare")
            totals["no_lifts"] += 1

        paid_base_points = set()
        for item in row["paid_rows"]:
            if item["stage"] == "CHART_B_LEADING":
                core.require(
                    item["reason"] == "FREE_B"
                    and core.value(base_relation, item) == 0
                    and core.value(sp.sympify(chart["b_leading"]["expression"]),
                                   item) == 0, "b-leading payment")
                totals["chart_b_paid"] += 1
            elif item["stage"] == "CHART_C_LEADING":
                core.require(
                    item["reason"] == "FREE_C"
                    and core.value(base_relation, item) == 0
                    and core.value(b_relation, item) == 0
                    and core.value(sp.sympify(chart["c_leading"]["expression"]),
                                   item) == 0, "c-leading payment")
                totals["chart_c_paid"] += 1
            elif item["stage"] == "REGULARIZED_BASE":
                point = tuple(item[name] for name in ("r", "t", "b", "c"))
                core.require(
                    item["reason"] == "MISSING_FREE"
                    and (epsilon, sigma, point) in regularized
                    and core.value(base_relation, item) == 0
                    and core.value(b_relation, item) == 0
                    and core.value(c_relation, item) == 0,
                    "regularized-base payment")
                paid_base_points.add(point)
                totals["regularized_paid"] += 1
            else:
                raise RuntimeError(f"unexpected payment {item}")

        kernel = kernels[epsilon]
        local_candidates = set()
        local_boundaries = []
        local_missing_free = set()
        core.require(row["source_point_count"] == row["route_point_count"]
                     == len(row["finite_rows"]), "source route count")
        for finite in row["finite_rows"]:
            core.require(
                core.value(base_relation, finite)
                == core.value(b_relation, finite)
                == core.value(c_relation, finite) == 0,
                "finite source relations")
            rv, tv, bv, cv = (finite[name] for name in ("r", "t", "b", "c"))
            guards = (
                bv, cv, rv, tv, bv - 1, bv + 1, cv - 1, cv + 1,
                bv - cv, bv + cv, rv * rv - 1, rv * rv + 1,
                tv * tv - 1, tv * tv + 1,
                tv * tv - rv * rv, tv * tv + rv * rv,
            )
            core.require(all(value % PRIME for value in guards),
                         "finite route guards")
            point = {core.r: rv, core.t: tv, core.b: bv, core.c: cv}
            values = [int(expression.subs(point)) % PRIME for expression in kernel]
            a_values, b_values = values[:3], values[3:6]
            beta_0, beta_1 = values[6:]
            label = -tv * tv % PRIME
            a_missing = sum(value * pow(label, index, PRIME)
                            for index, value in enumerate(a_values)) % PRIME
            b_missing = sum(value * pow(label, index, PRIME)
                            for index, value in enumerate(b_values)) % PRIME
            if finite["status"] == "MISSING_IMPOSSIBLE":
                core.require(a_missing == 0 and b_missing != 0,
                             "missing-impossible terminal")
                totals["missing_impossible"] += 1
                continue
            if finite["status"] == "MISSING_FREE":
                point_key = (rv, tv, bv, cv)
                core.require(a_missing == b_missing == 0
                             and point_key in paid_base_points,
                             "missing-free terminal")
                local_missing_free.add(point_key)
                totals["missing_free"] += 1
                continue
            core.require(a_missing != 0, "missing denominator")
            missing = b_missing * pow(a_missing, -1, PRIME) % PRIME
            de = missing if xi == 0 else -missing % PRIME
            second_de = -de % PRIME if xi == 0 else de
            source_sum = (
                label * pow((beta_0 + beta_1 * label) % PRIME, 2, PRIME)
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            core.require(
                (finite["missing"], finite["de"], finite["source_sum"])
                == (missing, de, source_sum), "missing-record replay")
            if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                core.require(de == 0 and finite["uf_rows"] == [],
                             "product boundary")
                local_boundaries.append(finite)
                totals["product_boundaries"] += 1
                continue
            core.require(finite["status"] == "CHECKED" and de != 0,
                         "checked source terminal")
            totals["checked"] += 1
            u_roots = core.quadratic_roots(
                core.paired_coefficients(a_values, b_values, second_de, 1),
                "u paired cut")
            f_roots = core.quadratic_roots(
                core.paired_coefficients(a_values, b_values, de, bv),
                "f paired cut")
            core.require(u_roots == finite["u_roots"]
                         and f_roots == finite["f_roots"],
                         "paired quadratic roots")
            uf_rows = {(item["u"], item["f"]): item for item in finite["uf_rows"]}
            core.require(set(uf_rows) == {(u, f) for u in u_roots for f in f_roots},
                         "Cartesian uf replay")
            eta = 1 if xi == 0 else -1
            for (uv, fv), uf_row in uf_rows.items():
                relation = (
                    pow((uv * uv + eta * de * fv * fv) % PRIME, 2, PRIME)
                    - source_sum * fv * fv * uv * uv
                ) % PRIME
                core.require(relation == uf_row["relation"],
                             "missing relation replay")
                if relation:
                    core.require(uf_row["status"] == "MISSING_RELATION_NONZERO",
                                 "nonzero relation terminal")
                    totals["missing_relation_nonzero"] += 1
                    continue
                totals["uf_checked"] += 1
                local_candidates.add((rv, tv, bv, cv, uv, fv))
                if fv == 0:
                    core.require(
                        uf_row["status"] == "TARGET_BOUNDARY"
                        and uf_row["failed_guards"] == ["nonzero_5"],
                        "zero-f boundary")
                    local_boundaries.append({**finite, **uf_row})
                    totals["f_boundaries"] += 1
                    continue
                dv = uv * pow(fv, -1, PRIME) % PRIME
                if dv == 0:
                    core.require(
                        uf_row["status"] == "TARGET_BOUNDARY"
                        and uf_row["failed_guards"] == ["nonzero_3"],
                        "zero-d boundary")
                    local_boundaries.append({**finite, **uf_row})
                    totals["d_boundaries"] += 1
                    continue
                ev = de * pow(dv, -1, PRIME) % PRIME
                vv = ev * fv % PRIME
                colored = core.paired(
                    a_values, b_values,
                    sigma_o * vv % PRIME,
                    sigma_c * cv * fv % PRIME)
                core.require(
                    (uf_row["d"], uf_row["e"], uf_row["v"],
                     uf_row["colored_cut"])
                    == (dv, ev, vv, colored)
                    and colored != 0
                    and uf_row["status"] == "COLORED_PAIR_NONZERO",
                    "colored-pair terminal")
                totals["colored_nonzero"] += 1
        core.require(local_missing_free == paid_base_points,
                     "regularized payment exactness")
        reported_candidates = {
            tuple(item[name] for name in ("r", "t", "b", "c", "u", "f"))
            for item in row["uf_candidates"]
        }
        core.require(reported_candidates == local_candidates,
                     "uf-candidate ledger")
        core.require(
            {core.boundary_key(item) for item in row["target_boundary_rows"]}
            == {core.boundary_key(item) for item in local_boundaries},
            "target-boundary ledger")
        for field in (
            "target_root_count", "candidate_root_count", "source_point_count",
            "route_point_count", "uf_candidate_count", "colored_solution_count",
        ):
            totals[field] += row[field]
        totals["target_boundaries"] += len(local_boundaries)
    core.require(seen == expected and counts["records"] == 96,
                 "complete Cartesian cover")
    return {
        "schema": (
            "rate-half-kb-positive-433-1b-cell9-positive-de-pairing9-direct-audit-v1"
        ),
        "field": PRIME,
        "source_manifest_sha256": digest(manifest),
        "source_roots_sha256": digest(REMOTE_ROOTS),
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
        for b_index in (2, 3) for c_index in (4, 5, 6)
    )
    chart_rows = list(audit.map(charts, order_outputs=True))
    if [tuple(row["chart"]) for row in chart_rows] != list(charts):
        raise RuntimeError("chart audit cover")
    shared_fields = (
        "schema", "field", "source_manifest_sha256", "source_roots_sha256",
        "source_tower_sha256", "source_kernel_sha256", "source_base_sha256",
        "sharded_counts", "profiles", "status",
    )
    for field in shared_fields:
        if len({json.dumps(row[field], sort_keys=True) for row in chart_rows}) != 1:
            raise RuntimeError(f"chart audit disagreement: {field}")
    summed = (
        "rows", "profile_visits", "target_root_count", "candidate_root_count",
        "source_point_count", "route_point_count", "uf_candidate_count",
        "colored_solution_count", "r_boundaries", "t_boundaries", "no_lifts",
        "missing_impossible", "missing_free", "product_boundaries", "checked",
        "missing_relation_nonzero", "uf_checked", "f_boundaries",
        "d_boundaries", "colored_nonzero", "chart_b_paid", "chart_c_paid",
        "regularized_paid", "target_boundaries",
    )
    output = {field: chart_rows[0][field] for field in shared_fields}
    output.update({field: sum(row[field] for row in chart_rows) for field in summed})
    output["chart_rows"] = chart_rows
    if output["rows"] != 96:
        raise RuntimeError("aggregate row cover")
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, sort_keys=True))
