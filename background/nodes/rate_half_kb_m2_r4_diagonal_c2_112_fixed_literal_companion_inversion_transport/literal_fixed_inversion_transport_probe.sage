#!/usr/bin/env sage
"""Audit full-system b-inversion for the two fixed literal companion pairs."""

import argparse
import hashlib
import json
from pathlib import Path


MOVING = Path(
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_moving_closure_v1.sage"
)


def load_moving():
    namespace = dict(globals())
    namespace.update(
        {"__name__": "moving_closure_library", "__file__": str(MOVING)}
    )
    exec(compile(MOVING.read_text(), str(MOVING), "exec"), namespace)
    return namespace


def digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def audit_pair(library, source_id, target_id):
    atlas = library["ATLAS"]
    R = library["R"]
    K = library["K"]
    b, c, d, w = R.gens()
    pull_b_K = library["pull_b_K"]
    pull_b_KW = library["pull_b_KW"]
    check_multiset = library["check_multiset"]
    build_source_R = library["build_source_R"]
    named_units_R = library["named_units_R"]
    factor_key = library["factor_key"]
    primitive_R = library["primitive_R"]
    reverse_b_R = library["reverse_b_R"]
    denominator_support_R = library["denominator_support_R"]

    source_u, source_v, source_z = build_source_R(source_id)
    target_u, target_v, target_z = build_source_R(target_id)
    source_exact = {
        "z": pull_b_K(source_z) == target_z,
        "V": vector(atlas["KW"], (pull_b_KW(value) for value in source_v))
        == target_v,
        "U": vector(atlas["KW"], (pull_b_KW(value) for value in source_u))
        == target_u,
    }
    assert all(source_exact.values())

    bK, cK, dK, wK = map(K, R.gens())
    source_J = [K(2), K(1) / 2, bK, 1 / bK, cK, dK]
    target_J = list(source_J)
    source_I = [1 / cK, 1 / dK, wK, 1 / wK, source_z, 1 / source_z]
    target_I = [1 / cK, 1 / dK, wK, 1 / wK, target_z, 1 / target_z]
    source_K = [wK, source_z, 1 / source_z, 1 / cK, 1 / dK]
    target_K = [wK, target_z, 1 / target_z, 1 / cK, 1 / dK]
    source_R_labels = [1 / wK, *source_J]
    target_R_labels = [1 / wK, *target_J]
    label_checks = {}
    for name, source_labels, target_labels in (
        ("J", source_J, target_J),
        ("I", source_I, target_I),
        ("K", source_K, target_K),
        ("R", source_R_labels, target_R_labels),
    ):
        label_checks[name] = check_multiset(
            [pull_b_K(value) for value in source_labels], target_labels
        )
    assert all(label_checks.values())

    source_units = list(named_units_R(source_id).values())
    target_units = list(named_units_R(target_id).values())
    source_nonmonomial = [
        factor for factor in source_units if factor_key(factor) != factor_key(b)
    ]
    target_nonmonomial = [
        factor for factor in target_units if factor_key(factor) != factor_key(b)
    ]
    pulled_units = [primitive_R(reverse_b_R(factor)) for factor in source_nonmonomial]
    named_units_exact = check_multiset(pulled_units, target_nonmonomial)
    assert named_units_exact

    KW = atlas["KW"]
    W = atlas["W"]
    KT = PolynomialRing(KW, "Tsource")
    Tsource = KT.gen()

    def source_polynomial(coefficients):
        return KT(sum(KT(coefficients[index]) * Tsource**index for index in range(3)))

    def G_polynomial(u_values, v_values):
        U = source_polynomial(u_values)
        V = source_polynomial(v_values)
        return U**2 - KT(W) * V**2

    def pull_KT(value):
        value = KT(value)
        return KT([pull_b_KW(value[index]) for index in range(value.degree() + 1)])

    source_G = G_polynomial(source_u, source_v)
    target_G = G_polynomial(target_u, target_v)
    G_exact = pull_KT(source_G) == target_G
    assert G_exact

    def G_values(G, labels):
        return [KW(G(KW(label))) for label in labels]

    J_G_exact = check_multiset(
        [pull_b_KW(value) for value in G_values(source_G, source_J)],
        G_values(target_G, target_J),
    )
    I_G_exact = check_multiset(
        [pull_b_KW(value) for value in G_values(source_G, source_I)],
        G_values(target_G, target_I),
    )
    assert J_G_exact and I_G_exact

    LT = PolynomialRing(K, "Ylabel")
    Ylabel = LT.gen()

    def locator(labels):
        return prod((Ylabel - K(label) for label in labels), LT(1))

    def pull_LT(value):
        value = LT(value)
        return LT([pull_b_K(value[index]) for index in range(value.degree() + 1)])

    source_q = (Ylabel - cK) * (Ylabel - dK)
    target_q = (Ylabel - cK) * (Ylabel - dK)
    locator_checks = {
        "q": pull_LT(source_q) == target_q,
        "K": pull_LT(locator(source_K)) == locator(target_K),
        "R": pull_LT(locator(source_R_labels)) == locator(target_R_labels),
    }
    assert all(locator_checks.values())

    atlas["build_assignment"](source_id)
    atlas["build_assignment"](target_id)
    qslice_checks = []
    for target in ("R02", "R11", "R20"):
        source_rows = atlas["RAW_CACHE"][f"{source_id}-{target}"]
        target_rows = atlas["RAW_CACHE"][f"{target_id}-{target}"]
        assert len(source_rows) == len(target_rows) == 4
        rows = []
        for index, (source, target_row) in enumerate(zip(source_rows, target_rows)):
            source_rational = K(source)
            target_rational = K(target_row)
            source_support = denominator_support_R(
                primitive_R(source_rational.denominator()), named_units_R(source_id)
            )
            target_support = denominator_support_R(
                primitive_R(target_rational.denominator()), named_units_R(target_id)
            )
            ratio = K(pull_b_K(source_rational) / target_rational)
            ratio_numerator_support = denominator_support_R(
                primitive_R(ratio.numerator()), named_units_R(target_id)
            )
            ratio_denominator_support = denominator_support_R(
                primitive_R(ratio.denominator()), named_units_R(target_id)
            )
            pulled_numerator = primitive_R(
                reverse_b_R(primitive_R(source_rational.numerator()))
            )
            target_numerator = primitive_R(target_rational.numerator())
            numerator_exact = pulled_numerator in (target_numerator, -target_numerator)
            assert numerator_exact
            rows.append(
                {
                    "index": index,
                    "cleared_numerator_up_to_sign": numerator_exact,
                    "source_denominator": source_support,
                    "target_denominator": target_support,
                    "ratio_numerator": ratio_numerator_support,
                    "ratio_denominator": ratio_denominator_support,
                    "pulled_numerator_sha256": digest(pulled_numerator),
                    "target_numerator_sha256": digest(target_numerator),
                }
            )
        qslice_checks.append(
            {
                "source_cell": f"{source_id}-{target}",
                "target_cell": f"{target_id}-{target}",
                "row_count": len(rows),
                "all_rows_exact": all(row["cleared_numerator_up_to_sign"] for row in rows),
                "rows": rows,
            }
        )

    return {
        "map": "b -> b^-1",
        "source_assignment": source_id,
        "target_assignment": target_id,
        "source_coefficients_exact": source_exact,
        "label_factor_multisets_exact": label_checks,
        "named_open_transport": {
            "b_chart_invariant": True,
            "source_factor_count": len(source_units),
            "target_factor_count": len(target_units),
            "nonmonomial_factor_multiset_exact": named_units_exact,
        },
        "full_identity_transport": {
            "G_exact": G_exact,
            "J_G_factor_multiset_exact": J_G_exact,
            "I_G_factor_multiset_exact": I_G_exact,
            "locator_checks": locator_checks,
            "full_J_exact": J_G_exact and locator_checks["K"] and locator_checks["q"],
            "full_I_exact": I_G_exact and locator_checks["R"] and locator_checks["q"],
        },
        "qslice_checks": qslice_checks,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", choices=("F04-F05", "F06-F07"), required=True)
    args = parser.parse_args()
    source_id, target_id = args.pair.split("-")
    result = audit_pair(load_moving(), source_id, target_id)
    packet = {
        "schema": "kb-c2-112-fixed-literal-companion-inversion-transport-v1",
        "result": result,
    }
    print(json.dumps(packet, sort_keys=True))
    print(f"PASS fixed literal inversion transport {args.pair}")


if __name__ == "__main__":
    main()
