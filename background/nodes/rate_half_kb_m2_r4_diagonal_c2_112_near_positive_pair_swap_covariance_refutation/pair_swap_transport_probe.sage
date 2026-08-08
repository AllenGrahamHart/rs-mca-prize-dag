#!/usr/bin/env sage
"""Probe the missing reciprocal-pair-swap transport exactly.

The loaded audit reconstructs all twelve near-positive source systems with a
generic 5 x 5 solve.  This probe then applies the centralizer map that sends
the moving reciprocal pair to {2,1/2}, including its action on W, and tests
residuals, targets, and radical localizers independently of orbit heuristics.
"""

load("/near_literal_assignment_transport_audit.sage")

import os


S_MAP = {
    "F00": "F04", "F01": "F06", "F02": "F05", "F03": "F07",
    "F04": "F00", "F05": "F02", "F06": "F01", "F07": "F03",
    "M00": "M01", "M01": "M00", "M02": "M03", "M03": "M02",
}
S_TARGET = {"A": "OB", "TA": "OI", "OB": "A", "OI": "TA"}

u = (2 * bK - 1) / (bK - 2)


def phi(value):
    value = K(value)
    return K((u * value + 1) / (value + u))


b_prime, c_prime, d_prime = phi(K(2)), phi(cK), phi(dK)
assert b_prime == (5 * bK - 4) / (4 * bK - 5)
assert phi(1 / bK) == K(1) / 2
assert phi(bK) == K(2)
assert phi(K(2)) == b_prime
assert phi(K(1) / 2) == 1 / b_prime
assert phi(1 / cK) == 1 / c_prime
assert phi(1 / dK) == 1 / d_prime


def parameter_pullback(value):
    return K(K(value).subs({bK: b_prime, cK: c_prime, dK: d_prime}))


def parameter_pullback_poly(poly):
    poly = KW(poly)
    return KW(sum(parameter_pullback(poly[index]) * W**index
                  for index in range(poly.degree() + 1)))


def forward_w_transform(poly):
    """Clear the inverse-map denominator after W_new=phi(W_old)."""
    poly = KW(poly)
    degree = poly.degree()
    return KW(sum(
        poly[index] * (u * W - 1)**index * (u - W)**(degree - index)
        for index in range(degree + 1)
    ))


def pulled_radical_factors(factors):
    result = set()
    for value in factors:
        pulled = parameter_pullback(value)
        for part in (pulled.numerator(), pulled.denominator()):
            normalized = strip_units(K(part))
            for item, _ in normalized.factor():
                if not item.is_constant():
                    result.add(str(primitive(item)))
    return sorted(result)


def evaluate_poly(poly, values):
    ring = PolynomialRing(QQ, "Y")
    y = ring.gen()
    substitutions = {bK: K(values[0]), cK: K(values[1]), dK: K(values[2])}
    return ring(sum(
        QQ(K(poly[index]).subs(substitutions)) * y**index
        for index in range(KW(poly).degree() + 1)
    ))


def forward_w_numeric(poly, values):
    ring = PolynomialRing(QQ, "Y")
    y = ring.gen()
    u_value = QQ(K(u).subs({bK: K(values[0])}))
    source = evaluate_poly(poly, values)
    degree = source.degree()
    return ring(sum(
        source[index] * (u_value * y - 1)**index
        * (u_value - y)**(degree - index)
        for index in range(degree + 1)
    ))


def projective_list_equal(left, right):
    if left.degree() != right.degree():
        return False
    return all(
        left[i] * right[j] == left[j] * right[i]
        for i in range(left.degree() + 1)
        for j in range(i + 1, left.degree() + 1)
    )


if os.environ.get("PAIR_SWAP_SEARCH", "0") == "1":
    samples = (
        (QQ(3), QQ(5), QQ(7)),
        (QQ(5) / 2, QQ(3), QQ(7)),
        (QQ(-2), QQ(3), QQ(5)),
    )
    matches = {}
    for assignment in ASSIGNMENTS:
        source_residuals, _ = cache[assignment]
        candidates = []
        for destination in ASSIGNMENTS:
            destination_residuals, _ = cache[destination]
            variants = []
            for variant in ("same-root-order", "swapped-root-order"):
                valid = True
                for values in samples:
                    bv, cv, dv = values
                    uv = (2 * bv - 1) / (bv - 2)
                    transform = lambda value: (uv * value + 1) / (value + uv)
                    destination_values = (transform(QQ(2)), transform(cv), transform(dv))
                    if variant == "swapped-root-order":
                        destination_values = (
                            destination_values[0], destination_values[2], destination_values[1]
                        )
                    for index in (0, 1):
                        destination_index = index if variant == "same-root-order" else 1 - index
                        if not projective_list_equal(
                            forward_w_numeric(source_residuals[index], values),
                            evaluate_poly(
                                destination_residuals[destination_index], destination_values
                            ),
                        ):
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    variants.append(variant)
            if variants:
                candidates.append({"assignment": destination, "variants": variants})
        matches[assignment] = candidates
    search_payload = {
        "schema": "kb-c2-112-near-literal-pair-swap-destination-search-v1",
        "samples": [[str(value) for value in sample] for sample in samples],
        "matches": matches,
        "terminal": "PAIR_SWAP_DESTINATION_SEARCH_COMPLETE",
    }
    print(
        "PAIR_SWAP_PROBE_JSON "
        + json.dumps(search_payload, sort_keys=True, separators=(",", ":"))
    )
    raise SystemExit(int(0))


residual_failures = []
target_failures = []
localizer_mismatches = []
checks = 0
assignment_filter = os.environ.get("PAIR_SWAP_ASSIGNMENT", "")
check_localizers = os.environ.get("PAIR_SWAP_LOCALIZERS", "0") == "1"
selected_assignments = (
    {assignment_filter: S_MAP[assignment_filter]}
    if assignment_filter
    else S_MAP
)
for assignment, destination in selected_assignments.items():
    source_residuals, source_systems = cache[assignment]
    destination_residuals, destination_systems = cache[destination]
    for index in (0, 1):
        if not projectively_equal(
            forward_w_transform(source_residuals[index]),
            parameter_pullback_poly(destination_residuals[index]),
        ):
            residual_failures.append({
                "assignment": assignment,
                "destination": destination,
                "endpoint": int(index),
            })
    for target_id, source_target in TARGETS.items():
        orbit, allocation = target_id.split("-")
        destination_target = f"{S_TARGET[orbit]}-{allocation}"
        for index in (0, 1):
            if not projectively_equal(
                forward_w_transform(source_target[index]),
                parameter_pullback_poly(TARGETS[destination_target][index]),
            ):
                target_failures.append({
                    "target": target_id,
                    "destination": destination_target,
                    "endpoint": int(index),
                })
        if check_localizers:
            source_factors = factor_set(source_systems[target_id], "I")
            destination_factors = pulled_radical_factors(
                destination_systems[destination_target]
            )
            if source_factors != destination_factors:
                localizer_mismatches.append({
                    "cell": f"{assignment}-{target_id}",
                    "destination": f"{destination}-{destination_target}",
                    "source_only": sorted(set(source_factors) - set(destination_factors)),
                    "destination_only": sorted(set(destination_factors) - set(source_factors)),
                })
        checks += 1

payload = {
    "schema": "kb-c2-112-near-literal-pair-swap-probe-v1",
    "assignment_filter": assignment_filter or "ALL",
    "localizers_checked": check_localizers,
    "checks": int(checks),
    "residual_failures": residual_failures,
    "target_failures": target_failures,
    "localizer_exact_cells": (
        int(checks - len(localizer_mismatches)) if check_localizers else None
    ),
    "localizer_mismatches": localizer_mismatches,
    "assignment_map": S_MAP,
    "target_map": S_TARGET,
    "b_prime": str(b_prime),
    "terminal": (
        "PAIR_SWAP_EXACT_PASS"
        if (
            check_localizers
            and not residual_failures
            and not target_failures
            and not localizer_mismatches
        )
        else (
            "PAIR_SWAP_CORE_PASS"
            if not check_localizers and not residual_failures and not target_failures
            else "PAIR_SWAP_CLASSIFIED"
        )
    ),
}
print(
    "PAIR_SWAP_PROBE_JSON "
    + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
)
