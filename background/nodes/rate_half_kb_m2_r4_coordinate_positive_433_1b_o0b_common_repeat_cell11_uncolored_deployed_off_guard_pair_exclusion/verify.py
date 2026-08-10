#!/usr/bin/env python3
"""Verify the cell-11 deployed off-guard paired-product exclusion."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_generic_rank_atlas"
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433
MISSING = ("DE+", "DF+", "EF")
EPSILONS = {
    "mm": (-1, -1),
    "mp": (-1, 1),
    "pm": (1, -1),
    "pp": (1, 1),
}
LAUNCHER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_generic_rank_modal.py"
)
COMPILER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_exceptional_manifest.py"
)
MANIFEST = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_uncolored_exceptional_replay_manifest.json"
)
FILES = {
    LAUNCHER: "d6995ccc293a30c3277c108a42dcbcbe1c7afa7eece40cd263a1cfd9cc9cb786",
    COMPILER: "4ec6de6737e081c8cdfb37d5edfa35b5a9d43fbff6d22ea0040d989e21731258",
    MANIFEST: "1f2f13e925f7a6b05141b6757cb21417d8537866f59dce59ff7a2a6a56bc2fb1",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcminus_emm_result.json": "3fdf054568151bd55799507bfb92314758e67f51c9829ab0c0ae18284b22a48c",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcminus_emp_result.json": "be543841e5a28692b06114154ad5b2c2ea55a91236743531649f2adb5c39e53e",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcminus_epm_result.json": "0288f3927dbbe2d1129e0dc83aecd1fbe271d48fa0487165223fc4689548d583",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcminus_epp_result.json": "6cb8f12b9736fbe557a922609045ef51e9024899bef6e65162a175180714f83e",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcplus_emm_result.json": "7fcaae4a89c5d4d65c49f6f078b6af7e71261b4564c7f96894d49a085a5bddca",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcplus_emp_result.json": "27a90f419645562223d6a4bc2eb4454a935f9ffc514b8983c0c907ce7ad0733a",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcplus_epm_result.json": "15fe77d6130ed26c0395d2c7d056e4a77f40a600ba4039597b4f481829d06631",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_resultant_norm_bcplus_epp_result.json": "6a082ad0f355500341b9ecabd5d040f9c4188b2425970219f28445b9a6f90301",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcminus_emm_result.json": "1c6abee11c174be2280928a8ef5a1031e6ce78ba56f727d0719b456390566e69",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcminus_emp_result.json": "78590a25e112c8470bfe5d0ee016cef1df8167dd0090612e5e417508ebb4d37f",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcminus_epm_result.json": "1dabb3b34e76f59966c03e1273917d1bd2a8bc2e0e643e3463aecab79683b286",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcminus_epp_result.json": "fa6b7b398afb095ae77ef31609dc9ea9452d7acaa27c9d36457335846f336839",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcplus_emm_result.json": "4b8a9cfb63d27f5734c21b80a0e624b0e21352b109a6c0959f7b05715942b26e",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcplus_emp_result.json": "feac376c5d39332a3cd8fac73643f57738250cd96a1c64f5e61e8ade487c059b",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcplus_epm_result.json": "3e403d3f7eba4d536995bd252ba6b7d8dd052627bd35aa306430a2dda598063f",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_exceptional_replay_bcplus_epp_result.json": "acd61c91f6421c82bdece449704c585df7ceafe6d72df4f0ea4585c3f4f61e6e",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(filename):
    return json.loads((EXPERIMENTS / filename).read_text())


def shard_filename(kind, bc_sign, token):
    sign = "plus" if bc_sign == 1 else "minus"
    return (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_uncolored_"
        f"{kind}_bc{sign}_e{token}_result.json"
    )


def case_key(row, x_value):
    return (
        row["bc_sign"], *row["epsilon"], row["missing_record"],
        row["sigma_o"], row["pairing_index"], x_value,
    )


def validate_norm_shards():
    statuses = Counter()
    manifest_cases = []
    norm_hashes = {}
    for bc_sign in (-1, 1):
        for token, epsilon in EPSILONS.items():
            filename = shard_filename("resultant_norm", bc_sign, token)
            payload = load(filename)
            norm_hashes[filename] = FILES[filename]
            require(
                payload["schema"].endswith(
                    "cell11-uncolored-resultant-factor-atlas-v1"
                ),
                f"norm schema: {filename}",
            )
            require(
                payload["bc_sign"] == bc_sign
                and tuple(payload["epsilon"]) == epsilon,
                f"norm shard scope: {filename}",
            )
            require(
                payload["complete_source_tower_atlas"]
                and payload["case_count"] == len(payload["rows"]) == 90,
                f"norm shard census: {filename}",
            )
            expected = set(itertools.product(MISSING, (-1, 1), range(15)))
            actual = set()
            shard_statuses = Counter()
            for row in payload["rows"]:
                key = (
                    row["missing_record"], row["sigma_o"],
                    row["pairing_index"],
                )
                require(key in expected and key not in actual, "norm formal key")
                actual.add(key)
                require(
                    row["bc_sign"] == bc_sign
                    and tuple(row["epsilon"]) == epsilon,
                    "norm row scope",
                )
                selected = row["selected"]
                norm = selected["resultant_nested_norm"]
                require(
                    norm["witness_value"] == selected["witness_determinant"],
                    "nested norm witness equality",
                )
                require(
                    selected["resultant_coordinate_gcd"][
                        "all_factors_construction_guards"
                    ],
                    "vertical factor",
                )
                roots = norm["base_field_roots"]
                non_guard = [
                    root for root in roots
                    if not root["construction_guard_factor"]
                ]
                require(non_guard == norm["non_guard_base_field_roots"],
                        "non-guard root projection")
                expected_status = (
                    "DEPLOYED_POINTWISE_NORM_COVER"
                    if non_guard else "DEPLOYED_OFF_GUARD_UNIT"
                )
                require(row["status"] == expected_status, "norm row status")
                statuses[row["status"]] += 1
                shard_statuses[row["status"]] += 1
                for root in non_guard:
                    require(
                        0 <= root["x"] < PRIME
                        and root["multiplicity"] > 0,
                        "norm root",
                    )
                    manifest_cases.append({
                        "bc_sign": row["bc_sign"],
                        "epsilon": row["epsilon"],
                        "missing_record": row["missing_record"],
                        "sigma_o": row["sigma_o"],
                        "pairing_index": row["pairing_index"],
                        "x": root["x"],
                        "root_multiplicity": root["multiplicity"],
                        "root_factor_sha256": root["factor_sha256"],
                        "norm_numerator_sha256": norm["numerator"]["sha256"],
                    })
            require(actual == expected, "norm formal coverage")
            require(dict(shard_statuses) == payload["status_counts"],
                    "norm printed status")
    require(
        dict(statuses) == {
            "DEPLOYED_OFF_GUARD_UNIT": 288,
            "DEPLOYED_POINTWISE_NORM_COVER": 432,
        },
        "norm aggregate status",
    )
    manifest_cases.sort(key=lambda row: (
        row["bc_sign"], *row["epsilon"], row["missing_record"],
        row["sigma_o"], row["pairing_index"], row["x"],
    ))
    return manifest_cases, norm_hashes


def validate_manifest(expected_cases, norm_hashes):
    manifest = load(MANIFEST)
    require(manifest["case_count"] == len(manifest["cases"]) == 1584,
            "manifest case census")
    require(manifest["distinct_x_count"] == 126, "manifest root census")
    require(manifest["norm_row_count"] == 720, "manifest norm census")
    require(manifest["norm_shard_sha256"] == norm_hashes,
            "manifest norm custody")
    require(manifest["cases"] == expected_cases, "manifest exact cases")
    return manifest


def validate_replay_shards(manifest):
    expected = {
        (
            row["bc_sign"], *row["epsilon"], row["missing_record"],
            row["sigma_o"], row["pairing_index"], row["x"],
        )
        for row in manifest["cases"]
    }
    actual = set()
    total = 0
    for bc_sign in (-1, 1):
        for token, epsilon in EPSILONS.items():
            filename = shard_filename("exceptional_replay", bc_sign, token)
            payload = load(filename)
            require(
                payload["schema"].endswith(
                    "cell11-uncolored-exceptional-pair-replay-v1"
                ),
                f"replay schema: {filename}",
            )
            require(
                payload["bc_sign"] == bc_sign
                and tuple(payload["epsilon"]) == epsilon,
                f"replay shard scope: {filename}",
            )
            require(payload["case_count"] == len(payload["rows"]),
                    "replay shard census")
            require(
                payload["status_counts"] == {
                    "EXCEPTIONAL_ROOT_EXCLUDED": payload["case_count"]
                },
                "replay printed status",
            )
            for row in payload["rows"]:
                total += 1
                key = case_key(row, row["replay_x"])
                require(key in expected and key not in actual, "replay formal key")
                actual.add(key)
                require(row["status"] == "EXCEPTIONAL_ROOT_EXCLUDED",
                        "replay row status")
                pair_rows = row["pair_rows"]
                require(
                    len(pair_rows) == 3
                    and {tuple(pair["equations"]) for pair in pair_rows}
                    == {(0, 1), (0, 2), (1, 2)},
                    "replay pair coverage",
                )
                full_rank = 0
                for pair in pair_rows:
                    require(pair["construction_guards_nonzero"],
                            "replay construction guard")
                    require(pair["replay_x"] == row["replay_x"],
                            "replay base value")
                    determinant = pair["replay_determinant"]
                    require(0 <= determinant < PRIME, "replay determinant range")
                    if pair["replay_status"] == "FULL_RANK":
                        require(determinant != 0 and pair["last_rank"] == pair["size"],
                                "replay full rank")
                        full_rank += 1
                    else:
                        require(
                            pair["replay_status"] == "SINGULAR"
                            and determinant == 0 and pair["last_rank"] is None,
                            "replay singular rank",
                        )
                require(full_rank > 0, "all replay pairs singular")
    require(total == len(actual) == 1584 and actual == expected,
            "replay aggregate coverage")


def main():
    for filename, expected_hash in FILES.items():
        actual_hash = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual_hash == expected_hash, f"file custody: {filename}")
    manifest_cases, norm_hashes = validate_norm_shards()
    manifest = validate_manifest(manifest_cases, norm_hashes)
    validate_replay_shards(manifest)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {
        (row["from"], row["to"], row.get("kind", "req"))
        for row in dag["edges"]
    }
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED", "parent status")
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELL11_OFF_GUARD_VERIFY_PASS "
        "representatives=720 roots=1584 distinct_x=126 excluded=1584"
    )


if __name__ == "__main__":
    main()
