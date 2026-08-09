#!/usr/bin/env python3
"""Verify the positive 433-1b cell-11 common-locus theorem."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCOUT_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_modal.py"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_complete_pivot_scout_result.json"
)
TOWER_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_modal.py"
)
TOWER = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
)
BOUNDARY_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_tower_boundary_modal.py"
)
BOUNDARY = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_tower_boundary_result.json"
)
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
)
PINNED = {
    SCOUT_SCRIPT: "0f77351384d69fc31d212569b94d414fcfd8dc2b4cbd7970db86d4d0fb13095b",
    STRUCTURE: "7c91aad3b83d1e87dceb2850ae5d20c631ae4a6d598f9a5d02aa3feb5158582a",
    TOWER_SCRIPT: "927e4bfea6fdb18ad0b8cdf7312e301bc826d166dbd2d41d1855958a4be049b2",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    BOUNDARY_SCRIPT: "f755dca238ee4ffaf6fc190e2c247eedf6a268f5024268ba2a9ba1e0b208bf5f",
    BOUNDARY: "ec6bcdfb4575bbada93f481ab5fdb8f196838d416b1a8fbc599d5850d5b67685",
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
r, t = sp.symbols("r t")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def polynomial(text, *variables):
    return sp.Poly(sp.sympify(text), *variables, modulus=PRIME)


def verify_structure(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-compact-pivot-scout-v3",
            "structure schema")
    require(payload["field"] == PRIME and payload["complete"] and
            payload["expected_rows"] == 24 and
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
        require(row["cell"] == 11 and row["pivot"] == 1 and
                row["status"] == "COMPLETE" and row["dimension"] == 1 and
                row["basis_size"] == 20 and row["lex_basis_size"] == 8,
                "common curve ledger")
        require(row["pivot_boundary_unit"] and
                row["pivot_boundary_dimension"] == -1 and
                row["pivot_boundary_size"] == 1, "pivot boundary")
        require(all(row["projection_dimensions"][name] == 3 and
                    row["projection_sizes"][name] == 1
                    for name in ("etr", "erb", "ebt", "erc")),
                "projection ledger")
        signature = tuple(item["sha256"] for item in row["lex_basis"])
        signs = tuple(row["epsilon"])
        require(signs not in signatures or signatures[signs] == signature,
                "cofactor-chart lex mismatch")
        signatures[signs] = signature
        require(not row["stderr"] and row["program_sha256"],
                "structure transcript")
    require(actual == expected and len(signatures) == 4,
            "24-chart structure cover")
    return signatures


def verify_factorization(row):
    base = polynomial(row["base"]["expression"], t, r)
    require(base.degree(t) == 2 and base.degree(r) == 4 and
            len(base.terms()) == 11, "base relation shape")
    discriminant = polynomial(
        str(sp.discriminant(base.as_expr(), t)), r
    )
    recorded = polynomial(row["base_discriminant"]["expression"], r)
    require(discriminant == recorded and discriminant.degree() == 8,
            "base discriminant replay")
    profile = row["base_discriminant_factors"]
    rebuilt = sp.Poly(profile["coefficient"], r, modulus=PRIME)
    factor_degrees = []
    multiplicities = []
    for item in profile["factors"]:
        factor = polynomial(item["expression"], r).monic()
        multiplicity = item["multiplicity"]
        rebuilt *= factor ** multiplicity
        factor_degrees.append(factor.degree())
        multiplicities.append(multiplicity)
    require(rebuilt == discriminant and
            sorted(factor_degrees) == [1, 1, 2, 4] and
            multiplicities == [1, 1, 1, 1],
            "discriminant factorization")
    require(sp.gcd(discriminant, discriminant.diff()).degree() == 0,
            "square-free degree-eight normalization")


def verify_tower(payload, structure_signatures):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell11-four-basis-tower-v1" and
            payload["field"] == PRIME and
            payload["source_structure_sha256"] == digest(STRUCTURE),
            "tower custody")
    expected = set(itertools.product((-1, 1), (-1, 1), (5, 6)))
    actual = set()
    bases = {}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["c_row_index"])
        require(key not in actual, "duplicate tower row")
        actual.add(key)
        c_index = row["c_row_index"]
        require(row["status"] == "COMPLETE" and row["exact"] and
                row["remainders"] == ["0"] * 8 and
                row["kernel_dimension"] == 1 and
                row["kernel_basis_size"] == 36 and
                row["tower_dimension"] == 1 and
                row["tower_basis_size"] == (43 if c_index == 5 else 39),
                "tower equality")
        require(row["b_palindromic"] and
                row["b_leading"]["expression"] ==
                row["b_constant"]["expression"],
                "palindromic b extension")
        require(not row["b_boundary_unit"] and
                row["b_boundary_dimension"] == 0 and
                row["b_boundary_basis_size"] == 15 and
                not row["c_boundary_unit"] and
                row["c_boundary_dimension"] == 0 and
                row["c_boundary_basis_size"] == (15 if c_index == 5 else 21),
                "leading-boundary dimensions")
        signs = tuple(row["epsilon"])
        require(signs in structure_signatures, "tower sign custody")
        verify_factorization(row)
        base_digest = row["base"]["sha256"]
        require(signs not in bases or bases[signs] == base_digest,
                "two recoveries disagree on base")
        bases[signs] = base_digest
        require(not row["stderr_tail"] and row["program_sha256"],
                "tower transcript")
    require(actual == expected and len(bases) == 4, "eight tower rows")


def verify_boundary(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell11-tower-boundary-v1" and
            payload["field"] == PRIME and
            payload["source_structure_sha256"] == digest(STRUCTURE) and
            payload["source_tower_sha256"] == digest(TOWER),
            "boundary custody")
    actual = set()
    counts = {}
    for row in payload["rows"]:
        key = (*row["epsilon"], row["boundary"], row["r"])
        require(key not in actual, "duplicate boundary row")
        actual.add(key)
        require(row["status"] == "COMPLETE" and not row["unit"] and
                row["dimension"] == 0 and row["basis_size"] == 4 and
                row["lex_basis_size"] == 4 and
                len(row["linear_t_roots"]) == 1 and
                not row["stderr_tail"], "boundary fiber")
        signs = tuple(row["epsilon"])
        counts.setdefault(signs, {"b_leading": 0, "c_leading": 0})
        counts[signs][row["boundary"]] += 1
        require(len(row["b_factors"]) == 1 and
                row["b_factors"][0]["degree"] == 2 and
                row["rational_points"] == [], "nonsplit boundary")
    expected_counts = {
        signs: {"b_leading": 1, "c_leading": 1}
        for signs in itertools.product((-1, 1), repeat=2)
    }
    require(len(actual) == 8 and counts == expected_counts,
            "eight-fiber boundary cover")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges,
                f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    signatures = verify_structure(json.loads(STRUCTURE.read_text()))
    verify_tower(json.loads(TOWER.read_text()), signatures)
    verify_boundary(json.loads(BOUNDARY.read_text()))
    verify_dag()
    print("cell=11 charts=24 base_genus=3 boundary_fibers=8 rational_points=0")


if __name__ == "__main__":
    main()
