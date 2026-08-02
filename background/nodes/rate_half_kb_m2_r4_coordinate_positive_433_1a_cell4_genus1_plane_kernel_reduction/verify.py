#!/usr/bin/env python3
"""Verify the cell-4 genus-one plane-kernel reduction packet."""

import hashlib
import json
from pathlib import Path
import re


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_genus1_plane_kernel_reduction"
)
FILES = {
    "scout": "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json",
    "profile": "rate_half_kb_positive_433_1a_remaining_palindromic_profile_result.json",
    "cover": "rate_half_kb_positive_433_1a_cell4_conic_cover_profile_result.json",
    "kernel": "rate_half_kb_positive_433_1a_cell4_kernel_reduction_result.json",
    "plane": "rate_half_kb_positive_433_1a_cell4_plane_kernel_flint_result.json",
    "target": "rate_half_kb_positive_433_1a_cell4_plane_target_free_family_result.json",
}
HASHES = {
    "scout": "13a82e809774880ccaf2b89d5dd62cbb4995533ecde59619db2ac65443bee172",
    "profile": "4b3f973743288f2bf742ce359121d40b1e6ef7075f674be321c297eea9de7441",
    "cover": "b6468e2c8916d4cf26d2d2824ff84694f808e83989e00db1c620a75c275ab494",
    "kernel": "90f82f6cd8d4cf2640ee1a05ee64a6fa61e83754dff33b4255ff2d626b4e3bbd",
    "plane": "26cc881846361a6f85d270dc436784991109f67982122b40cc4bbf75235e410e",
    "target": "26c94f21ef237a4ebea7990b665933165ff359eedbc6b2d5aed391874293109e",
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
        output[key] = (output.get(key, 0)+sign*coefficient) % PRIME
    return {key: coefficient for key, coefficient in output.items() if coefficient}


def verify_payloads(payloads):
    scout = payloads["scout"]
    require(scout["schema"] ==
            "rate-half-kb-positive-433-1a-remaining-lex-scout-v1",
            "scout schema")
    require(len(scout["rows"]) == 10 and
            all(row["status"] == "COMPLETE" for row in scout["rows"]),
            "scout completion")
    cell4 = next(row for row in scout["rows"] if row["cell"] == 4
                 and row["order"] == ["c", "r", "b", "t"])
    require(cell4["basis_size"] == 7 and
            "BEGIN_LEX_SUMMARY\n1\n7" in cell4["stdout"], "cell4 lex basis")

    profiles = payloads["profile"]
    require(profiles["source_scout_sha256"] == HASHES["scout"],
            "scout-to-profile chain")
    profile = next(row for row in profiles["rows"] if row["cell"] == 4)
    require(profile["status"] == "COMPLETE" and
            profile["palindromic"] is True and
            profile["reconstruction_equal"] is True, "reciprocal quotient")
    require(profile["eliminant_shape"] == {
        "degree_b": 4, "degree_t": 4, "terms": 21, "total_degree": 8,
    }, "cell4 eliminant shape")
    require([(row["degree"], row["multiplicity"])
             for row in profile["discriminant_factorization"]["factors"]] ==
            [(1, 1), (1, 1), (1, 2), (1, 4)], "quotient discriminant")

    cover = payloads["cover"]["result"]
    require(cover["status"] == "COMPLETE" and
            cover["source_profile_sha256"] == HASHES["profile"],
            "cover completion and chain")
    require(cover["conic_base_point"] == [1, 66846712], "conic point")
    numerator = cover["numerator_factorization"]["factors"]
    denominator = cover["denominator_factorization"]["factors"]
    require(cover["numerator_shape"] == {"degree": 6, "terms": 7} and
            [(row["degree"], row["multiplicity"]) for row in numerator] ==
            [(1, 1), (1, 2), (3, 1)], "genus-one branch profile")
    require([(row["degree"], row["multiplicity"]) for row in denominator] ==
            [(1, 2)]*4, "square denominator")

    kernel = payloads["kernel"]["result"]
    require(kernel["status"] == "COMPLETE" and kernel["basis_size"] == 7,
            "kernel reduction")
    reduced = kernel["reduced_coefficients"]
    b1_sum = parse_compact(reduced["b10"])
    for monomial, coefficient in parse_compact(reduced["b11"]).items():
        b1_sum[monomial] = (b1_sum.get(monomial, 0)+coefficient) % PRIME
    require(not any(b1_sum.values()), "lex B1 opposition")

    plane = payloads["plane"]["result"]
    require(plane["status"] == "COMPLETE" and plane["b1_opposite"] is True,
            "plane kernel completion")
    require(plane["source_scout_sha256"] == HASHES["scout"] and
            plane["source_kernel_sha256"] == HASHES["kernel"],
            "plane source chain")
    require(plane["plane_shape"] == {
        "degrees": [4, 4], "total_degree": 8, "terms": 21,
    }, "plane shape")
    require(plane["pseudo_scale_power"] == 9 and
            plane["common_projective_scale_shape"]["degrees"] == [0, 20] and
            plane["projected_common_scale_shape"]["degrees"] == [0, 49],
            "scale ledger")
    for row in plane["normalized_coefficients"].values():
        require(row["degrees"][0] <= 3 and row["degrees"][1] <= 18,
                "compact coefficient shape")

    target = payloads["target"]["result"]
    require(target["status"] == "TIMEOUT" and
            target["shapes_emitted"] is True and
            target["source_plane_sha256"] == HASHES["plane"],
            "honest target timeout")
    require([row["terms"] for row in target["equation_shapes"]] ==
            [1716, 10724, 20508, 26388], "target-free compiler")


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
    require("- **status:** PROVED" in statement and "genus one" in statement,
            "statement status and genus")
    require("does not exclude" in statement and "timeout" in contract.lower(),
            "nonclaim and timeout fences")

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
    print("positive 433-1a cell-4 genus-one plane-kernel reduction verified")


if __name__ == "__main__":
    main()
