#!/usr/bin/env python3
"""Verify the cell-9 signed-pair guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell9_signed_pair_guard_factorization_exclusion"
)
PRIME = 2130706433
SCOUT_FILE = "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
SCOUT_HASH = "13a82e809774880ccaf2b89d5dd62cbb4995533ecde59619db2ac65443bee172"
FILES = {
    "kernel_result": ("rate_half_kb_positive_433_1a_cell9_kernel_reduction_result.json", "3a06040aadb45fc0a851f2336aaeaafecd21f08b48ea0fff4a135241ee2413b8"),
    "kernel_script": ("rate_half_kb_positive_433_1a_cell9_kernel_reduction_modal.py", "ab41d6ebb6485c63df6fc817150db4235ebec5cf51802481f73f07babd40ef45"),
    "plane_result": ("rate_half_kb_positive_433_1a_cell9_plane_kernel_flint_result.json", "11046e1f341617b21d39c045021ddb3ee682b6733c06a78d4b709a6414625d63"),
    "plane_script": ("rate_half_kb_positive_433_1a_cell9_plane_kernel_flint_modal.py", "ac7a19d218b9fed0c73e5b1e8d3aebbc838f23273d6defdcee6ff0da6af359a1"),
    "main_result": ("rate_half_kb_positive_433_1a_cell9_signed_pair_guard_factorization_result.json", "f899bd41a8bbdb394a6af4b8288abbf737c5e2825e86dff5fb8dee2c2334759b"),
    "main_script": ("rate_half_kb_positive_433_1a_cell9_signed_pair_guard_factorization_modal.py", "5900ee01b93451629e25712bf53ea953be3f21f077f77e3e54b99901ea9372da"),
    "scale_result": ("rate_half_kb_positive_433_1a_cell9_exceptional_scale_factor_result.json", "1b043263a418b23e4ae98b8b0a18f929de08a8ee3aabb178fe5db8047480c6b8"),
    "scale_script": ("rate_half_kb_positive_433_1a_cell9_exceptional_scale_factor_modal.py", "5275d0d80ab36fabbe87c44ad5eec29bda7754e8e80efb04639dd3c69117bb04"),
    "charts_result": ("rate_half_kb_positive_433_1a_cell9_exceptional_common_charts_result.json", "7c6e5fdf9fb037ab1a37be8bf180fa93a84c1d7c0f4b79275329e4d4114d0a2b"),
    "charts_script": ("rate_half_kb_positive_433_1a_cell9_exceptional_common_charts_modal.py", "3d80cae804ee8a2f5b2991d09d151cced38654e0d17fdcf6b70490d34eaadc82"),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell9-kernel-reduction-v1",
            "kernel schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["cell"] == 9 and result["basis_size"] == 11,
            "kernel completion")
    require(result["common_gcd_shape"] == {"degree": 2, "terms": 2},
            "kernel gcd")
    require(result["reduced_sha256"] == {
        "a00": "39b19a744fd99088858a8e62213ccfb72844237ceddf2b56cd8a13ded104c73f",
        "a01": "3ce6e7f8e12f11df179032a1da048c90b4044f93bf1b997b22233237f4d2f52d",
        "a02": "dc1d02481dc23bb03a4dfd5054dbbd7ba52364f4ce08d0e8e00561bdde2dc411",
        "a20": "f097ddb89d5573c36cbf140c85f35da1ce7cd7c94dbb80e572f5b29c2850b30a",
        "a21": "223685432bb8d209e01a555f66023f12d1cc90fe7ee48b5d15e40cd522475cd6",
        "a22": "38f18d42d6ccf25885a9d19b6a551bcf56828eeae3c9fc2bd95e1b6f4bd34938",
        "b10": "86ba85d32afd79c73261b22ea358c2b07260d0ac1e90d055cdf40e87792f12ec",
        "b11": "1473067932d607b1849046ee126739d399998b4ba1c58e0532f5410a86bab2ab",
    }, "kernel reductions")


def verify_plane(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell9-plane-kernel-flint-v1",
            "plane schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_kernel_sha256"] == FILES["kernel_result"][1] and
            result["source_scout_sha256"] == SCOUT_HASH,
            "plane custody")
    require(result["basis_indices"] == {
        "plane": 0, "r_linear": 1, "c_linear": 6,
    } and result["kernel_degree_bounds"] == {"c": 1, "r": 4},
            "plane basis")
    require(result["plane_shape"] == {
        "degrees": [4, 8], "terms": 45, "total_degree": 12,
    } and result["plane_leading_shape"] == {
        "degrees": [0, 8], "terms": 9, "total_degree": 8,
    } and result["pseudo_scale_power"] == 9 and
            result["b1_opposite"] is True, "plane normalization")
    require(all(row["degrees"] == [3, 17] and row["terms"] == 72
                for row in result["normalized_coefficients"].values()),
            "normalized coefficient shapes")


def verify_main(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell9-signed-pair-guard-factorization-v1",
            "main schema")
    require(payload["source_plane_sha256"] == FILES["plane_result"][1],
            "main custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            (result["product_steps"], result["square_steps"],
             result["projected_steps"]) == (3, 9, 15),
            "main completion")
    require(result["raw_resultant_shape"] == {
        "degrees": [0, 16, 18, 482], "terms": 146243,
        "total_degree": 515,
    }, "raw resultant")
    require(result["projected_shape"] == {
        "degrees": [0, 16, 3, 587], "terms": 36876,
        "total_degree": 604,
    } and result["projected_sha256"] ==
            "6ea852026b7c2e5b9ddcccac85cc676a243a45943f0b149ca797f64e2590350f",
            "projected resultant")
    require(result["guard_identity"] ==
            "plane-reduced(N0*D0^5*(w0+1)*(w0-t^2)^2*(rd^2*w0-rn^2)) is proportional to pair resultant",
            "guard identity")
    require(result["candidate_shape"] == {
        "degrees": [0, 16, 3, 271], "terms": 17156,
        "total_degree": 288,
    } and result["candidate_sha256"] ==
            "af487e351003eeffeac974a18d9ed20595be241d7e871ba7b6943d95299ba503" and
            len(result["guard_reductions"]) == 7 and
            [row["steps"] for row in result["guard_reductions"]] == [3]*7 and
            result["guard_plane_leading_exponent"] == 21,
            "guard candidate")
    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3 and
            cross["projected_leading_sha256"] ==
            "f2236a38d4dcf055b0a9e5a30110d792ebf4d9caa8c8591c2f5f1bcc2da48500" and
            cross["candidate_leading_sha256"] ==
            "1dc0905e3a9659034053cb47898fa854100d737a49cda0043a5dd8ec18bf5221",
            "cross identity")
    norm = result["projected_leading_norm"]
    require(norm["content"] == 1337229458 and norm["shape"] == {
        "degrees": [0, 0, 0, 2344], "terms": 2153,
        "total_degree": 2344,
    } and norm["sha256"] ==
            "dd2f9190a07b0d6e2296b2fe3b19d369851661e66efc5435b8bdb9ffb188837c",
            "leading norm")
    require([row["shape"]["degrees"][3] for row in norm["factors"]] ==
            [1, 2, 2, 3, 3, 1, 3, 1, 1, 1], "norm factors")
    roots = [0, 1, 16711679, 2113994754, 2130706432]
    atlas = result["leading_exception_atlas"]
    require(atlas["base_field_norm_roots"] == roots and
            atlas["all_deployed_roots_guarded"] is False,
            "leading atlas")
    rows = {row["t"]: row for row in atlas["rows"]}
    require(set(rows) == set(roots), "atlas rows")
    unguarded = []
    for t_value, row in rows.items():
        for b_row in row["b_rows"]:
            require(b_row["zero_projected_polynomial"] is True,
                    "atlas projected zero")
            if not b_row["all_deployed_roots_guarded"]:
                unguarded.append((t_value, b_row["b"], b_row["common_guards"]))
    require(unguarded == [
        (PRIME-1, 16711679, []), (PRIME-1, 2113994754, []),
    ], "scale-only atlas exceptions")


def verify_scales(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell9-exceptional-scale-factor-v1",
            "scale schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_plane_sha256"] == FILES["plane_result"][1],
            "scale completion")
    require([row["name"] for row in result["rows"]] == [
        "r_denominator", "c_denominator", "denominator_scale",
        "common_projective_scale", "plane_leading_coefficient",
        "projected_common_scale",
    ], "scale names")
    require([row["t"] for row in result["linear_roots"]] ==
            [0, 1, 16711679, 2113994754, 2130706432], "scale roots")
    require(all(factor["degrees"] in ([0, 1], [0, 3])
                for row in result["rows"] for factor in row["factorization"]),
            "scale factors")


def verify_charts(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell9-exceptional-common-charts-v1",
            "charts schema")
    require(payload["source_factor_sha256"] == FILES["scale_result"][1],
            "charts custody")
    roots = [0, 1, 16711679, 2113994754, 2130706432]
    require([row["t"] for row in payload["rows"]] == roots, "chart roots")
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["unit"] is True and
                row["guard_trivial"] is True and "UNIT=1" in row["stdout"],
                "unit scale chart")


def verify_payloads(kernel, plane, main, scales, charts):
    verify_kernel(kernel)
    verify_plane(plane)
    verify_main(main)
    verify_scales(scales)
    verify_charts(charts)


def main():
    require(hashlib.sha256((EXPERIMENTS / SCOUT_FILE).read_bytes()).hexdigest()
            == SCOUT_HASH, "scout custody")
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    keys = ("kernel_result", "plane_result", "main_result", "scale_result",
            "charts_result")
    verify_payloads(*[
        json.loads((EXPERIMENTS / FILES[key][0]).read_text()) for key in keys
    ])
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "orbit `[9,10]` is PROVED excluded" in statement,
            "statement status")
    require("either Prize result" in contract and
            "positive common-orbit frontier is empty" in contract,
            "contract fences")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-9 signed-pair guard factorization verified")


if __name__ == "__main__":
    main()
