#!/usr/bin/env python3
"""Verify the cell-12 signed-pair guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell12_signed_pair_guard_factorization_exclusion"
)
PRIME = 2130706433
SCOUT_FILE = "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
SCOUT_HASH = "13a82e809774880ccaf2b89d5dd62cbb4995533ecde59619db2ac65443bee172"
FILES = {
    "kernel_result": ("rate_half_kb_positive_433_1a_cell12_kernel_reduction_result.json", "3666340765f9dad9d3eb0518e543205d0d2d339abc19117e57e346e164415aef"),
    "kernel_script": ("rate_half_kb_positive_433_1a_cell12_kernel_reduction_modal.py", "e89d803a3525d8b186e92bee98b565c87d6bca376f7fe00f7e8266c6d85b56dc"),
    "plane_result": ("rate_half_kb_positive_433_1a_cell12_plane_kernel_flint_result.json", "87777384ffbe0460d4fa9663f55e8589c229c9d64ce785e25ccbb8fb8ef11b78"),
    "plane_script": ("rate_half_kb_positive_433_1a_cell12_plane_kernel_flint_modal.py", "dd32a76d613b9447c492558b41e38866b4822de0bb586f421762caaaeea15bfe"),
    "main_result": ("rate_half_kb_positive_433_1a_cell12_signed_pair_guard_factorization_result.json", "fc61880b1462555ebd3a1f938d67202e3f11b4d4765f68eaf4c293ed224084b9"),
    "main_script": ("rate_half_kb_positive_433_1a_cell12_signed_pair_guard_factorization_modal.py", "3b06661c12a4a4eb406f91b2914f3d8f112b1523dcde23b6977e648f26119b1b"),
    "scale_result": ("rate_half_kb_positive_433_1a_cell12_exceptional_scale_factor_result.json", "5f78ea3741ba8ec4ca6e484196293313ed37c73e6de50598c37d341dec545e3f"),
    "scale_script": ("rate_half_kb_positive_433_1a_cell12_exceptional_scale_factor_modal.py", "0577fa3397be31b0fbe35d6fb1d88e6aa09cb00aa20de4a64a04120d2dd6de03"),
    "charts_result": ("rate_half_kb_positive_433_1a_cell12_exceptional_common_charts_result.json", "8a69f8415e358c240cfcbbd7650676922988360ddae1b2b04f768ca3774bd2e1"),
    "charts_script": ("rate_half_kb_positive_433_1a_cell12_exceptional_common_charts_modal.py", "2ffc7b636aabee5e3672943511545d1a601ffbdfd82d9051b4a22d7740feb538"),
    "exception_result": ("rate_half_kb_positive_433_1a_cell12_exceptional_signed_pair_result.json", "f345fd24f879010d23ef0e311671d929d601c31c973f621751e188b5cab5f2d4"),
    "exception_script": ("rate_half_kb_positive_433_1a_cell12_exceptional_signed_pair_modal.py", "25224b31842d291a756a25a5a3c139b82d75731e0cc84f282f8f15733596b695"),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-kernel-reduction-v1",
            "kernel schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["cell"] == 12 and result["epsilon"] == [-1, -1],
            "kernel completion")
    require(result["basis_size"] == 9 and len(result["basis_sha256"]) == 9,
            "kernel basis")
    require(result["common_gcd_shape"] == {"degree": 2, "terms": 2},
            "kernel gcd")
    require(result["reduced_sha256"] == {
        "a00": "836a3834c0973bc19f41c50c4b27f6fdce02ba4ebe122eba3fdf67d3fa374cc6",
        "a01": "74ceb91d9fb328fcf87d8cea9a889c876920962c701f455226fd254e4dbf06bd",
        "a02": "5a23a5c06dbe0321ca7f17f4e546295d36ec28d8550c96caa43df5bf4a0648ed",
        "a20": "e4a7940eb6a9519f5aa01896cd1f8c86dc8d16e87a5b71e6b565c3bd9fdb7630",
        "a21": "e2d0f386bbd222bd1cc20cc5643e2256ada339f43d31c44cd57f33dc4632cd79",
        "a22": "c0e28c5ed9496961fe7766f8bf000ef00d3c66ab6b23d1f97be110f3e6a394c3",
        "b10": "1a74a695a228fbf6dc9d4377e57bcaf80cfa0c4d459dc232b8570b9c473b6bb6",
        "b11": "1447fcbbaccfff57172ae95c7a690b40cbfbc3a521b1df9fd8ff7ca55512b4df",
    }, "kernel reductions")


def verify_plane(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-plane-kernel-flint-v1",
            "plane schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_kernel_sha256"] == FILES["kernel_result"][1] and
            result["source_scout_sha256"] == SCOUT_HASH,
            "plane completion and custody")
    require(result["basis_indices"] == {
        "plane": 0, "r_linear": 1, "c_linear": 5,
    } and result["kernel_degree_bounds"] == {"c": 3, "r": 6},
            "plane basis")
    require(result["plane_shape"] == {
        "degrees": [4, 8], "terms": 17, "total_degree": 10,
    } and result["plane_leading_shape"] == {
        "degrees": [0, 4], "terms": 1, "total_degree": 4,
    }, "plane shape")
    require(result["pseudo_scale_power"] == 16 and
            result["b1_opposite"] is True and
            all(row["degrees"][0] <= 3
                for row in result["normalized_coefficients"].values()),
            "plane normalization")


def verify_main(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-signed-pair-guard-factorization-v1",
            "main schema")
    require(payload["source_plane_sha256"] == FILES["plane_result"][1],
            "main custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "main completion")
    require((result["product_steps"], result["square_steps"],
             result["projected_steps"]) == (3, 9, 15),
            "pair reductions")
    require(result["raw_resultant_shape"] == {
        "degrees": [0, 16, 18, 592], "terms": 153761,
        "total_degree": 619,
    }, "raw resultant")
    require(result["projected_shape"] == {
        "degrees": [0, 16, 3, 672], "terms": 36236,
        "total_degree": 689,
    } and result["projected_sha256"] ==
            "9f7babadf7e691f7589bd8f8123208534bf21d9aa8ea6338dbb47d7188ea7607",
            "projected resultant")
    require(result["guard_identity"] ==
            "plane-reduced(N0*D0^5*(w0+1)*(rd^2*w0-rn^2)*(rd^2*w0+rn^2)^2) is proportional to pair resultant",
            "guard identity")
    require(result["candidate_shape"] == {
        "degrees": [0, 16, 3, 346], "terms": 14204,
        "total_degree": 363,
    } and result["candidate_sha256"] ==
            "bf5a24cd372d77f3eb929ca09b694819e03224f3f45a56f3cbac7ec2716e72ba",
            "candidate")
    require([row["steps"] for row in result["guard_reductions"]] == [3]*10 and
            result["guard_plane_leading_exponent"] == 30,
            "candidate reductions")
    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3 and
            cross["projected_leading_sha256"] ==
            "1253329c6db88f95fb6dadd7a3a757965e8caa0b5b77d0c9e039fd01791047bc" and
            cross["candidate_leading_sha256"] ==
            "91f9a676691c2dd39c3ef9c1a7df04970fb2acfa37520214417ae28c03655f9f",
            "cross identity")
    norm = result["projected_leading_norm"]
    require(norm["content"] == 1486959812 and norm["shape"] == {
        "degrees": [0, 0, 0, 2432], "terms": 1621,
        "total_degree": 2432,
    } and norm["sha256"] ==
            "321f38bc4059cfe29fd72a8b18f9a90d0e6840ab0f91486bc5ef4574e6a53dda",
            "leading norm")
    require([row["shape"]["degrees"][3] for row in norm["factors"]] ==
            [1, 10, 1, 1, 3, 3, 1, 1, 3, 1, 1, 1],
            "norm factor degrees")
    for row in norm["factors"]:
        require(hashlib.sha256(row["text"].encode()).hexdigest() ==
                row["sha256"], "norm factor hash")

    atlas = result["leading_exception_atlas"]
    roots = [0, 1, 16711679, 1117681606, 1419755025, 1992261782,
             2113994754, 2130706432]
    require(atlas["base_field_norm_roots"] == roots and
            atlas["all_deployed_roots_guarded"] is False,
            "main exception atlas")
    rows = {row["t"]: row for row in atlas["rows"]}
    require(set(rows) == set(roots), "main exception roots")
    allowed = {"N0", "D0", "w0+1", "w0-r^2", "w0+r^2"}
    displayed = 0
    for t_value in (1419755025, 1992261782):
        require(len(rows[t_value]["b_rows"]) == 2,
                f"main proper lifts {t_value}")
        for b_row in rows[t_value]["b_rows"]:
            require(b_row["all_deployed_roots_guarded"] is True and
                    b_row["zero_projected_polynomial"] is False,
                    "main proper row")
            for root in b_row["deployed_w0_roots"]:
                require(root["guards"] and set(root["guards"]) <= allowed,
                        "main proper guard")
                displayed += 1
    require(displayed == 20, "main displayed roots")


def verify_scales(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-exceptional-scale-factor-v1",
            "scale schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_plane_sha256"] == FILES["plane_result"][1],
            "scale completion")
    roots = [0, 1, 16711679, 1117681606, 2113994754, 2130706432]
    require([row["t"] for row in result["linear_roots"]] == roots,
            "scale roots")
    require(all(factor["degrees"] in ([0, 1], [0, 3])
                for row in result["rows"] for factor in row["factorization"]),
            "scale factors")


def verify_charts(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-exceptional-common-charts-v1",
            "charts schema")
    require(payload["source_factor_sha256"] == FILES["scale_result"][1],
            "charts custody")
    rows = {row["t"]: row for row in payload["rows"]}
    require(set(rows) == {0, 1, 16711679, 1117681606,
                          2113994754, 2130706432}, "chart roots")
    for t_value in (0, 1, 16711679, 2113994754, 2130706432):
        require(rows[t_value]["status"] == "COMPLETE" and
                rows[t_value]["unit"] is True and
                rows[t_value]["guard_trivial"] is True,
                f"guard chart {t_value}")
    proper = rows[1117681606]
    require(proper["status"] == "COMPLETE" and proper["unit"] is False and
            proper["guard_trivial"] is False and
            "G[4]=b2-9674473b+1" in proper["stdout"],
            "proper common chart")


def verify_exception(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell12-exceptional-signed-pair-v1",
            "exception schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["t"] == 1117681606 and
            result["source_charts_sha256"] == FILES["charts_result"][1],
            "exception completion and custody")
    require(result["b_polynomial"] == "x^2 + 2121031960*x + 1" and
            result["b_roots"] == [816507220, 1323873686] and
            result["all_deployed_roots_guarded"] is True,
            "exceptional points")
    allowed = {"N0", "D0", "w0+1", "w0-r^2", "w0+r^2",
               "w0-t^2", "w0+t^2"}
    require(len(result["rows"]) == 2, "exception rows")
    for row in result["rows"]:
        require(row["resultant_shape"] == {
            "degrees": [0, 16], "terms": 17, "total_degree": 16,
        } and row["all_deployed_roots_guarded"] is True and
                (row["kernel"]["b1"][0] + row["kernel"]["b1"][1]) % PRIME == 0,
                "exception raw resultant")
        require(sum(factor["degree"] * factor["multiplicity"]
                    for factor in row["factors"]) == 16,
                "exception factor degree")
        for factor in row["factors"]:
            if factor["degree"] == 1:
                require(factor["owners"] and set(factor["owners"]) <= allowed,
                        "exception deployed guard")


def verify_payloads(kernel, plane, main, scales, charts, exception):
    verify_kernel(kernel)
    verify_plane(plane)
    verify_main(main)
    verify_scales(scales)
    verify_charts(charts)
    verify_exception(exception)


def main():
    require(hashlib.sha256((EXPERIMENTS / SCOUT_FILE).read_bytes()).hexdigest()
            == SCOUT_HASH, "scout custody")
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    keys = ("kernel_result", "plane_result", "main_result", "scale_result",
            "charts_result", "exception_result")
    payloads = [
        json.loads((EXPERIMENTS / FILES[key][0]).read_text()) for key in keys
    ]
    verify_payloads(*payloads)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "orbit `[12,13]` is PROVED excluded" in statement,
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
    print("positive 433-1a cell-12 signed-pair guard factorization verified")


if __name__ == "__main__":
    main()
