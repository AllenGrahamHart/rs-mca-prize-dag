#!/usr/bin/env python3
"""Verify the cell-3 signed-pair guard-factorization exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell3_signed_pair_guard_factorization_exclusion"
)
RESULT_FILE = "rate_half_kb_positive_433_1a_cell3_signed_pair_guard_factorization_result.json"
SCRIPT_FILE = "rate_half_kb_positive_433_1a_cell3_signed_pair_guard_factorization_modal.py"
RESULT_HASH = "b604908d97a7d7588392236c962f490d600479dadd0cd69eea47b318f0bb5269"
SCRIPT_HASH = "c5bd69f2cde6f8246a36b6a1da1fa01f452a9d850c4a695dfec2e0335206557c"
PLANE_HASH = "4e36308e9e5d062f9c60280057b961c8181d0edb2406831cfaae7be76c7a2a0a"
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-signed-pair-guard-factorization-v1",
            "schema")
    require(payload["source_plane_sha256"] == PLANE_HASH, "input custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "completion")
    require(result["product_steps"] == 3 and result["square_steps"] == 9 and
            result["projected_steps"] == 15, "pair plane reductions")
    require(result["raw_resultant_shape"] == {
        "degrees": [0, 16, 18, 471], "terms": 151031,
        "total_degree": 498,
    }, "raw resultant")
    require(result["projected_shape"] == {
        "degrees": [0, 16, 3, 531], "terms": 35876,
        "total_degree": 543,
    } and result["projected_sha256"] ==
            "f47a8ac08d3c9e9925596931aff6899f437ab2767955e36a46b7322aed24b387",
            "projected resultant")
    require(result["guard_identity"] ==
            "plane-reduced(N0*D0^5*(w0+1)*(w0-t^2)*(rd^2*w0-rn^2)^2) is proportional to pair resultant",
            "guard identity")
    require(result["candidate_shape"] == {
        "degrees": [0, 16, 3, 258], "terms": 17380,
        "total_degree": 270,
    } and result["candidate_sha256"] ==
            "fbc5eef8a8ab213e03c1fa2e9647a2c9c2559dbd07c52919c775c3003cf8a189",
            "guard candidate")
    reductions = result["guard_reductions"]
    require([row["operation"] for row in reductions] == [
        "d0_power_2", "d0_power_3", "d0_power_4", "d0_power_5",
        "r_guard", "r_guard_squared", "n0_times_d0_fifth",
        "times_label_guards",
    ], "guard reductions")
    require([row["steps"] for row in reductions] == [3]*8 and
            result["guard_plane_leading_exponent"] == 24,
            "guard plane scale")
    cross = result["quotient_ring_cross_identity"]
    require(cross["verified"] is True and cross["remainder_zero"] is True and
            cross["plane_steps"] == 3, "cross identity")
    require(cross["projected_leading_sha256"] ==
            "1c4e2b15ba7da420bba3c97ca45b0465ab1809b7c00b6879eb5176187c045b98" and
            cross["candidate_leading_sha256"] ==
            "7e29224eac8f68b5cc42b335d99396c75ecb604c5f40ea0248b09cd069e8d214",
            "leading hashes")

    norm = result["projected_leading_norm"]
    require(norm["content"] == 1717523883 and norm["shape"] == {
        "degrees": [0, 0, 0, 2104], "terms": 2101,
        "total_degree": 2104,
    } and norm["sha256"] ==
            "ab19f9f49cb884846de86901c0952598584d6eef35c2f135917339cee5bb641a",
            "leading norm")
    expected_factors = [
        (4, "t"), (6, "t + 1644584132"),
        (6, "t + 1877313284"),
        (6, "t^2 + 2056212964*t + 1135134686"),
        (6, "t^2 + 1931098098*t + 633384727"),
        (6, "t^2 + 1013617252*t + 1489832821"),
        (22, "t + 2097506614"), (22, "t + 2063636178"),
        (24, "t^3 + 2097283074*t^2 + 2097283076*t + 2130706432"),
        (64, "t + 1"), (84, "t + 16711679"),
        (144, "t + 842344834"),
        (144, "t^3 + 1254938237*t^2 + 861030612*t + 485824922"),
        (167, "t^3 + 2097283076*t^2 + 33423359*t + 1"),
        (271, "t + 2130706432"), (440, "t + 2113994754"),
    ]
    require([(row["multiplicity"], row["text"])
             for row in norm["factors"]] == expected_factors,
            "norm factorization")
    for row in norm["factors"]:
        require(hashlib.sha256(row["text"].encode()).hexdigest() ==
                row["sha256"], "norm factor hash")

    atlas = result["leading_exception_atlas"]
    roots = [0, 1, 16711679, 33199819, 67070255, 253393149,
             486122301, 1288361599, 2113994754, 2130706432]
    scales = [0, 1, 16711679, 1288361599, 2113994754, 2130706432]
    require(atlas["base_field_norm_roots"] == roots and
            atlas["exceptional_scale_roots"] == scales and
            atlas["all_uncovered_deployed_roots_guarded"] is True,
            "exception root census")
    rows = {row["t"]: row for row in atlas["rows"]}
    require(set(rows) == set(roots), "exception rows")
    for root in scales:
        require(rows[root]["covered_by_exceptional_scale"] is True,
                f"scale root {root}")
    for root in (33199819, 67070255):
        row = rows[root]
        require(row["deployed_b_roots"] == [PRIME-1] and
                row["b_rows"][0]["zero_projected_polynomial"] is True and
                row["b_rows"][0]["common_guards"] == ["b+1"],
                f"b+1 exception {root}")
    allowed = {"N0", "D0", "w0+1", "w0-t^2", "w0-r^2"}
    deployed = 0
    for root in (253393149, 486122301):
        row = rows[root]
        require(len(row["deployed_b_roots"]) == 2 and
                len(row["b_rows"]) == 2, f"finite b atlas {root}")
        for b_row in row["b_rows"]:
            require(b_row["all_deployed_roots_guarded"] is True and
                    b_row["zero_projected_polynomial"] is False and
                    b_row["nonlinear_factors"] == [], "finite w0 atlas")
            for w0_row in b_row["deployed_w0_roots"]:
                require(w0_row["guards"] and
                        set(w0_row["guards"]) <= allowed,
                        "finite root guard")
                deployed += 1
    require(deployed == 24, "finite deployed root count")


def main():
    result_path = EXPERIMENTS / RESULT_FILE
    script_path = EXPERIMENTS / SCRIPT_FILE
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == RESULT_HASH,
            "result hash")
    require(hashlib.sha256(script_path.read_bytes()).hexdigest() == SCRIPT_HASH,
            "script hash")
    verify_payload(json.loads(result_path.read_text()))

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "orbit `[3,6]` is PROVED excluded" in statement,
            "statement status")
    require("other four positive representatives" in contract and
            "either Prize result" in contract, "contract nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_genus3_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_exceptional_scale_chart_exclusion",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-3 signed-pair guard factorization verified")


if __name__ == "__main__":
    main()
