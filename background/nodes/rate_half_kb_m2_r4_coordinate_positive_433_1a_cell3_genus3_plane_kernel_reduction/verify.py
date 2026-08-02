#!/usr/bin/env python3
"""Verify the cell-3 genus-three plane-kernel reduction packet."""

import hashlib
import json
from pathlib import Path
import re


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell3_genus3_plane_kernel_reduction"
)
FILES = {
    "scout": "rate_half_kb_positive_433_1a_cell3_common_triangle_scout_result.json",
    "profile": "rate_half_kb_positive_433_1a_cell3_palindromic_profile_result.json",
    "cover": "rate_half_kb_positive_433_1a_cell3_conic_cover_profile_result.json",
    "kernel": "rate_half_kb_positive_433_1a_cell3_kernel_reduction_result.json",
    "plane": "rate_half_kb_positive_433_1a_cell3_plane_kernel_flint_result.json",
    "target": "rate_half_kb_positive_433_1a_cell3_plane_target_free_family_result.json",
    "w2": "rate_half_kb_positive_433_1a_cell3_w2_resultant_result.json",
    "z2": "rate_half_kb_positive_433_1a_cell3_z2_resultant_result.json",
}
HASHES = {
    "scout": "5448d98da4033a2a589a201223eb687b83bfabb3de24699d9b1c96c36401a340",
    "profile": "d36e63493bcca128c18293f298a614df51fd8449e1cd06b6a1e3cd0da3151550",
    "cover": "64f655da9e5c286ed2849d2ae3d12056acbed7b12e07d98be15221db0b248c42",
    "kernel": "afa3829dec518a9000d65cfcca5ec7632980986086f53ce5de6f2eaf12f06b48",
    "plane": "4e36308e9e5d062f9c60280057b961c8181d0edb2406831cfaae7be76c7a2a0a",
    "target": "9816c4eaa0ed2761c752e4fef276c6282f93ed4550d7d40e66d77d73768feb4d",
    "w2": "51717a105a7aa87ec9c306b2d99e65a762ab85af238cb6ca81f172640e4b52b3",
    "z2": "a929b726e49f637fd4dbd86c7bda35bdd51c2cf16d332e154b7fb3621341b88a",
}
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_compact(value):
    output = {}
    for raw_term in re.findall(r"[+-]?[^+-]+", value):
        sign = 1
        term = raw_term
        if term.startswith("+"):
            term = term[1:]
        elif term.startswith("-"):
            sign = -1
            term = term[1:]
        match = re.match(r"\d+", term)
        coefficient = int(match.group(0)) if match else 1
        term = term[match.end():] if match else term
        exponents = {name: 0 for name in "crbt"}
        while term:
            match = re.match(r"([crbt])(\d*)", term)
            require(match is not None, "compact parser")
            name, exponent = match.groups()
            exponents[name] += int(exponent) if exponent else 1
            term = term[match.end():]
        key = tuple(exponents[name] for name in "crbt")
        output[key] = (output.get(key, 0) + sign*coefficient) % PRIME
    return {key: coefficient for key, coefficient in output.items() if coefficient}


def verify_payloads(payloads):
    scout = payloads["scout"]
    require(scout["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-common-triangle-scout-v1",
            "scout schema")
    require(len(scout["rows"]) == 4 and
            all(row["status"] == "COMPLETE" for row in scout["rows"]),
            "scout completion")
    lex = next(row for row in scout["rows"]
               if row["order"] == ["c", "r", "b", "t"])
    require("BEGIN_LEX_SUMMARY\n1\n7" in lex["stdout"], "seven-element lex basis")

    profile = payloads["profile"]["result"]
    require(profile["status"] == "COMPLETE" and profile["palindromic"] is True,
            "palindromic profile")
    require(profile["reconstruction_equal"] is True, "quotient reconstruction")
    factors = profile["discriminant_factorization"]["factors"]
    require([(row["degree"], row["multiplicity"]) for row in factors] ==
            [(1, 1), (1, 1), (1, 2), (1, 4)], "first discriminant")

    cover = payloads["cover"]["result"]
    require(cover["status"] == "COMPLETE", "cover completion")
    require(cover["conic_base_point"] == [1, 66846712], "conic point")
    numerator = cover["numerator_factorization"]["factors"]
    denominator = cover["denominator_factorization"]["factors"]
    require(cover["numerator_shape"]["degree"] == 8 and
            [(row["degree"], row["multiplicity"]) for row in numerator] ==
            [(1, 1)]*5 + [(3, 1)], "square-free degree-eight cover")
    require([(row["degree"], row["multiplicity"]) for row in denominator] ==
            [(1, 2), (3, 2)], "square denominator")

    kernel = payloads["kernel"]["result"]
    require(kernel["status"] == "COMPLETE" and kernel["basis_size"] == 7,
            "kernel reduction")
    reduced = kernel["reduced_coefficients"]
    b1_sum = parse_compact(reduced["b10"])
    for monomial, coefficient in parse_compact(reduced["b11"]).items():
        b1_sum[monomial] = (b1_sum.get(monomial, 0) + coefficient) % PRIME
    require(not any(b1_sum.values()), "lex B1 opposition")

    plane = payloads["plane"]["result"]
    require(plane["status"] == "COMPLETE" and plane["b1_opposite"] is True,
            "plane kernel completion")
    require(plane["plane_shape"] ==
            {"degrees": [4, 4], "total_degree": 8, "terms": 25},
            "plane shape")
    require(plane["pseudo_scale_power"] == 16, "pseudo scale")
    require(plane["common_projective_scale_shape"]["degrees"] == [0, 12],
            "first common scale")
    require(plane["projected_common_scale_shape"]["degrees"] == [0, 84],
            "projected common scale")
    for row in plane["normalized_coefficients"].values():
        require(row["degrees"][0] <= 3 and row["degrees"][1] <= 22,
                "compact coefficient shape")

    target = payloads["target"]["result"]
    require(target["status"] == "TIMEOUT" and
            target["shapes_emitted"] is True, "honest timeout fence")
    require([row["pseudo_steps"] for row in target["equation_shapes"]] ==
            [3, 9, 7, 7], "target-free equation compiler")

    w2 = payloads["w2"]
    require(w2["status"] == "REMOTE_ERROR" and
            "TypeError" in w2["error"], "honest w2 implementation fence")
    require([row["terms"] for row in w2["cut_summary"]["reduced_shapes"]] ==
            [23532, 321284], "squared w2 size fence")

    z2 = payloads["z2"]
    require(z2["status"] == "REMOTE_ERROR" and
            "FunctionTimeoutError" in z2["error"], "honest z2 timeout")
    require([row["terms"] for row in z2["cut_summary"]["reduced_shapes"]] ==
            [23532, 30276], "direct z2 input fence")


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
    require("- **status:** PROVED" in statement, "statement status")
    require("genus three" in statement and "does not\nexclude" in statement,
            "statement scope")
    require("timeout" in contract.lower() and "nonclaim" in contract,
            "contract fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_remaining_common_curve_profile",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-3 genus-three plane-kernel reduction verified")


if __name__ == "__main__":
    main()
