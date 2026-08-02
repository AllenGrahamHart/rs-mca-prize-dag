#!/usr/bin/env python3
"""Verify the cell-14 signed-pair guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell14_signed_pair_guard_factorization_exclusion"
)
PRIME = 2130706433
SCOUT_FILE = "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
SCOUT_HASH = "13a82e809774880ccaf2b89d5dd62cbb4995533ecde59619db2ac65443bee172"
FILES = {
    "kernel_result": (
        "rate_half_kb_positive_433_1a_cell14_kernel_reduction_result.json",
        "fe7e4207c91a1a43164a0271a838c1556e2887c285014f2bbb3df08149278927",
    ),
    "kernel_script": (
        "rate_half_kb_positive_433_1a_cell14_kernel_reduction_modal.py",
        "77923aaa577ef3aea7c9606b4a289744152d6da1fd930760868b0a2c076cb935",
    ),
    "plane_result": (
        "rate_half_kb_positive_433_1a_cell14_plane_kernel_flint_result.json",
        "471e81d1b3870c73719a08cc922139d9572658a73abbe85e2022abc72cc2d820",
    ),
    "plane_script": (
        "rate_half_kb_positive_433_1a_cell14_plane_kernel_flint_modal.py",
        "be32b19fea0fac45deddc7574ecefdaf97047ba960f097da22882a03d6cbee5d",
    ),
    "main_result": (
        "rate_half_kb_positive_433_1a_cell14_signed_pair_guard_factorization_result.json",
        "e3ff4a2acd58a42e299791962ae0d5f53849bc8a36efb852526bc937db7fc70f",
    ),
    "main_script": (
        "rate_half_kb_positive_433_1a_cell14_signed_pair_guard_factorization_modal.py",
        "b2611252e09676563f8db930ef5efc90fd9e532c6ecee0b04a694bd953b86524",
    ),
    "scale_result": (
        "rate_half_kb_positive_433_1a_cell14_exceptional_scale_factor_result.json",
        "1bdb31ed7b90d8456eb6e080f28f8405a6104a0b007d6716d2a510314e6b7638",
    ),
    "scale_script": (
        "rate_half_kb_positive_433_1a_cell14_exceptional_scale_factor_modal.py",
        "e7953b4f226f52b4d1c1cf187e2d8196fbf8e35f3821256b5b22457264560af0",
    ),
    "charts_result": (
        "rate_half_kb_positive_433_1a_cell14_exceptional_common_charts_result.json",
        "8abba49320fc235014efb08da4c4401f5f385942e4318cdcf41fa63b055aecf4",
    ),
    "charts_script": (
        "rate_half_kb_positive_433_1a_cell14_exceptional_common_charts_modal.py",
        "fe8b6214661424bdabac23d27a7b120b621dba89e23c68204f38ae256f463b96",
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell14-kernel-reduction-v1",
            "kernel schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["cell"] == 14 and result["epsilon"] == [-1, -1],
            "kernel completion")
    require(result["basis_size"] == 8 and len(result["basis_sha256"]) == 8,
            "lex basis")
    require(result["common_gcd_shape"] == {"degree": 2, "terms": 1},
            "common kernel gcd")
    expected = {
        "a00": "ff8457c9b982b22ec73218da1b70dde9202ec0360b6e3bd174b1fc5d5e22f1c7",
        "a01": "a1f725ca3e626d156f3a2ed722a9bc4f9e2425ae4934abee9d2416dff594a1d9",
        "a02": "a537b3500fd82e4569ef12188582081c071982107c15bb52ad31b9680c68881f",
        "a20": "a764b09b5345bc41f14bbb5e27242ad07323308448d4430bf5d3decf5f6eea3f",
        "a21": "f7833119afbc2f916679e34ffca23828ebcb03b6a96e7d62a600867e3b537cb2",
        "a22": "e681fe57b1966990da1ec7f0a78fa042937d2ed13b6230142e42054540c4289c",
        "b10": "bef367c0da4a529c1e7863df0537acb5751920d272747c9b60ed6907c7187f7e",
        "b11": "6b551cb69e0e67f2944777a55df85c17301516a697205c08d2c878b526d3c4ce",
    }
    require(result["reduced_sha256"] == expected, "kernel reductions")


def verify_plane(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell14-plane-kernel-flint-v1",
            "plane schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_kernel_sha256"] == FILES["kernel_result"][1],
            "plane completion and custody")
    require(result["source_scout_sha256"] == SCOUT_HASH,
            "plane scout custody")
    require(result["basis_indices"] == {
        "plane": 0, "r_linear": 1, "c_linear": 5,
    }, "plane basis indices")
    require(result["plane_shape"] == {
        "degrees": [4, 8], "terms": 17, "total_degree": 10,
    } and result["plane_leading_shape"] == {
        "degrees": [0, 4], "terms": 1, "total_degree": 4,
    }, "plane shape")
    require(result["kernel_degree_bounds"] == {"c": 3, "r": 7} and
            result["pseudo_scale_power"] == 19 and
            result["b1_opposite"] is True, "normalized kernel")
    require(set(result["normalized_coefficients"]) == {
        "a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11",
    }, "normalized coefficients")
    require(all(row["degrees"][0] <= 3
                for row in result["normalized_coefficients"].values()),
            "normalized b degree")


def verify_main(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell14-signed-pair-guard-factorization-v1",
            "main schema")
    require(payload["source_plane_sha256"] == FILES["plane_result"][1],
            "main input custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "main completion")
    require((result["product_steps"], result["square_steps"],
             result["projected_steps"]) == (3, 9, 15),
            "pair reductions")
    require(result["raw_resultant_shape"] == {
        "degrees": [0, 16, 18, 672], "terms": 179183,
        "total_degree": 699,
    }, "raw resultant")
    require(result["projected_shape"] == {
        "degrees": [0, 16, 3, 752], "terms": 41556,
        "total_degree": 769,
    } and result["projected_sha256"] ==
            "de1a788615f9276da20452488cd6e044baf510383626e4bc881ffe04a68a62e9",
            "projected resultant")
    require(result["guard_identity"] ==
            "plane-reduced(N0*D0^5*(w0+1)^2*(rd^2*w0-rn^2)*(rd^2*w0+rn^2)) is proportional to pair resultant",
            "guard identity")
    require(result["candidate_shape"] == {
        "degrees": [0, 16, 3, 340], "terms": 15580,
        "total_degree": 357,
    } and result["candidate_sha256"] ==
            "d57c96aeceeb5a079e4702b47198798e0430c201d269b537e7a9d8b9e250afc9",
            "guard candidate")
    require([row["operation"] for row in result["guard_reductions"]] == [
        "d0_power_2", "d0_power_3", "d0_power_4", "d0_power_5",
        "r_minus", "r_plus", "n0_times_d0_fifth",
        "times_minus_labels", "times_plus_label",
    ] and [row["steps"] for row in result["guard_reductions"]] == [3]*9 and
            result["guard_plane_leading_exponent"] == 27,
            "guard reductions")
    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3, "cross identity")
    require(cross["projected_leading_sha256"] ==
            "c7b31855504c1415f8ba0f6b68501623e6cce939eed5e3e404cfe920c30e26cb" and
            cross["candidate_leading_sha256"] ==
            "4f985cf861d27b3472abf198f9b0a61539ba2d1131755e82c37de63d8749fab2",
            "leading hashes")

    norm = result["projected_leading_norm"]
    require(norm["content"] == 1060626869 and norm["shape"] == {
        "degrees": [0, 0, 0, 2752], "terms": 1929,
        "total_degree": 2752,
    } and norm["sha256"] ==
            "782f279a9924b674f4b0acfa8383dd153a7baa7de93528e85677a160215786f6",
            "leading norm")
    expected_factors = [
        (824, "t"),
        (6, "t^6 + 1985681298*t^5 + 1782735033*t^4 + 1797954162*t^3 + 736638391*t^2 + 1268793801*t + 1919789891"),
        (6, "t + 388154718"),
        (6, "t^5 + 1854153492*t^4 + 1806281358*t^3 + 462355765*t^2 + 74456104*t + 510186908"),
        (22, "t + 2097506614"), (22, "t + 2063636178"),
        (24, "t^3 + 2097283076*t^2 + 33423359*t + 1"),
        (24, "t^3 + 2097283074*t^2 + 2097283076*t + 2130706432"),
        (80, "t + 2130706432"), (80, "t + 1"),
        (144, "t^3 + 1340459003*t^2 + 2122238823*t + 16711679"),
        (144, "t^3 + 756824072*t^2 + 8467608*t + 16711679"),
        (160, "t + 16711679"), (484, "t + 2113994754"),
    ]
    require([(row["multiplicity"], row["text"])
             for row in norm["factors"]] == expected_factors,
            "norm factorization")
    for row in norm["factors"]:
        require(hashlib.sha256(row["text"].encode()).hexdigest() ==
                row["sha256"], "norm factor hash")

    atlas = result["leading_exception_atlas"]
    roots = [0, 1, 16711679, 33199819, 67070255, 1742551715,
             2113994754, 2130706432]
    require(atlas["base_field_norm_roots"] == roots and
            atlas["all_deployed_roots_guarded"] is True,
            "leading atlas")
    rows = {row["t"]: row for row in atlas["rows"]}
    require(set(rows) == set(roots), "leading rows")
    expected_guard_lifts = {
        0: (0, "b"), 1: (1, "b-1"),
        16711679: (PRIME-1, "b+1"),
        33199819: (PRIME-1, "b+1"),
        67070255: (PRIME-1, "b+1"),
        2113994754: (PRIME-1, "b+1"),
        2130706432: (1, "b-1"),
    }
    for t_value, (b_value, guard) in expected_guard_lifts.items():
        row = rows[t_value]
        require(row["deployed_b_roots"] == [b_value] and
                row["b_rows"] == [{
                    "b": b_value,
                    "zero_projected_polynomial": True,
                    "common_guards": [guard],
                    "all_deployed_roots_guarded": True,
                }], f"guard lift {t_value}")
    proper = rows[1742551715]
    require(proper["deployed_b_roots"] == [848523624, 1980548607] and
            len(proper["b_rows"]) == 2, "proper leading fiber")
    allowed = {"N0", "D0", "w0+1", "w0-r^2", "w0+r^2"}
    displayed = 0
    for row in proper["b_rows"]:
        require(row["all_deployed_roots_guarded"] is True and
                row["zero_projected_polynomial"] is False and
                row["nonlinear_factors"] in (
                    [{"degree": 2, "multiplicity": 1}],
                    [{"degree": 2, "multiplicity": 5}],
                ), "proper factor profile")
        for root in row["deployed_w0_roots"]:
            require(root["guards"] and set(root["guards"]) <= allowed,
                    "proper root guard")
            displayed += 1
    require(displayed == 8, "proper deployed root count")


def verify_scales(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell14-exceptional-scale-factor-v1",
            "scale schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME and
            result["source_plane_sha256"] == FILES["plane_result"][1],
            "scale completion and custody")
    roots = [0, 1, 16711679, 2113994754, 2130706432]
    require([row["t"] for row in result["linear_roots"]] == roots,
            "scale roots")
    require({row["name"] for row in result["rows"]} == {
        "r_denominator", "c_denominator", "denominator_scale",
        "common_projective_scale", "plane_leading_coefficient",
        "projected_common_scale",
    }, "scale names")
    require(all(factor["degrees"] in ([0, 1], [0, 3])
                for row in result["rows"] for factor in row["factorization"]),
            "scale factor degrees")
    require(sum(factor["degrees"] == [0, 3]
                for row in result["rows"]
                for factor in row["factorization"]) == 4,
            "recorded irreducible cubic occurrences")


def verify_charts(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell14-exceptional-common-charts-v1",
            "chart schema")
    require(payload["source_factor_sha256"] == FILES["scale_result"][1],
            "chart input custody")
    require([row["t"] for row in payload["rows"]] ==
            [0, 1, 16711679, 2113994754, 2130706432],
            "chart roots")
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["unit"] is True and
                row["guard_trivial"] is True and
                "UNIT=1" in row["stdout"], "exceptional common chart")


def verify_payloads(kernel, plane, main, scales, charts):
    verify_kernel(kernel)
    verify_plane(plane)
    verify_main(main)
    verify_scales(scales)
    verify_charts(charts)


def main():
    require(hashlib.sha256((EXPERIMENTS / SCOUT_FILE).read_bytes()).hexdigest()
            == SCOUT_HASH, "scout file custody")
    for filename, expected in FILES.values():
        path = EXPERIMENTS / filename
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"file custody {filename}")
    payloads = {
        key: json.loads((EXPERIMENTS / FILES[key][0]).read_text())
        for key in ("kernel_result", "plane_result", "main_result",
                    "scale_result", "charts_result")
    }
    verify_payloads(payloads["kernel_result"], payloads["plane_result"],
                    payloads["main_result"], payloads["scale_result"],
                    payloads["charts_result"])

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "`[14]` is PROVED excluded" in statement,
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
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")
    print("positive 433-1a cell-14 signed-pair guard factorization verified")


if __name__ == "__main__":
    main()
