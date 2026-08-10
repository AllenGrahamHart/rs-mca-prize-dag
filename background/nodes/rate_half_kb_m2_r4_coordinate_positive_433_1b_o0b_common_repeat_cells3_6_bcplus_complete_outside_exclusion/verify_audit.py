#!/usr/bin/env python3
"""Hostile controls for the complete cells-3/6 BC+ outside exclusion."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("aggregate_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(master, shards, label):
    try:
        VERIFY.validate(master, shards)
    except (RuntimeError, KeyError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    master, shards = VERIFY.load_payloads()
    VERIFY.validate(master, shards)
    mutation = copy.deepcopy(master)
    mutation["rows"].pop()
    reject(mutation, shards, "lost compact row")
    mutation = copy.deepcopy(master)
    mutation["rows"][0]["fiber_count"] -= 1
    reject(mutation, shards, "fiber census")
    mutation = copy.deepcopy(shards)
    mutation["DE+"]["rows"][0]["u_values"].pop()
    reject(master, mutation, "shard/master mismatch")
    mutation = copy.deepcopy(master)
    mutation["shards"]["EF"]["sha256"] = "0"*64
    reject(mutation, shards, "shard custody")
    print("PASS complete cells-3/6 BC+ outside hostile audit: 4/4")


if __name__ == "__main__":
    main()
