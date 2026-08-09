#!/usr/bin/env python3
"""Direct replay for the cell-5 positive-DE pairing-14 certificate."""

import hashlib
import json
from pathlib import Path

import sympy as sp


P = 2130706433
IOTA = 16711679
t, r, c, b = sp.symbols("t r c b")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value(expression, point):
    substitutions = {
        t: point.get("t", 0),
        r: point.get("r", 0),
        c: point.get("c", 0),
        b: point.get("b", 0),
    }
    return int(sp.sympify(expression).subs(substitutions)) % P


def parse_flint(text):
    if text == "0":
        return {}
    coefficients = {}
    for term in text.split(" + "):
        if "*x^" in term:
            coefficient, degree = term.split("*x^")
            coefficient, degree = int(coefficient), int(degree)
        elif term.startswith("x^"):
            coefficient, degree = 1, int(term[2:])
        elif term.endswith("*x"):
            coefficient, degree = int(term[:-2]), 1
        elif term == "x":
            coefficient, degree = 1, 1
        else:
            coefficient, degree = int(term), 0
        require(degree not in coefficients, "duplicate polynomial degree")
        coefficients[degree] = coefficient % P
    return {degree: item for degree, item in coefficients.items() if item}


def evaluate_sparse(coefficients, point):
    output = 0
    for degree in range(max(coefficients, default=-1), -1, -1):
        output = (output * point + coefficients.get(degree, 0)) % P
    return output


def paired(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value - left * a_value) % P
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0] - right * a_values[0]) % P
    q1 = (-b_values[1] + right * a_values[1]) % P
    q2 = (b_values[2] - right * a_values[2]) % P
    return (
        pow((p2 * q0 - p0 * q2) % P, 2, P)
        - ((p2 * q1 - p1 * q2) % P) * ((p1 * q0 - p0 * q1) % P)
    ) % P


def paired_coefficients(a_values, b_values, left, right_scale):
    p0, p1, p2 = (
        (b_value - left * a_value) % P
        for a_value, b_value in zip(a_values, b_values)
    )
    a0 = (p2 * b_values[0] - p0 * b_values[2]) % P
    a1 = right_scale * (-p2 * a_values[0] + p0 * a_values[2]) % P
    b0 = (-p2 * b_values[1] - p1 * b_values[2]) % P
    b1 = right_scale * (p2 * a_values[1] + p1 * a_values[2]) % P
    c0 = (p1 * b_values[0] + p0 * b_values[1]) % P
    c1 = right_scale * (-p1 * a_values[0] - p0 * a_values[1]) % P
    return [
        (a0 * a0 - b0 * c0) % P,
        (2 * a0 * a1 - b0 * c1 - b1 * c0) % P,
        (a1 * a1 - b1 * c1) % P,
    ]


def quadratic_roots(coefficients, label):
    coefficients = [item % P for item in coefficients]
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    degree = len(coefficients) - 1
    require(degree >= 0, f"{label} identically zero")
    if degree == 0:
        return []
    if degree == 1:
        return [-coefficients[0] * pow(coefficients[1], -1, P) % P]
    require(degree == 2, f"{label} degree")
    constant, linear, leading = coefficients
    discriminant = (linear * linear - 4 * leading * constant) % P
    inverse = pow(2 * leading, -1, P)
    return sorted({
        (-linear + root) * inverse % P
        for root in sp.sqrt_mod(discriminant, P, all_roots=True)
    })


def even_quartic_roots(coefficients, label):
    require(
        len(coefficients) == 5
        and coefficients[1] % P == coefficients[3] % P == 0
        and coefficients[4] % P != 0,
        f"{label} even quartic",
    )
    square_roots = quadratic_roots(
        [coefficients[0], coefficients[2], coefficients[4]],
        f"{label} in u^2",
    )
    return sorted({
        int(root)
        for square in square_roots
        for root in sp.sqrt_mod(square, P, all_roots=True)
    })


def boundary_key(item):
    return (
        item.get("r"), item.get("t"), item.get("b"), item.get("c"),
        item.get("u"), item.get("f"), item.get("status"),
        tuple(item.get("failed_guards", ())),
    )


def load_root_cache(root_result, primary_paths):
    payloads = {name: json.loads(path.read_text())
                for name, path in primary_paths.items()}
    profiles = {}
    for payload in payloads.values():
        for row in payload["rows"]:
            for item in [*row["inverse_guards"], row["target_norm"]]:
                for side in ("numerator", "denominator"):
                    profile = item[side]
                    profiles.setdefault(profile["sha256"], profile)
    roots = json.loads(root_result.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-positive-de-pairing14-frobenius-roots-v1"
        and roots["field"] == P
        and roots["method"]
        == "external FLINT gcd(P,x^p-x), factor squarefree root part"
        and roots["source_primary_sha256"]
        == digest(next(iter(primary_paths.values()))),
        "external root custody",
    )
    root_rows = {item["sha256"]: item for item in roots["rows"]}
    require(set(root_rows) == set(profiles), "external root profile cover")
    cache = {}
    for key, profile in profiles.items():
        text = profile["expression"]
        require(hashlib.sha256(text.encode()).hexdigest() == key,
                "profile digest")
        coefficients = parse_flint(text)
        require(
            (max(coefficients, default=-1), len(coefficients))
            == (profile["degree"], profile["terms"]),
            "profile shape",
        )
        audited = root_rows[key]
        require(
            (audited["degree"], audited["terms"])
            == (profile["degree"], profile["terms"])
            and audited["frobenius_root_degree"] == len(audited["roots"])
            and audited["roots"] == sorted(set(audited["roots"]))
            and all(evaluate_sparse(coefficients, root) == 0
                    for root in audited["roots"]),
            "external root row",
        )
        cache[key] = audited["roots"]
    return cache, len(profiles)


def audit_result(result, root_result, primary_paths, tower_path, kernel_path,
                 pairing, xi_values, matching):
    cache, combined_profiles = load_root_cache(root_result, primary_paths)
    tower = json.loads(tower_path.read_text())
    leading = {
        tuple(row["epsilon"]): sp.sympify(row["b_leading"]["expression"])
        for row in tower["rows"] if row["c_row_index"] == 6
    }
    kernels = {
        tuple(row["epsilon"]): tuple(
            sp.sympify(item["expression"]) for item in row["kernel"]
        )
        for row in json.loads(kernel_path.read_text())["rows"]
    }
    payload = json.loads(result.read_text())
    expected = {
        (epsilon, sigma, xi, pairing)
        for epsilon in ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for sigma in ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for xi in xi_values
    }
    seen = set()
    totals = {
        key: 0 for key in (
            "target_root_count", "candidate_root_count", "source_point_count",
            "route_point_count", "uf_candidate_count", "colored_solution_count",
            "leading_boundaries", "product_boundaries", "target_boundaries",
            "missing_impossible", "checked", "colored_nonzero",
        )
    }
    profile_visits = 0
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]),
               row["xi_index"], row["pairing_index"])
        require(key in expected and key not in seen, "Cartesian row cover")
        seen.add(key)
        epsilon, sigma, xi, _ = key
        sigma_c, sigma_o = sigma
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and tuple(map(tuple, row["matching"])) == matching
            and (row["p_b_degree"], row["p_c_degree"]) == (2, 2)
            and row["common_f_resultant"]
            and not row["witnesses"] and not row["unresolved"],
            "complete result row",
        )
        target_num = row["target_norm"]["numerator"]
        target_den = row["target_norm"]["denominator"]
        target_roots = [root for root in cache[target_num["sha256"]]
                        if root not in set(cache[target_den["sha256"]])]
        require(target_roots == row["target_roots"], "target-root replay")
        candidate_roots = set()
        for item in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                candidate_roots.update(cache[item[side]["sha256"]])
                profile_visits += 1
        require(sorted(candidate_roots) == row["candidate_roots"],
                "candidate-root union")
        covered = {
            item["r"]
            for field in ("boundary_rows", "no_lift_rows", "finite_rows")
            for item in row[field]
        }
        require(covered == candidate_roots, "candidate terminal cover")

        base = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        for item in row["boundary_rows"]:
            if item["stage"] == "R_GUARD":
                require(item["r"] in {0, 1, P - 1, IOTA, P - IOTA},
                        "r boundary")
            elif item["stage"] == "T_GUARD":
                rv, tv = item["r"], item["t"]
                require(
                    value(base, item) == 0
                    and tv * (tv * tv - 1) * (tv * tv + 1)
                    * (tv * tv - rv * rv) * (tv * tv + rv * rv) % P == 0,
                    "t boundary",
                )
            elif item["stage"] == "CELL5_B_LEADING":
                require(value(leading[epsilon], item) == 0,
                        "cell-5 leading boundary")
                totals["leading_boundaries"] += 1
            else:
                raise RuntimeError(f"unexpected boundary {item['stage']}")
        b_polynomial = sp.Poly(b_relation, b)
        for item in row["no_lift_rows"]:
            require(item["stage"] == "NO_B_ROOT" and value(base, item) == 0,
                    "no-b lift row")
            leading_coefficient, linear, constant = (
                value(coefficient, item)
                for coefficient in b_polynomial.all_coeffs()
            )
            discriminant = (linear * linear
                            - 4 * leading_coefficient * constant) % P
            require(leading_coefficient and pow(discriminant, (P - 1) // 2, P)
                    == P - 1, "no-b nonsquare")

        kernel = kernels[epsilon]
        local_candidates = set()
        local_boundaries = []
        require(row["source_point_count"] == row["route_point_count"]
                == len(row["finite_rows"]), "source route count")
        for finite in row["finite_rows"]:
            require(value(base, finite) == value(b_relation, finite)
                    == value(c_relation, finite) == 0,
                    "finite source relations")
            rv, tv, bv, cv = (finite[name] for name in ("r", "t", "b", "c"))
            guards = (
                bv, cv, rv, tv, bv - 1, bv + 1, cv - 1, cv + 1,
                bv - cv, bv + cv, rv * rv - 1, rv * rv + 1,
                tv * tv - 1, tv * tv + 1,
                tv * tv - rv * rv, tv * tv + rv * rv,
            )
            require(all(item % P for item in guards), "finite route guards")
            point = {r: rv, t: tv, b: bv, c: cv}
            values = [int(item.subs(point)) % P for item in kernel]
            a_values, b_values = values[:3], values[3:6]
            beta_0, beta_1 = values[6:]
            label = -tv * tv % P
            a_missing = sum(item * pow(label, index, P)
                            for index, item in enumerate(a_values)) % P
            b_missing = sum(item * pow(label, index, P)
                            for index, item in enumerate(b_values)) % P
            if finite["status"] == "MISSING_IMPOSSIBLE":
                require(a_missing == 0 and b_missing != 0,
                        "missing-impossible terminal")
                totals["missing_impossible"] += 1
                continue
            require(a_missing != 0, "missing denominator")
            missing = b_missing * pow(a_missing, -1, P) % P
            de = missing if xi == 0 else -missing % P
            second_de = -de % P if xi == 0 else de
            source_sum = (
                label * pow((beta_0 + beta_1 * label) % P, 2, P)
                * pow(a_missing, -2, P)
            ) % P
            require((finite["missing"], finite["de"], finite["source_sum"])
                    == (missing, de, source_sum), "missing-record replay")
            if finite["status"] == "TARGET_PRODUCT_BOUNDARY":
                require(de == 0 and finite["uf_rows"] == [],
                        "product boundary")
                local_boundaries.append(finite)
                totals["product_boundaries"] += 1
                continue
            require(finite["status"] == "CHECKED" and de != 0,
                    "checked source terminal")
            totals["checked"] += 1
            if pairing == 11:
                b_left, c_left = de, second_de
            else:
                b_left, c_left = second_de, de
            b_roots = quadratic_roots(
                paired_coefficients(a_values, b_values, b_left, bv),
                "b paired f cut",
            )
            c_roots = quadratic_roots(
                paired_coefficients(a_values, b_values, c_left, sigma_c * cv),
                "c paired f cut",
            )
            require(b_roots == finite["b_pair_f_roots"]
                    and c_roots == finite["c_pair_f_roots"],
                    "paired f roots")
            common = sorted(set(b_roots) & set(c_roots))
            require(common == finite["common_f_roots"], "common-f roots")
            expected_pairs = set()
            eta = 1 if xi == 0 else -1
            for fv in common:
                if fv == 0:
                    expected_pairs.add((None, 0))
                    continue
                square = fv * fv % P
                quartic = [
                    de * de * square * square % P,
                    0,
                    square * (2 * eta * de - source_sum) % P,
                    0,
                    1,
                ]
                expected_pairs.update(
                    (uv, fv) for uv in even_quartic_roots(quartic, "missing cut")
                )
            require({(item["u"], item["f"]) for item in finite["uf_rows"]}
                    == expected_pairs, "complete quartic lift")
            for uf_row in finite["uf_rows"]:
                uv, fv = uf_row["u"], uf_row["f"]
                if fv == 0:
                    require(uv is None and uf_row["status"] == "TARGET_BOUNDARY"
                            and uf_row["failed_guards"] == ["nonzero_5"],
                            "f-zero boundary")
                    local_boundaries.append({**finite, **uf_row})
                    continue
                relation = (
                    pow((uv * uv + eta * de * fv * fv) % P, 2, P)
                    - source_sum * fv * fv * uv * uv
                ) % P
                require(relation == uf_row["relation"] == 0,
                        "missing quartic relation")
                local_candidates.add((rv, tv, bv, cv, uv, fv))
                ev = uv * pow(fv, -1, P) % P
                if ev == 0:
                    require(uf_row["status"] == "TARGET_BOUNDARY"
                            and uf_row["failed_guards"] == ["nonzero_4"],
                            "e-zero boundary")
                    local_boundaries.append({**finite, **uf_row})
                    continue
                dv = de * pow(ev, -1, P) % P
                vv = dv * fv % P
                colored = paired(a_values, b_values, vv, sigma_o * uv % P)
                require(
                    (uf_row["d"], uf_row["e"], uf_row["v"],
                     uf_row["colored_cut"])
                    == (dv, ev, vv, colored)
                    and colored != 0
                    and uf_row["status"] == "COLORED_PAIR_NONZERO",
                    "colored-pair terminal",
                )
                totals["colored_nonzero"] += 1
        reported_candidates = {
            tuple(item[name] for name in ("r", "t", "b", "c", "u", "f"))
            for item in row["uf_candidates"]
        }
        require(reported_candidates == local_candidates,
                "uf-candidate ledger")
        require({boundary_key(item) for item in row["target_boundary_rows"]}
                == {boundary_key(item) for item in local_boundaries},
                "target-boundary ledger")
        for field in (
            "target_root_count", "candidate_root_count", "source_point_count",
            "route_point_count", "uf_candidate_count", "colored_solution_count",
        ):
            totals[field] += row[field]
        totals["target_boundaries"] += len(local_boundaries)
    require(seen == expected, "complete Cartesian cover")
    return {
        "rows": len(seen),
        "combined_profiles": combined_profiles,
        "profile_visits": profile_visits,
        **totals,
    }
