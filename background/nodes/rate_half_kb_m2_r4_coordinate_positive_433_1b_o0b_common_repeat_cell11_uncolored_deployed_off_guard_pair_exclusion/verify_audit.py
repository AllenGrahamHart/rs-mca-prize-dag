#!/usr/bin/env python3
"""Hostile controls for the cell-11 deployed off-guard exclusion."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_off_guard_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(filename, mutation, phase, label):
    original_load = VERIFY.load
    payload = copy.deepcopy(original_load(filename))
    mutation(payload)

    def hostile_load(requested):
        return payload if requested == filename else original_load(requested)

    VERIFY.load = hostile_load
    try:
        phase()
    except RuntimeError:
        return
    finally:
        VERIFY.load = original_load
    raise RuntimeError(f"mutation survived: {label}")


def norm_phase():
    VERIFY.validate_norm_shards()


def manifest_phase():
    cases, hashes = VERIFY.validate_norm_shards()
    VERIFY.validate_manifest(cases, hashes)


def replay_phase():
    cases, hashes = VERIFY.validate_norm_shards()
    manifest = VERIFY.validate_manifest(cases, hashes)
    VERIFY.validate_replay_shards(manifest)


def main():
    norm = VERIFY.shard_filename("resultant_norm", 1, "mm")
    replay = VERIFY.shard_filename("exceptional_replay", -1, "mm")
    reject(
        norm,
        lambda value: value["rows"][0].__setitem__(
            "status", "DEPLOYED_OFF_GUARD_UNIT"
        ),
        norm_phase,
        "norm status",
    )
    reject(
        norm,
        lambda value: value["rows"][0]["selected"][
            "resultant_nested_norm"
        ].__setitem__("witness_value", 0),
        norm_phase,
        "nested norm witness",
    )
    reject(
        norm,
        lambda value: value["rows"][0]["selected"][
            "resultant_coordinate_gcd"
        ].__setitem__("all_factors_construction_guards", False),
        norm_phase,
        "vertical factor",
    )
    reject(
        VERIFY.MANIFEST,
        lambda value: value["cases"].pop(),
        manifest_phase,
        "manifest coverage",
    )
    reject(
        VERIFY.MANIFEST,
        lambda value: value["norm_shard_sha256"].__setitem__(norm, "0" * 64),
        manifest_phase,
        "manifest custody",
    )
    reject(
        replay,
        lambda value: value["rows"][0].__setitem__(
            "status", "EXCEPTIONAL_ROOT_UNRESOLVED"
        ),
        replay_phase,
        "replay status",
    )

    def singularize(value):
        for pair in value["rows"][0]["pair_rows"]:
            pair["replay_status"] = "SINGULAR"
            pair["replay_determinant"] = 0
            pair["last_rank"] = None

    reject(replay, singularize, replay_phase, "all pairs singular")
    print("PASS cell11 deployed off-guard hostile audit: 7/7")


if __name__ == "__main__":
    main()
