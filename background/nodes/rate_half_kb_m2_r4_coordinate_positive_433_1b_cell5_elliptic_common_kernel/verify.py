#!/usr/bin/env python3
"""Verify the positive 433-1b cell-5 common atlas and kernel."""

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCOUT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_modal.py"
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell5_complete_pivot_scout_result.json"
TOWER_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_modal.py"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
COMMON = EXP / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXP / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PINNED = {
    SCOUT_SCRIPT: "0f77351384d69fc31d212569b94d414fcfd8dc2b4cbd7970db86d4d0fb13095b",
    STRUCTURE: "12814c5e912c28a7ed1bdcc6d1550041cd8d297fb634e02ab0dca64dbf46e854",
    TOWER_SCRIPT: "6d0d78dea6e8b513ca75caed3d0ab70995f90c3e4072581a418da85d00db5847",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL_SCRIPT: "5025dd457ea0d10806120de5b67296d306d0c0bce9d89b307df023d2b412f4a2",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
P = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_structure():
    payload = json.loads(STRUCTURE.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-compact-pivot-scout-v3"
        and payload["field"] == P and payload["complete"]
        and payload["expected_rows"] == 24
        and payload["source_common_sha256"] == digest(COMMON)
        and payload["source_product_sha256"] == digest(PRODUCT),
        "structure custody",
    )
    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = set()
    signatures = {}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["chart"])
        require(key not in actual, "duplicate structure row")
        actual.add(key)
        require(
            row["cell"] == 5 and row["pivot"] == 1
            and row["status"] == "COMPLETE" and row["dimension"] == 1
            and row["basis_size"] == 17 and row["lex_basis_size"] == 8
            and row["quotient_basis_size"] == 8 and row["quotient_exact"]
            and row["quotient_remainders"] == ["0"] * 8,
            "common curve ledger",
        )
        require(
            row["pivot_boundary_unit"]
            and row["pivot_boundary_dimension"] == -1
            and row["pivot_boundary_size"] == 1,
            "pivot boundary",
        )
        require(
            all(row["projection_dimensions"][name] == 3
                and row["projection_sizes"][name] == 1
                for name in ("etr", "erb", "ebt", "erc")),
            "projection ledger",
        )
        signature = tuple(item["sha256"] for item in row["lex_basis"])
        signs = tuple(row["epsilon"])
        require(signs not in signatures or signatures[signs] == signature,
                "cofactor chart mismatch")
        signatures[signs] = signature
        require(not row["stderr"] and row["program_sha256"], "structure transcript")
    require(actual == expected and len(signatures) == 4, "24-chart cover")
    return signatures


def verify_discriminant(row):
    t, r = sp.symbols("t r")
    base = sp.Poly(sp.sympify(row["base"]["expression"]), t, r, modulus=P)
    require(base.degree(t) == 2 and base.degree(r) == 3
            and len(base.terms()) == 10, "base relation")
    discriminant = sp.Poly(sp.discriminant(base.as_expr(), t), r, modulus=P)
    recorded = sp.Poly(sp.sympify(row["base_discriminant"]["expression"]), r,
                       modulus=P)
    require(discriminant == recorded and discriminant.degree() == 6,
            "discriminant replay")
    profile = row["base_discriminant_factors"]
    rebuilt = sp.Poly(profile["coefficient"], r, modulus=P)
    factors = []
    for item in profile["factors"]:
        factor = sp.Poly(sp.sympify(item["expression"]), r, modulus=P).monic()
        factors.append((factor, item["multiplicity"]))
        rebuilt *= factor ** item["multiplicity"]
    require(rebuilt == discriminant
            and sorted((factor.degree(), multiplicity)
                       for factor, multiplicity in factors)
                == [(1, 1), (1, 1), (4, 1)],
            "discriminant factorization")
    quartic = next(factor for factor, _ in factors if factor.degree() == 4)
    linear = {factor.as_expr() for factor, _ in factors if factor.degree() == 1}
    require(linear == {r - 1, r + 1}
            and sp.gcd(quartic, quartic.diff()).degree() == 0,
            "guarded square-free quartic")


def verify_tower(signatures):
    payload = json.loads(TOWER.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-cell5-four-basis-tower-v1"
        and payload["field"] == P
        and payload["source_structure_sha256"] == digest(STRUCTURE),
        "tower custody",
    )
    expected = set(itertools.product((-1, 1), (-1, 1), (5, 6)))
    actual = set()
    bases = {}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["c_row_index"])
        require(key not in actual, "duplicate tower row")
        actual.add(key)
        c_index = row["c_row_index"]
        require(
            row["status"] == "COMPLETE" and row["exact"]
            and row["remainders"] == ["0"] * 8
            and row["kernel_dimension"] == 1
            and row["kernel_basis_size"] == 36
            and row["tower_dimension"] == 1
            and row["tower_basis_size"] == (38 if c_index == 5 else 37)
            and row["b_boundary_unit"]
            and row["b_boundary_dimension"] == -1
            and row["b_boundary_basis_size"] == 1,
            "tower equality",
        )
        if c_index == 6:
            require(row["c_boundary_unit"]
                    and row["c_boundary_dimension"] == -1
                    and row["c_boundary_basis_size"] == 1,
                    "boundary-free c recovery")
        else:
            require(not row["c_boundary_unit"]
                    and row["c_boundary_dimension"] == 0
                    and row["c_boundary_basis_size"] == 15,
                    "unused recovery boundary")
        require(row["b_palindromic"]
                and row["b_leading"]["expression"]
                    == row["b_constant"]["expression"],
                "palindromic b relation")
        verify_discriminant(row)
        signs = tuple(row["epsilon"])
        require(signs in signatures, "tower sign custody")
        require(signs not in bases or bases[signs] == row["base"]["sha256"],
                "recovery base mismatch")
        bases[signs] = row["base"]["sha256"]
        require(not row["stderr_tail"] and row["program_sha256"],
                "tower transcript")
    require(actual == expected and len(bases) == 4, "eight tower rows")


def verify_kernel(signatures):
    payload = json.loads(KERNEL.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-cell5-compact-kernel-v1"
        and payload["field"] == P and payload["cell"] == 5
        and payload["pivot"] == 1
        and payload["source_common_sha256"] == digest(COMMON)
        and payload["source_product_sha256"] == digest(PRODUCT)
        and payload["source_structure_sha256"] == digest(STRUCTURE),
        "kernel custody",
    )
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    kernel_signatures = set()
    shapes = ((15, 50), (15, 56), (13, 50), (16, 50),
              (16, 56), (14, 50), (15, 56), (15, 56))
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate kernel row")
        actual.add(signs)
        require(
            row["status"] == "COMPLETE" and row["all_rows_zero"]
            and row["remainders"] == ["0"] * 10
            and row["common_dimension"] == 1
            and row["common_basis_size"] == 33
            and row["identically_zero_rows"] == [True] * 7 + [False] * 3
            and tuple((item["degree"], item["terms"])
                      for item in row["kernel"]) == shapes
            and tuple(row["lex_signature"]) == signatures[signs],
            "exact kernel reduction",
        )
        kernel_signatures.add(tuple(item["sha256"] for item in row["kernel"]))
        require(not row["stderr_tail"] and row["program_sha256"],
                "kernel transcript")
    require(actual == expected and len(kernel_signatures) == 1,
            "one sign-independent kernel")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    signatures = verify_structure()
    verify_tower(signatures)
    verify_kernel(signatures)
    verify_dag()
    print("PASS cell-5 common kernel: charts=24 tower=8 kernel_rows=4")


if __name__ == "__main__":
    main()
