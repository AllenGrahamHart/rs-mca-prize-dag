#!/usr/bin/env python3
"""Hostile controls for the O0b split rank-drop exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("rankdrop_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(master, shards, points):
    try:
        VERIFY.validate(master, shards, points)
    except RuntimeError:
        return
    raise RuntimeError("mutation survived")


def main():
    master = json.loads(VERIFY.MASTER.read_text())
    shards = {key: json.loads(path.read_text())
              for key, path in VERIFY.SHARDS.items()}
    points = json.loads(VERIFY.POINTS.read_text())
    VERIFY.validate(master, shards, points)
    mutation = copy.deepcopy(master)
    mutation["shard_manifest"]["S0"]["sha256"] = "0" * 64
    reject(mutation, shards, points)
    mutation = copy.deepcopy(shards)
    mutation["S0"]["lanes"].pop()
    reject(master, mutation, points)
    mutation = copy.deepcopy(shards)
    mutation["SDE"]["lanes"][0]["rows"].pop()
    reject(master, mutation, points)
    mutation = copy.deepcopy(shards)
    mutation["SDF"]["lanes"][0]["rows"][0]["unit"] = False
    reject(master, mutation, points)
    mutation = copy.deepcopy(points)
    target = next(row for row in mutation["rows"] if row["rational_points"])
    target["rational_points"][0]["b"] ^= 1
    reject(master, shards, mutation)
    print("PASS positive 433-1b/O0b split rank-drop hostile audit: 5/5")


if __name__ == "__main__":
    main()
