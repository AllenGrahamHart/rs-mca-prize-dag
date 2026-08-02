#!/usr/bin/env python3
"""Verify the cell-4 main projection guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_main_projection_guard_factorization_exclusion"
)
RESULT_FILE = (
    "rate_half_kb_positive_433_1a_cell4_main_projection_"
    "guard_factorization_result.json"
)
SCRIPT_FILE = (
    "rate_half_kb_positive_433_1a_cell4_main_projection_"
    "guard_factorization_modal.py"
)
RESULT_HASH = "0772e51e34f71820af3e6bbddb9a53b2466093ebc31b922db39d8acca1b171ad"
SCRIPT_HASH = "1a0bc0cf72aa563702bdd7ebc798de7c957c85acfbdcbc96a5d623addf54a7b9"
PLANE_HASH = "26cc881846361a6f85d270dc436784991109f67982122b40cc4bbf75235e410e"
F_HASH = "af0c74a85dcb83c3245f5a93045206a431e06019fbbd3d690621d010fd9af10c"
PRIME = 2130706433
I = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-main-guard-factorization-v1",
            "schema")
    require(payload["artifact_sha256"] == {
        "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt": F_HASH,
        "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json": PLANE_HASH,
    }, "input custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "completion")
    require(result["identity"] ==
            "plane-reduced(N0*D0^5*(rd^2*w0-rn^2))=Q(t)*F",
            "identity label")
    require(result["plane_leading"] == "t^4 + 2*t^2 + 1" and
            result["plane_leading_exponent"] == 21, "plane scale")
    require(result["plane_shape"] == {
        "degrees": [0, 4, 4], "terms": 21, "total_degree": 8,
    }, "plane shape")
    require(result["f_shape"] == {
        "degrees": [13, 3, 284], "terms": 15792, "total_degree": 294,
    }, "F shape")
    require(result["n0_shape"] == result["d0_shape"] == {
        "degrees": [2, 3, 18], "terms": 220, "total_degree": 22,
    }, "N0/D0 shapes")
    require(result["source_guard_shape"] == {
        "degrees": [1, 3, 20], "terms": 94, "total_degree": 23,
    }, "source guard shape")
    require(result["candidate_shape"] == {
        "degrees": [13, 3, 200], "terms": 11088, "total_degree": 210,
    } and result["candidate_sha256"] ==
            "f78456d1baf487788a633e7b1768569d0a4bda67e84565236f1a12396c0f44a8",
            "candidate certificate")

    reductions = result["reductions"]
    require([row["operation"] for row in reductions] == [
        "d0_power_2", "d0_power_3", "d0_power_4", "d0_power_5",
        "source_guard", "n0_times_d0_fifth", "times_source_guard",
    ], "reduction operations")
    require([row["steps"] for row in reductions] == [3]*7,
            "reduction steps")
    require(sum(row["steps"] for row in reductions) ==
            result["plane_leading_exponent"], "scale reconstruction")

    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3, "quotient-ring identity")
    require(cross["f_leading_sha256"] ==
            "6182823e255440f80b3ea00d790cc92659f11138c8ce99830ec5abc227ef0447" and
            cross["candidate_leading_sha256"] ==
            "d62adba3b28a858e2366cbca85918e3336765a650ae5c6c7e29ea0d949a33784",
            "leading coefficients")
    diagnostic = result["ambient_division_diagnostic"]
    require(diagnostic["remainder_zero"] is False,
            "ambient division must not replace quotient identity")

    norm = result["f_leading_norm"]
    require(norm["content"] == 1221358375 and norm["shape"] == {
        "degrees": [0, 0, 1124], "terms": 1125, "total_degree": 1124,
    } and norm["sha256"] ==
            "0bb5e2786ff5e518dc802334d2f78d442512e8ea1f503ca41f106895fdc21e64",
            "leading norm")
    expected = [
        (6, "t^2 + 1457968268*t + 1019305654"),
        (6, "t^3 + 622603126*t^2 + 1463338870*t + 1228312035"),
        (24, "t^3 + 2097283074*t^2 + 2097283076*t + 2130706432"),
        (36, "t + 1"),
        (68, "t + 2130706432"),
        (98, "t + 16711679"),
        (144, "t^3 + 2097283076*t^2 + 33423359*t + 1"),
        (388, "t + 2113994754"),
    ]
    require([(row["multiplicity"], row["text"])
             for row in norm["factors"]] == expected, "norm factors")
    for row in norm["factors"]:
        require(hashlib.sha256(row["text"].encode()).hexdigest() ==
                row["sha256"], "norm factor hash")

    require(pow(I, 2, PRIME) == PRIME-1, "deployed i")
    roots = [PRIME-1, 1, PRIME-I, I]
    for root in roots:
        require(root*(1-root*root)*(1+root*root) % PRIME == 0,
                f"guard root {root}")


def main():
    result_path = EXPERIMENTS / RESULT_FILE
    script_path = EXPERIMENTS / SCRIPT_FILE
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == RESULT_HASH,
            "result artifact hash")
    require(hashlib.sha256(script_path.read_bytes()).hexdigest() == SCRIPT_HASH,
            "generator hash")
    payload = json.loads(result_path.read_text())
    verify_payload(payload)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "orbit `[4,7]` is PROVED excluded" in statement,
            "statement status")
    require("other five positive representatives" in contract and
            "either Prize result" in contract, "contract nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_scale_chart_exclusion",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_signed_pair_projection_reconstruction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-4 main guard factorization verified")


if __name__ == "__main__":
    main()
