#!/usr/bin/env python3
"""Verify the cell-4 exceptional reconstruction colored exclusion."""

import hashlib
import json
from pathlib import Path
import re


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_exceptional_reconstruction_colored_exclusion"
)
FILES = {
    "w2": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_w2_resultant_result.json",
    "reduce": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_x_reduce_result.json",
    "frobenius": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_coefficient_frobenius_result.json",
    "atlas": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_candidate_atlas_result.json",
    "content": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_colored_content_fiber_replay_result.json",
    "scales": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_subresultant_scale_atlas_result.json",
}
HASHES = {
    "w2": "f0fa41452c7025ea45b9940c0cd7ff5ee8900ecd32dd5f3d9ee6a0d5506ae1bb",
    "reduce": "2afa6e219da94cf26131d645d4ad1a67951c45a0436c15e4ae8abfb1e4e6ba21",
    "frobenius": "e6040fc21bed1016ad79fc910578de98f05d62bfae39a5293d455e9c6464c750",
    "atlas": "1c466992b55b3226e74352b64fcf081bb1988910c8762f20ffaf8140009fa165",
    "content": "f1c27c737dba5182611ebd8d88ea56c0905d638f17d1e04222bc8699142daa20",
    "scales": "66390180133d29db539e9b48a9d87ae4bab227534e7dea4fafa8e9d05f3b9bdc",
}
PRIME = 2130706433
I = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_polynomial(row, canonical_key):
    path = EXPERIMENTS / row["polynomial_file"]
    require(hashlib.sha256(path.read_bytes()).hexdigest() ==
            row["polynomial_file_sha256"], "polynomial file hash")
    require(hashlib.sha256(path.read_text().strip().encode()).hexdigest() ==
            row[canonical_key], "polynomial canonical hash")


def root_from_factor(text):
    compact = text.replace(" ", "")
    if compact == "x":
        return 0
    match = re.fullmatch(r"x\+(\d+)", compact)
    require(match is not None, f"linear factor syntax {text!r}")
    return (-int(match.group(1))) % PRIME


def verify_payloads(payloads):
    w2_payload = payloads["w2"]
    require(w2_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-x-w2-resultant-v1",
            "w2 schema")
    w2 = w2_payload["result"]
    require(w2_payload["status"] == w2["status"] == "COMPLETE",
            "w2 completion")
    require(w2["resultant_shape"] == {
        "degrees": [4, 0, 8, 8, 18, 439],
        "terms": 1275945, "total_degree": 465,
    } and w2["primitive_shape"] == {
        "degrees": [4, 0, 8, 8, 3, 300],
        "terms": 177540, "total_degree": 311,
    }, "w2 shapes")
    verify_polynomial(w2, "primitive_sha256")

    reduce_payload = payloads["reduce"]
    require(reduce_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-x-reduce-v1",
            "reduce schema")
    reduced = reduce_payload["result"]
    require(reduced["status"] == "COMPLETE" and
            reduced["h_steps"] == 22 and reduced["b_steps"] == 3,
            "reduce completion")
    require(reduced["primitive_shape"] == {
        "degrees": [4, 0, 7, 0, 2047],
        "terms": 16368, "total_degree": 2055,
    }, "x4 C shape")
    verify_polynomial(reduced, "primitive_sha256")
    linear_content_roots = {
        (-int(row["text"].split("+")[1].strip())) % PRIME
        for row in reduced["content"]["factors"]
        if row["shape"]["degrees"][-1] == 1
    }
    require(linear_content_roots == {
        1, I, 1231496538, 1620586492, PRIME-I, PRIME-1,
    }, "colored content roots")

    frobenius_payload = payloads["frobenius"]
    require(frobenius_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-coefficient-frobenius-v1",
            "Frobenius schema")
    frobenius = frobenius_payload["result"]
    require(frobenius["status"] == "COMPLETE" and
            frobenius["x_degrees"] == [4] and
            frobenius["coefficient_shape"] == {
                "degrees": [0, 7, 2047],
                "terms": 16368, "total_degree": 2051,
            } and frobenius["eliminant_shape"] == {
                "degrees": [0, 0, 16248],
                "terms": 16021, "total_degree": 16248,
            }, "Frobenius shapes")
    root_gcd = frobenius["base_field_root_gcd"]
    require(root_gcd["degree"] == 15 and
            all(row["degree"] == row["multiplicity"] == 1
                for row in root_gcd["factors"]), "Frobenius split gcd")
    expected_roots = [
        0, 1, I, 49838125, 429003821, 576044550, 592669297,
        1231496538, 1620586492, 1662124772, 1709004077,
        1998500970, 2066915989, PRIME-I, PRIME-1,
    ]
    require(sorted(root_from_factor(row["text"])
                   for row in root_gcd["factors"]) == sorted(expected_roots),
            "Frobenius root census")
    eliminant_path = EXPERIMENTS / frobenius["eliminant_file"]
    require(hashlib.sha256(eliminant_path.read_bytes()).hexdigest() ==
            frobenius["eliminant_file_sha256"] and
            hashlib.sha256(eliminant_path.read_text().strip().encode()).hexdigest() ==
            frobenius["eliminant_sha256"], "eliminant hashes")

    atlas_payload = payloads["atlas"]
    require(atlas_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-candidate-atlas-v1",
            "atlas schema")
    atlas = atlas_payload["result"]
    require(atlas["status"] == "COMPLETE" and atlas["t_root_count"] == 15 and
            [row["t"] for row in atlas["rows"]] == sorted(expected_roots),
            "atlas coverage")
    generic_b_rows = []
    lift_exception_points = set()
    for row in atlas["rows"]:
        if row["t_guard"] or row["content_exceptional"]:
            continue
        for w0_row in row["w0_rows"]:
            if w0_row.get("status") == "LIFT_LEADING_EXCEPTION":
                lift_exception_points.add((row["t"], w0_row["w0"]))
            else:
                generic_b_rows.append(w0_row)
    require(len(generic_b_rows) == 4 and
            sum(len(row["w1_rows"]) for row in generic_b_rows) == 8 and
            all(row["d0_zero"] and
                all(item["d1_zero"] for item in row["w1_rows"])
                for row in generic_b_rows), "generic denominator exclusion")

    content_payload = payloads["content"]
    require(content_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-colored-content-fiber-replay-v1",
            "content schema")
    content = content_payload["result"]
    require(content["status"] == "COMPLETE" and
            content["admissible_content_roots"] == [1231496538, 1620586492] and
            len(content["rows"]) == 2, "content coverage")
    for row in content["rows"]:
        require(row["w0_rows"] == [] and
                [(item["degree"], item["multiplicity"])
                 for item in row["h_factors"]] == [(2, 2), (2, 2)],
                "content fiber has no deployed w0")

    scales_payload = payloads["scales"]
    require(scales_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-subresultant-scale-atlas-v1",
            "scale schema")
    scales = scales_payload["result"]
    require(scales["status"] == "COMPLETE" and
            scales["exceptional_point_count"] == 19, "scale coverage")
    expected_scales = [
        ("h_leading", [0, 0, 8], 1),
        ("linear_leading", [7, 0, 197], 8),
        ("quadratic_content", [0, 0, 182], 3),
        ("quadratic_leading", [7, 0, 276], 6),
        ("candidate_content", [0, 0, 179], 5),
        ("candidate_leading_A", [7, 0, 688], 13),
    ]
    require([(row["name"], row["shape"]["degrees"],
              row["base_field_t_degree"]) for row in scales["scale_rows"]] ==
            expected_scales, "scale census")
    scale_points = {(row["t"], row["w0"])
                    for row in scales["replay_rows"]}
    require(lift_exception_points <= scale_points,
            "generic lift exceptions covered by scale atlas")
    non_guard = [row for row in scales["replay_rows"] if not row["t_guard"]]
    require(len(non_guard) == 6 and
            sum(not row["b_rows"] for row in non_guard) == 2 and
            sum(len(row["b_rows"]) for row in non_guard) == 4 and
            sum(len(item["w1_rows"])
                for row in non_guard for item in row["b_rows"]) == 8,
            "scale replay counts")
    require(all(item["d0_zero"] and
                all(w1["d1_zero"] for w1 in item["w1_rows"])
                for row in non_guard for item in row["b_rows"]),
            "scale denominator exclusion")


def main():
    payloads = {}
    for name, filename in FILES.items():
        path = EXPERIMENTS / filename
        require(hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[name],
                f"artifact hash {name}")
        payloads[name] = json.loads(path.read_text())
    verify_payloads(payloads)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "does not exclude the main `L!=0` component" in statement,
            "statement status and boundary")
    require("complete exclusion" in contract and "nonclaim" in contract,
            "claim contract")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_exceptional_coefficient_projection_decomposition",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_universal_target_elimination_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-4 exceptional reconstruction exclusion verified")


if __name__ == "__main__":
    main()
