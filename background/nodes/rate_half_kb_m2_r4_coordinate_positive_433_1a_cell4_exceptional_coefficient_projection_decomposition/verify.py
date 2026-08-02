#!/usr/bin/env python3
"""Verify the cell-4 exceptional coefficient projection decomposition."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell4_exceptional_coefficient_projection_decomposition"
)
FILES = {
    "ledger": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_ledger_result.json",
    "gcd": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_gcd_result.json",
    "sequence": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_sequence_result.json",
    "lex": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_lex_result.json",
    "factor": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_tpoly_factor_result.json",
    "lift": "rate_half_kb_positive_433_1a_cell4_pair_exceptional_h_b_gcd_result.json",
}
HASHES = {
    "ledger": "0a6dda18b50b781f43c18fd1c2227c06780b957ce9bc64bffb96071aff16615a",
    "gcd": "14ff20605cca740d77a0b958f1f9f0213bdf0ea51fdb6d186010440516ec3fe8",
    "sequence": "97a2e4a1a2604d8d1aed0ab0055efd9658e02cc45d36a677d707913cccc723d7",
    "lex": "b43f5564881d58c5b49066e933c107b6c70a7242ee51393dd038e27a7e006491",
    "factor": "9fb8910e89aa959f5af9b87546244c7b86a65cf1b5e796e09120655dc5033077",
    "lift": "889fe454c5864fba61940264892404e840cec34317b3659f8a3ffa6bcc3b8a23",
}
ARCHIVES = {
    "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_sources.tar.gz":
        "fe4a266328c14d6ba5625d2900589cbc1f87e6a669631f1104c78784d6fbd009",
    "rate_half_kb_positive_433_1a_cell4_pair_exceptional_b_resultant_primitive_sources.tar.gz":
        "4c123e2cfa036e849c3dc482964aa75461ba7befabf9b094efe6eb0bf6234dfd",
}
PRIME = 2130706433
I = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_file(row, canonical_key="sha256"):
    path = EXPERIMENTS / row["file"]
    require(hashlib.sha256(path.read_bytes()).hexdigest() ==
            row["file_sha256"], f"file hash {row['file']}")
    text = path.read_text().strip()
    require(hashlib.sha256(text.encode()).hexdigest() == row[canonical_key],
            f"canonical hash {row['file']}")
    return text


def verify_payloads(payloads):
    ledger = payloads["ledger"]
    require(ledger["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-ledger-v1",
            "ledger schema")
    require(ledger["status"] == "COMPLETE" and
            ledger["field"] == PRIME and ledger["degree_bound"] == 4 and
            ledger["evaluation_rank"] == 15,
            "ledger completion and rank")
    require(len(ledger["monomials"]) == len(ledger["points"]) ==
            len(ledger["rows"]) == 15, "ledger coverage")
    require([row["point"] for row in ledger["rows"]] == ledger["points"],
            "ledger point order")
    for row in ledger["rows"]:
        require(row["status"] == "COMPLETE" and
                row["resultant_shape"]["degrees"][1] == 0,
                "resultant completion")
        verify_file(row, "resultant_sha256")

    gcd_payload = payloads["gcd"]
    require(gcd_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-gcd-v1",
            "gcd schema")
    require(gcd_payload["source_ledger_sha256"] == HASHES["ledger"],
            "gcd ledger chain")
    gcd_result = gcd_payload["result"]
    require(gcd_result["status"] == "COMPLETE", "gcd completion")
    common = gcd_result["common"]
    factors = common["factors"]
    require([(row["shape"]["degrees"], row["multiplicity"])
             for row in factors] == [
        ([0, 3], 14), ([0, 1], 26), ([0, 1], 42),
        ([0, 1], 62), ([0, 3], 90), ([0, 1], 228),
        ([8, 12], 2),
    ], "common factor census")
    common_texts = [verify_file(row) for row in factors]
    require(common_texts[1:4] == [
        "t + 1", "t + 2130706432", "t + 16711679",
    ] and common_texts[5] == "t + 2113994754",
            "common guard factor texts")
    require(factors[6]["shape"] == {
        "degrees": [8, 12], "terms": 97, "total_degree": 16,
    }, "H shape")
    require(len(gcd_result["primitive_rows"]) == 15, "primitive coverage")
    for row in gcd_result["primitive_rows"]:
        verify_file(row)

    sequence = payloads["sequence"]
    require(sequence["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-sequence-v1",
            "sequence schema")
    seq = sequence["result"]
    require(seq["status"] == "COMPLETE" and seq["completed_stages"] == 11 and
            seq["unit"] is False, "sequence completion")
    for marker in ("\n528\nEND_STAGE_0", "\n472\nUNIT=0",
                   "\n471\nUNIT=0", "\n470\nUNIT=0"):
        require(marker in seq["stdout"], f"degree marker {marker!r}")
    require(seq["stdout"].count("\n470\nUNIT=0") == 5,
            "stable degree-470 tail")

    lex_payload = payloads["lex"]
    require(lex_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-lex-v1",
            "lex schema")
    lex = lex_payload["result"]
    require(lex["status"] == "COMPLETE" and
            "BEGIN_DP\n0\n29\n470\nEND_DP" in lex["stdout"] and
            "BEGIN_LEX\n0\n17\n470\n105\n93\nEND_LEX" in lex["stdout"],
            "lex dimensions")
    t_path = EXPERIMENTS / lex["t_polynomial_file"]
    require(hashlib.sha256(t_path.read_bytes()).hexdigest() ==
            lex["t_polynomial_file_sha256"], "t eliminant file hash")
    require(hashlib.sha256(t_path.read_text().strip().encode()).hexdigest() ==
            lex["t_polynomial_sha256"], "t eliminant canonical hash")

    factor_payload = payloads["factor"]
    require(factor_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-b-resultant-primitive-tpoly-factor-v1",
            "t factor schema")
    factor_result = factor_payload["result"]
    require(factor_result["status"] == "COMPLETE" and
            factor_result["field"] == PRIME and
            factor_result["source_degree"] == 105 and
            factor_result["source_terms"] == 93,
            "t factor completion")
    t_factors = factor_result["factors"]
    require([(row["degree"], row["multiplicity"], row.get("root"))
             for row in t_factors] == [
        (1, 13, 0), (1, 4, PRIME-I), (3, 5, None),
        (1, 11, I), (1, 18, PRIME-1), (1, 44, 1),
    ], "t factor census")
    for row in t_factors:
        verify_file(row)

    lift_payload = payloads["lift"]
    require(lift_payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell4-pair-exceptional-h-b-gcd-v3",
            "lift schema")
    lift = lift_payload["result"]
    require(lift["status"] == "COMPLETE" and lift["field"] == PRIME and
            lift["h_shape"] == {
                "degrees": [8, 0, 12], "terms": 97, "total_degree": 16,
            }, "lift completion")
    require(lift["candidate_shape"] == {
        "degrees": [7, 1, 688], "terms": 10992, "total_degree": 693,
    }, "linear lift shape")
    candidate_path = EXPERIMENTS / lift["candidate_file"]
    require(hashlib.sha256(candidate_path.read_bytes()).hexdigest() ==
            lift["candidate_file_sha256"], "candidate file hash")
    require(hashlib.sha256(candidate_path.read_text().strip().encode()).hexdigest() ==
            lift["candidate_sha256"], "candidate canonical hash")
    require(set(lift["divisibility"]) == {"plane", "linear", "constant", "live"},
            "lift divisor coverage")
    for name, row in lift["divisibility"].items():
        require(row["remainder_shape"]["terms"] == 0 and
                all(item["zero_mod_h"] for item in row["coefficients"]),
                f"zero H remainder {name}")

    require(pow(I, 2, PRIME) == PRIME-1, "deployed square root of -1")
    for root in (0, 1, PRIME-1, I, PRIME-I):
        require(root*(1-root*root)*(1+root*root) % PRIME == 0,
                f"original t guard {root}")


def main():
    payloads = {}
    for name, filename in FILES.items():
        path = EXPERIMENTS / filename
        require(hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[name],
                f"artifact hash {name}")
        payloads[name] = json.loads(path.read_text())
    for filename, expected in ARCHIVES.items():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest() ==
                expected, f"archive hash {filename}")
    verify_payloads(payloads)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "does not prove that every `H` point" in statement,
            "statement status and nonclaim")
    require("necessary projection" in contract and "nonclaim" in contract,
            "claim contract")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_signed_pair_projection_reconstruction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-4 exceptional coefficient projection verified")


if __name__ == "__main__":
    main()
