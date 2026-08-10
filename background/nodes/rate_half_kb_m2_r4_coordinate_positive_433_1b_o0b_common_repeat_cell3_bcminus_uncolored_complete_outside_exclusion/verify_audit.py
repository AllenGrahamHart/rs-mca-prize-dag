#!/usr/bin/env python3
"""Hostile controls for the complete BC- uncolored exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("aggregate_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, label):
    try:
        VERIFY.validate_master(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(VERIFY.MASTER.read_text())
    VERIFY.validate_master(payload)
    mutation = copy.deepcopy(payload); mutation["shards"]["DE+"]["sha256"] = "0"*64; reject(mutation, "shard")
    mutation = copy.deepcopy(payload); mutation["survivor_count"] = 1; reject(mutation, "survivor")
    mutation = copy.deepcopy(payload); mutation["rows"].pop(); reject(mutation, "row")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["fiber_count"] += 1; reject(mutation, "fiber")
    print("PASS repeated-BC cell3 BC- uncolored aggregate hostile audit: 4/4")


if __name__ == "__main__":
    main()
