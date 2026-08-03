#!/usr/bin/env python3
"""Verify the positive 433-1b cell-4 four-basis tower and kernel."""

import hashlib
import itertools
import json
from pathlib import Path
import re

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
STRUCTURE_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_modal.py"
)
STRUCTURE_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_modal.py"
)
KERNEL_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
)
PINNED = {
    STRUCTURE_SCRIPT: "5ff188b7cb1e4f6218b82f17f2a080c4011a9dee993c6825b1d31fdb04ff98af",
    STRUCTURE_RESULT: "53e7e23afe164a94a677d2f3be044b1e25542d9c3d0ab6850efd1f0029002a33",
    KERNEL_SCRIPT: "2c04bf0d1500024c54874bb5a18163d71a370406ece7cd1d8d00c4e7bfe1bbba",
    KERNEL_RESULT: "52d40fe51d713eeb6c92217d4bd0024dfd9fa29118c44cfa64592c0da350fdab",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
PRIME = 2130706433
t, r, c, b = sp.symbols("t r c b")
SYMBOLS = {"t": t, "r": r, "c": c, "b": b}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_singular(text, variables):
    expression = 0
    for term in re.findall(r"[+-]?[^+-]+", text):
        sign = -1 if term.startswith("-") else 1
        unsigned = term.lstrip("+-")
        digits = re.match(r"\d*", unsigned).group()
        monomial = sp.Integer(sign * int(digits or "1"))
        for variable, exponent in re.findall(
            r"([trcb])(\d*)", unsigned[len(digits):]
        ):
            monomial *= SYMBOLS[variable] ** int(exponent or "1")
        expression += monomial
    return sp.Poly(expression, *variables, modulus=PRIME)


def verify_structure(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-compact-pivot-scout-v3",
            "structure schema")
    require(payload["field"] == PRIME and
            payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT),
            "structure custody")
    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = set()
    signatures = {}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["chart"])
        require(key not in actual, "duplicate structure row")
        actual.add(key)
        require(row["cell"] == 4 and row["pivot"] == 1 and
                row["status"] == "COMPLETE" and
                row["dimension"] == 1 and row["basis_size"] == 16,
                "common curve")
        require(row["pivot_boundary_unit"] and
                row["pivot_boundary_dimension"] == -1 and
                row["pivot_boundary_size"] == 1, "pivot boundary")
        require(row["lex_basis_size"] == 9 and
                row["quotient_basis_size"] == 9 and
                row["quotient_exact"] and
                row["quotient_remainders"] == ["0"] * 9,
                "localized quotient equality")
        require(all(row["projection_dimensions"][name] == 3 and
                    row["projection_sizes"][name] == 1
                    for name in ("etr", "erb", "ebt", "erc")),
                "projection ledger")
        signature = tuple(value["sha256"] for value in row["lex_basis"])
        signs = tuple(row["epsilon"])
        require(signs not in signatures or signatures[signs] == signature,
                "chart lex mismatch")
        signatures[signs] = signature

        base = parse_singular(row["lex_basis"][0]["expression"], (t, r))
        b_relation = parse_singular(
            row["lex_basis"][1]["expression"], (b, t, r)
        )
        c_relation = parse_singular(
            row["lex_basis"][5]["expression"], (c, b, t, r)
        )
        require(base.degree(t) == 2 and base.degree(r) == 3 and
                len(base.terms()) == 10, "base shape")
        discriminant = sp.Poly(
            sp.discriminant(base.as_expr(), t), r, modulus=PRIME
        )
        require(discriminant.degree() == 6 and
                sp.gcd(discriminant, discriminant.diff()).degree() == 0,
                "square-free degree-six discriminant")

        b_polynomial = sp.Poly(b_relation.as_expr(), b)
        b_leading = sp.Poly(
            b_polynomial.coeff_monomial(b**2), t, r, modulus=PRIME
        )
        b_constant = sp.Poly(
            b_polynomial.coeff_monomial(1), t, r, modulus=PRIME
        )
        require(b_polynomial.degree() == 2 and len(b_relation.terms()) == 18 and
                b_leading == b_constant, "palindromic b relation")
        eta = row["epsilon"][0] * row["epsilon"][1]
        expected_b = (
            r * (r - 1) * (r + 1)**2 if eta == 1
            else r * (r + 1) * (r - 1)**2
        )
        require(sp.Poly(
            b_leading.as_expr() - expected_b, t, r, modulus=PRIME
        ).is_zero, "b leading guard identity")

        c_polynomial = sp.Poly(c_relation.as_expr(), c)
        c_leading = sp.Poly(
            c_polynomial.coeff_monomial(c), t, r, modulus=PRIME
        )
        expected_c = (
            (t + 1) * (r - 1) if eta == 1
            else (t - 1) * (r + 1)
        )
        require(c_polynomial.degree() == 1 and len(c_relation.terms()) == 10 and
                sp.Poly(c_leading.as_expr() - expected_c,
                        t, r, modulus=PRIME).is_zero,
                "c recovery guard identity")
        require(not row["stderr"] and row["program_sha256"],
                "structure transcript")
    require(actual == expected and len(signatures) == 4, "24-chart cover")


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell4-compact-kernel-v1",
            "kernel schema")
    require(payload["field"] == PRIME and payload["cell"] == 4 and
            payload["pivot"] == 1 and
            payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT) and
            payload["source_structure_sha256"] == digest(STRUCTURE_RESULT),
            "kernel custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    kernel_digests = set()
    shapes = ((15, 50), (15, 56), (13, 50), (16, 50),
              (16, 56), (14, 50), (15, 72), (15, 72))
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate kernel row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and
                row["all_rows_zero_mod_common"], "kernel completion")
        require(tuple((value["degree"], value["terms"])
                      for value in row["kernel"]) == shapes, "kernel shapes")
        require(row["identically_zero_rows"] == [True] * 7 + [False] * 3,
                "identical row ledger")
        require(row["reduced_remainders"] == ["0"] * 10,
                "ten zero reductions")
        require(row["common_dimension"] == 2 and
                row["common_basis_size"] == 85 and not row["stderr"],
                "kernel transcript")
        require(row["product_kernel_removed_gcd"]["degree"] == 0 and
                row["final_kernel_removed_gcd"]["degree"] == 3 and
                row["final_kernel_removed_gcd"]["terms"] == 2,
                "kernel gcd ledger")
        kernel_digests.add(tuple(value["sha256"] for value in row["kernel"]))
    require(actual == expected and len(kernel_digests) == 1,
            "four identical kernels")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_structure(json.loads(STRUCTURE_RESULT.read_text()))
    verify_kernel(json.loads(KERNEL_RESULT.read_text()))
    verify_dag()
    print("cell=4 charts=24 tower_basis=4 base_genus=2 kernels=4 rows=40")


if __name__ == "__main__":
    main()
