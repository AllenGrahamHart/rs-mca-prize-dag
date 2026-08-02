#!/usr/bin/env python3
"""Verify the cell-11 signed-pair guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell11_signed_pair_guard_factorization_exclusion"
)
PRIME = 2130706433
SCOUT_FILE = "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
SCOUT_HASH = "13a82e809774880ccaf2b89d5dd62cbb4995533ecde59619db2ac65443bee172"
FILES = {
    "kernel_result": ("rate_half_kb_positive_433_1a_cell11_kernel_reduction_result.json", "908c1bf36e3ad71e0ef442398b68e71193bd52c6b71bf346b53ab6481b3e7205"),
    "kernel_script": ("rate_half_kb_positive_433_1a_cell11_kernel_reduction_modal.py", "3b4e828ebb7a8d8a3190bf7329ef339c0ff23b6cc3523205108d44846ec5fff1"),
    "plane_result": ("rate_half_kb_positive_433_1a_cell11_plane_kernel_flint_result.json", "f705f1e29c151df6956cbb43b4c045425ad7b50678ecd01ed0c06bb3ba062bb4"),
    "plane_script": ("rate_half_kb_positive_433_1a_cell11_plane_kernel_flint_modal.py", "3e6a14f36496d780dfbf94b1a7b994dff647937251aa803c58e42f824594f1ce"),
    "main_result": ("rate_half_kb_positive_433_1a_cell11_signed_pair_guard_factorization_result.json", "52511345706c352233de5a50f0695c45e95e9564b2f512a419d76ec503093edf"),
    "main_script": ("rate_half_kb_positive_433_1a_cell11_signed_pair_guard_factorization_modal.py", "875294d6d3d535a4e20a4ee68d255e5fcb7166ee51297f0f1f81c035177fdcf1"),
    "scale_result": ("rate_half_kb_positive_433_1a_cell11_exceptional_scale_factor_result.json", "228ffcf9ffa7937e4524691c44df54f8eaf7ad018e35d47438101470ff05cc57"),
    "scale_script": ("rate_half_kb_positive_433_1a_cell11_exceptional_scale_factor_modal.py", "bc56179bdd841a890dbfddf834222e50d6b3917ffb9d0ca7be219150a56cdadd"),
    "charts_result": ("rate_half_kb_positive_433_1a_cell11_exceptional_common_charts_result.json", "d5d90ee919b3c1c25b12f2ac0845730d070fb049f32931aaac3b10c1a02fe2be"),
    "charts_script": ("rate_half_kb_positive_433_1a_cell11_exceptional_common_charts_modal.py", "3be8d620feddbecf778cc7ada65d4251d08d5290a29d187f50296acb18519d0d"),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell11-kernel-reduction-v1",
            "kernel schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["cell"] == 11 and result["basis_size"] == 10,
            "kernel completion")
    require(result["common_gcd_shape"] == {"degree": 2, "terms": 1},
            "kernel gcd")
    require(result["reduced_sha256"] == {
        "a00": "da4555983890e4812a10589b7c1c5d43367c437a6a3228ee2a0e7551737ba43a",
        "a01": "c5fcedaeef75c7a04f3baec76c160da29a72a85344c7954a36b7fb5c6dd971c2",
        "a02": "a84306cc03a06c81a96797463bdc20ae99f3ddddbdfe27eebab32fb0377c2871",
        "a20": "04cd249baecc28ece017f8df709281ff76c029cb9fdb6abd3bef78a295b3c106",
        "a21": "4b089279e12fabe45eb6880de5393344730f4d1f091e1db0e719990d90531fe0",
        "a22": "d497a3fbd332acc740b2fc0ad66620abb19f44f6f6b8629fe4e06080e37a5bfd",
        "b10": "388ef728952e847fa6839dde2d6224506afdeba9ec93999628c4032ca333defa",
        "b11": "1987efc0d7f5574f4414d939950ce9f0424a0b00054c0c36495f2af5708e542c",
    }, "kernel reductions")


def verify_plane(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell11-plane-kernel-flint-v1",
            "plane schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_kernel_sha256"] == FILES["kernel_result"][1] and
            result["source_scout_sha256"] == SCOUT_HASH,
            "plane custody")
    require(result["basis_indices"] == {
        "plane": 0, "r_linear": 1, "c_linear": 4,
    } and result["kernel_degree_bounds"] == {"c": 3, "r": 7},
            "plane basis")
    require(result["plane_shape"] == {
        "degrees": [4, 8], "terms": 45, "total_degree": 12,
    } and result["plane_leading_shape"] == {
        "degrees": [0, 8], "terms": 9, "total_degree": 8,
    } and result["pseudo_scale_power"] == 19 and
            result["b1_opposite"] is True, "plane normalization")


def verify_main(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell11-signed-pair-guard-factorization-v1",
            "main schema")
    require(payload["source_plane_sha256"] == FILES["plane_result"][1],
            "main custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            (result["product_steps"], result["square_steps"],
             result["projected_steps"]) == (3, 9, 15),
            "main completion")
    require(result["raw_resultant_shape"] == {
        "degrees": [0, 16, 18, 562], "terms": 172159,
        "total_degree": 596,
    }, "raw resultant")
    require(result["projected_shape"] == {
        "degrees": [0, 16, 3, 667], "terms": 42316,
        "total_degree": 684,
    } and result["projected_sha256"] ==
            "102c925674db13100aaff351f6a402a8189561a1a57d8b27bd93f829e4eada4d",
            "projected resultant")
    require(result["guard_identity"] ==
            "plane-reduced(N0*D0^5*(w0-t^2)^2*(rd^2*w0-rn^2)*(rd^2*w0+rn^2)) is proportional to pair resultant",
            "guard identity")
    require(result["candidate_shape"] == {
        "degrees": [0, 16, 3, 361], "terms": 23004,
        "total_degree": 378,
    } and result["candidate_sha256"] ==
            "a9f4f94993a0c394edf14985ee5c811c588089ef113976263ca79de843bd571f" and
            [row["steps"] for row in result["guard_reductions"]] == [3]*9 and
            result["guard_plane_leading_exponent"] == 27,
            "guard candidate")
    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3 and
            cross["projected_leading_sha256"] ==
            "39f78bb8dceff7da7b9817517fa6e0b44d2d48faf7a62bbd3ba2d4484d3a0f65" and
            cross["candidate_leading_sha256"] ==
            "3c32ba8c358f76bd853f36c796f7bbde6c0676a7da9d62d242c3595b9cfa6799",
            "cross identity")
    norm = result["projected_leading_norm"]
    require(norm["content"] == 1845502928 and norm["shape"] == {
        "degrees": [0, 0, 0, 2664], "terms": 2473,
        "total_degree": 2664,
    } and norm["sha256"] ==
            "8f199c673128a5ed4abb09ecae4297b79a8dfa545f5cc2c2cf7575a4683c51f2",
            "leading norm")
    require([row["shape"]["degrees"][3] for row in norm["factors"]] ==
            [1, 1, 7, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1],
            "norm factors")
    atlas = result["leading_exception_atlas"]
    roots = [0, 1, 16711679, 33199819, 67070255, 989155728,
             1231496538, 1620586492, 2113994754, 2130706432]
    require(atlas["base_field_norm_roots"] == roots and
            atlas["all_deployed_roots_guarded"] is False,
            "leading atlas")
    rows = {row["t"]: row for row in atlas["rows"]}
    for t_value in (33199819, 67070255):
        require(rows[t_value]["deployed_b_roots"] == [PRIME-1] and
                rows[t_value]["b_rows"][0]["common_guards"] == ["b+1"],
                "b+1 norm fiber")
    proper = rows[989155728]
    require(proper["deployed_b_roots"] == [47466281, 1184823458] and
            len(proper["b_rows"]) == 2, "proper norm fiber")
    allowed = {"N0", "D0", "w0-t^2", "w0-r^2", "w0+r^2"}
    displayed = 0
    for b_row in proper["b_rows"]:
        require(b_row["all_deployed_roots_guarded"] is True and
                b_row["zero_projected_polynomial"] is False,
                "proper norm lift")
        for root in b_row["deployed_w0_roots"]:
            require(root["guards"] and set(root["guards"]) <= allowed,
                    "proper norm guard")
            displayed += 1
    require(displayed == 12, "proper displayed roots")


def verify_scales(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell11-exceptional-scale-factor-v1",
            "scale schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_plane_sha256"] == FILES["plane_result"][1],
            "scale completion")
    require([row["t"] for row in result["linear_roots"]] ==
            [0, 1, 16711679, 1231496538, 1620586492,
             2113994754, 2130706432], "scale roots")
    require(all(factor["degrees"] in ([0, 1], [0, 3])
                for row in result["rows"] for factor in row["factorization"]),
            "scale factors")


def verify_charts(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell11-exceptional-common-charts-v1",
            "charts schema")
    require(payload["source_factor_sha256"] == FILES["scale_result"][1],
            "charts custody")
    roots = [0, 1, 16711679, 1231496538, 1620586492,
             2113994754, 2130706432]
    require([row["t"] for row in payload["rows"]] == roots, "chart roots")
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["unit"] is True and
                "UNIT=1" in row["stdout"], "unit scale chart")


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
            "orbit `[11]` is PROVED excluded" in statement,
            "statement status")
    require("either Prize result" in contract and "[9,10]" in contract,
            "contract nonclaim")
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
    print("positive 433-1a cell-11 signed-pair guard factorization verified")


if __name__ == "__main__":
    main()
