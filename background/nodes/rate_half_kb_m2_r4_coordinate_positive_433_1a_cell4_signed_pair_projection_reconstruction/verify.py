#!/usr/bin/env python3
"""Verify the cell-4 signed-pair projection and reconstruction."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_signed_pair_projection_reconstruction"
)
FILES = {
    "projection": "rate_half_kb_positive_433_1a_cell4_pair_w1_resultant_result.json",
    "factor": "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_result.json",
    "reconstruction": "rate_half_kb_positive_433_1a_cell4_pair_w1_reconstruction_result.json",
}
HASHES = {
    "projection": "462bebfdc3ae53c7dbf189205732573469b6771cfb05f999b90603a492b986db",
    "factor": "8158cce478bd8085e01bc78a4f87be144b5893025382d3585a9b2346455965a7",
    "reconstruction": "8ce61fe34937f099a67eecbf9038758bc61076568fc3b254fd9393747ab949f9",
}
PLANE_HASH = "26cc881846361a6f85d270dc436784991109f67982122b40cc4bbf75235e410e"
PAIR_SOURCE_HASH = "b15f88c44fdaf4b54c31f6eb86123c1e22b56e9b0f23fc9bae79c8646307b33c"
PRIME = 2130706433
I = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_file_row(row, expected_text=None):
    path = EXPERIMENTS / row["file"]
    require(hashlib.sha256(path.read_bytes()).hexdigest() ==
            row["file_sha256"], f"factor file hash {row['file']}")
    text = path.read_text().strip()
    require(hashlib.sha256(text.encode()).hexdigest() == row["sha256"],
            f"factor canonical hash {row['file']}")
    if expected_text is not None:
        require(text == expected_text, f"factor text {row['file']}")


def verify_payloads(projection, factor, reconstruction):
    require(projection["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-w1-resultant-v1",
            "projection schema")
    require(projection["status"] == "COMPLETE" and
            projection["result"]["status"] == "COMPLETE",
            "projection completion")
    require(projection["source_plane_sha256"] == PLANE_HASH,
            "projection plane chain")
    projected = projection["result"]
    require(projected["pseudo_steps"] == [3, 9] and
            projected["projected_pseudo_steps"] == 15,
            "projection pseudo steps")
    require(projected["resultant_shape"] == {
        "degrees": [0, 16, 18, 407], "terms": 130359,
        "total_degree": 434,
    }, "raw resultant shape")
    require(projected["primitive_shape"] == {
        "degrees": [0, 16, 3, 286], "terms": 19284,
        "total_degree": 298,
    }, "primitive projection shape")
    require(projected["primitive_sha256"] ==
            "a3ebb6a4e8e1f528aac254eee78a31d7bb7ef555ce1d16aad095ecffc6302216",
            "primitive canonical hash")

    require(factor["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-resultant-factor-v1",
            "factor schema")
    factored = factor["result"]
    require(factored["status"] == "COMPLETE" and
            factored["field"] == PRIME and
            factored["content"] == 2058485041,
            "factor completion")
    require(factored["source_polynomial_sha256"] ==
            projected["polynomial_file_sha256"], "factor source chain")
    factors = factored["factors"]
    require([(row["degrees"], row["terms"], row["multiplicity"])
             for row in factors] == [
        ([1, 0, 0], 2, 2), ([1, 0, 2], 2, 1),
        ([13, 3, 284], 15792, 1),
    ], "projection factor census")
    verify_file_row(factors[0], "w0 + 1")
    verify_file_row(factors[1], "w0 + 2130706432*t^2")
    verify_file_row(factors[2])

    require(reconstruction["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-w1-reconstruction-v3",
            "reconstruction schema")
    require(reconstruction["source_pair_sha256"] == PAIR_SOURCE_HASH and
            reconstruction["source_plane_sha256"] == PLANE_HASH,
            "reconstruction source chain")
    rebuilt = reconstruction["result"]
    require(rebuilt["status"] == "COMPLETE" and
            rebuilt["pseudo_steps"] == 3, "reconstruction completion")
    identity = rebuilt["resultant_identity"]
    require(identity["verified"] is True and
            identity["leading_exponent"] == 3 and
            identity["original_shape"] == projected["resultant_shape"],
            "resultant identity")
    plane = rebuilt["plane_reduction"]
    require(plane["steps"] == 9 and plane["compact_remainder_shape"] == {
        "degrees": [1, 9, 3, 181], "terms": 14312,
        "total_degree": 189,
    }, "compact reconstruction")
    discarded = plane["discarded_factors"]
    scale_rows = discarded["plane_content"]["factors"]
    expected_scales = [
        ("t + 2130706432", 5), ("t + 1", 7),
        ("t + 16711679", 45), ("t + 2113994754", 49),
    ]
    require([row["multiplicity"] for row in scale_rows] ==
            [row[1] for row in expected_scales], "scale multiplicities")
    for row, (text, _) in zip(scale_rows, expected_scales):
        verify_file_row(row, text)
    gcd_rows = discarded["polynomial_gcd"]["factors"]
    require(len(gcd_rows) == 1 and gcd_rows[0]["multiplicity"] == 1,
            "polynomial gcd census")
    verify_file_row(gcd_rows[0], "w0 + 1")

    coefficients = rebuilt["coefficients"]
    require(coefficients["linear"]["shape"] == {
        "degrees": [0, 9, 3, 181], "terms": 7176,
        "total_degree": 188,
    }, "linear coefficient shape")
    require(coefficients["constant"]["shape"] == {
        "degrees": [0, 9, 3, 181], "terms": 7136,
        "total_degree": 188,
    }, "constant coefficient shape")
    linear_factors = coefficients["linear"]["factors"]
    constant_factors = coefficients["constant"]["factors"]
    require(len(linear_factors) == 1 and
            linear_factors[0]["degrees"] == [0, 9, 3, 181] and
            linear_factors[0]["multiplicity"] == 1,
            "linear irreducibility")
    require(len(constant_factors) == 2 and
            constant_factors[0]["degrees"] == [0, 0, 0, 1] and
            constant_factors[1]["degrees"] == [0, 9, 3, 180] and
            all(row["multiplicity"] == 1 for row in constant_factors),
            "constant factorization")
    verify_file_row(linear_factors[0])
    verify_file_row(constant_factors[0], "t")
    verify_file_row(constant_factors[1])

    require(pow(I, 2, PRIME) == PRIME-1, "deployed square root of -1")
    for root in (1, PRIME-1, I, PRIME-I):
        require(root*(1-root*root)*(1+root*root) % PRIME == 0,
                f"main t guard {root}")


def main():
    payloads = {}
    for name, filename in FILES.items():
        path = EXPERIMENTS / filename
        require(hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[name],
                f"artifact hash {name}")
        payloads[name] = json.loads(path.read_text())
    verify_payloads(payloads["projection"], payloads["factor"],
                    payloads["reconstruction"])

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "does not impose the colored `BE` equations" in statement,
            "statement status and nonclaim")
    require("projection" in contract and "no converse" in contract and
            "nonclaim" in contract, "claim contract")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_scale_chart_exclusion",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-4 signed-pair reduction verified")


if __name__ == "__main__":
    main()
