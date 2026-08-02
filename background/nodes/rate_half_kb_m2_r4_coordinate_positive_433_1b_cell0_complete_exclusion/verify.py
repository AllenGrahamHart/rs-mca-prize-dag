#!/usr/bin/env python3
"""Verify complete exclusion of positive 433-1b role cell 0."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "charts_script": EXPERIMENTS / "rate_half_kb_positive_433_1b_principal_common_charts_modal.py",
    "charts_result": EXPERIMENTS / "rate_half_kb_positive_433_1b_principal_common_charts_result.json",
    "components_script": EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_modal.py",
    "components_result": EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json",
    "outside_script": EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_outside_modal.py",
    "outside_result": EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_outside_result.json",
}
HASHES = {
    "charts_script": "d2de06b6011105ddb5ddd95e93eff865ce01491d4b9b612dbac2cc703271b577",
    "charts_result": "c4bbba007d2d4b7a5cd40fd1afb299c5233eaf878b2fc5bee71b3b6e254bd9f5",
    "components_script": "271c5b9cc31ea9eff8981f4acd1d0b9055cc1ece1e9976c9ab7058a9873a2d8e",
    "components_result": "2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100",
    "outside_script": "143e99979eb6d3d2a94974f6e0a02f59c675f3d9487dc7851e25e6fef9c9d749",
    "outside_result": "077912af339ab60ef17036b69e15f06b93a0d2dd1cca89a32eb065dc3d2fb23b",
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
IOTA = 16711679
ZFREE_HASHES = {
    -1: "bfda1867367e6506ed45a3bd0e16b4a592d51b8e234f7d42a491b55816be8a65",
    1: "0f62b7d4451491c599ecd341079987b1f02adf3e164814d595cdf3db09897b53",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def zfree_basis(row):
    return tuple(
        line.split("=", 1)[1]
        for line in row["stdout"].splitlines()
        if line.startswith("G[") and "z" not in line.split("=", 1)[1]
    )


def verify_charts(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-principal-common-charts-v1", "chart schema")
    require(payload["app"] == "rs-mca-positive-433-1b-principal-common-charts" and
            payload["field"] == PRIME, "chart app/field")
    require(payload["case_count"] == 24 and
            payload["status_counts"] == {"COMPLETE": 24} and
            payload["unit_count"] == 12 and payload["nonunit_count"] == 12,
            "chart aggregate")
    expected = set(itertools.product((0,), (-1, 1), (-1, 1), range(6)))
    actual = set()
    references = {}
    for row in payload["rows"]:
        key = (row["cell"], *row["epsilon"], row["chart"])
        require(key not in actual, "duplicate chart")
        actual.add(key)
        require(row["status"] == "COMPLETE" and not row["stderr"], "chart completion")
        require(row["singleton"] == "LA" and row["matching"] ==
                [["AB", "AC"], ["BC+", "BC-"]], "cell-0 role shape")
        e1, e2 = row["epsilon"]
        if e1 != e2:
            require(row["unit"] and row["dimension"] == -1 and
                    row["basis_size"] == 1 and "UNIT=1" in row["stdout"],
                    "mixed-sign chart")
        else:
            basis = zfree_basis(row)
            require(not row["unit"] and row["dimension"] == 1 and
                    row["basis_size"] == 14 and len(basis) == 7,
                    "equal-sign chart")
            basis_hash = hashlib.sha256("\n".join(basis).encode()).hexdigest()
            require(basis_hash == ZFREE_HASHES[e1], "equal-sign basis digest")
            references.setdefault(e1, basis)
            require(references[e1] == basis, "chart-independent basis")
    require(actual == expected, "chart Cartesian product")
    require(references[1][0] == references[-1][0] == "c2+b2", "quadratic split")
    require(references[1][1] == "rc-16711679rb-cb+16711679b2", "positive G2")
    require(references[-1][1] == "rc+16711679rb-cb-16711679b2", "negative G2")
    require(references[1][5] == "t2r+8355840t2+8355840r2+16711679r",
            "positive G6")
    require(references[-1][5] == "t2r-8355839t2-8355839r2-16711679r",
            "negative G6")


def verify_components(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell0-principal-components-v2", "component schema")
    require(payload["app"] == "rs-mca-positive-433-1b-cell0-principal-components" and
            payload["field"] == PRIME, "component app/field")
    expected = set(itertools.product(("A", "B"), (-1, 1)))
    actual = set()
    b, t = sp.symbols("b t")
    inverse_two = pow(2, -1, PRIME)
    for row in payload["rows"]:
        key = (row["component"], row["source_sign"])
        require(key not in actual, "duplicate component")
        actual.add(key)
        require(row["all_rows_zero"] and len(row["row_checks"]) == 10 and
                all(item["zero"] for item in row["row_checks"]), "common replay")
        require(len(row["kernel"]) == 8 and
                all(item["expression"] != "0" for item in row["kernel"]),
                "component kernel")
        for item in [row["relation"], *row["kernel"]]:
            polynomial = sp.Poly(sp.sympify(item["expression"]), t, b, modulus=PRIME)
            text = str(polynomial.as_expr())
            require(hashlib.sha256(text.encode()).hexdigest() == item["sha256"] and
                    polynomial.total_degree() == item["degree"] and
                    len(polynomial.terms()) == item["terms"], "component summary")
        component, source_sign = key
        alpha = (1 + source_sign*IOTA)*inverse_two % PRIME
        if component == "A":
            expected_relation = t*t*b*(1 + alpha*b) + alpha + source_sign*IOTA*b
        else:
            expected_relation = t*t*(b + alpha) + b*(alpha*b + source_sign*IOTA)
        require(sp.Poly(sp.sympify(row["relation"]["expression"]) - expected_relation,
                        t, b, modulus=PRIME).is_zero, "component relation")
    require(actual == expected, "component Cartesian product")


def verify_outside(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell0-principal-outside-v2", "outside schema")
    require(payload["app"] == "rs-mca-positive-433-1b-cell0-principal-outside" and
            payload["field"] == PRIME, "outside app/field")
    require(payload["source_components_sha256"] == HASHES["components_result"],
            "component custody")
    require(payload["component_count"] == 2 and payload["source_sign_count"] == 2 and
            payload["lane_count"] == 16 and payload["case_count"] == 1680 and
            payload["status_counts"] == {"COMPLETE": 1680} and
            payload["unit_count"] == 1680, "outside aggregate")
    expected = set(itertools.product(
        ("A", "B"), (-1, 1), (-1, 1), (-1, 1), range(7), range(15)
    ))
    actual = set()
    program_hashes = set()
    for row in payload["rows"]:
        key = (row["component"], row["source_sign"], *row["sigma"],
               row["xi_index"], row["pairing_index"])
        require(key not in actual, "duplicate outside case")
        actual.add(key)
        require(row["status"] == "COMPLETE" and row["unit"] and
                row["dimension"] == -1 and row["basis_size"] == 1 and
                "UNIT=1" in row["stdout"] and "END" in row["stdout"] and
                "SAT=0" in row["stdout"] and not row["stderr"], "outside unit")
        require(not row["input_polynomials"] and not row["guard_factors"],
                "unexpected nonunit diagnostics")
        require(len(row["program_sha256"]) == 64, "program digest")
        program_hashes.add(row["program_sha256"])
    require(actual == expected, "outside Cartesian product")
    require(len(program_hashes) == 1440, "outside program census")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer edge")


def main():
    for key, path in FILES.items():
        require(path.is_file() and digest(path) == HASHES[key], f"custody {key}")
    require(IOTA*IOTA % PRIME == PRIME - 1, "iota square")
    inverse_two = pow(2, -1, PRIME)
    gamma = 1056997377
    negative_half = 1065353216
    require(gamma*IOTA % PRIME == inverse_two and
            (gamma*IOTA + negative_half) % PRIME == 0 and
            (-gamma*IOTA + negative_half) % PRIME == PRIME - 1,
            "G3 component factor arithmetic")
    require(len(tuple(pairings(range(6)))) == 15, "perfect matching census")
    verify_charts(json.loads(FILES["charts_result"].read_text()))
    verify_components(json.loads(FILES["components_result"].read_text()))
    verify_outside(json.loads(FILES["outside_result"].read_text()))
    verify_dag()
    print("cell0_charts=24 mixed_unit=12 components=4 outside_unit=1680")


if __name__ == "__main__":
    main()
