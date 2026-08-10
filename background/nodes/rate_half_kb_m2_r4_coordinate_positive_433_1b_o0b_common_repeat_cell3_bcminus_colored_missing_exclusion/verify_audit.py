#!/usr/bin/env python3
"""Hostile controls for the cell-3 BC- colored exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("colored_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(norms, replay):
    try:
        VERIFY.ROOT_CACHE.clear()
        VERIFY.validate(norms, replay)
    except RuntimeError:
        return
    raise RuntimeError("mutation survived")


def main():
    norms = json.loads((VERIFY.EXPERIMENTS / VERIFY.NORM_RESULT).read_text())
    replay = json.loads((VERIFY.EXPERIMENTS / VERIFY.REPLAY_RESULT).read_text())
    VERIFY.validate(norms, replay)
    mutation = copy.deepcopy(replay)
    mutation["root_ledger"][0]["roots"].pop()
    reject(norms, mutation)
    mutation = copy.deepcopy(replay)
    mutation["root_ledger"].pop()
    reject(norms, mutation)
    mutation = copy.deepcopy(replay)
    mutation["rows"][0]["status"] = "NO_BASE_FIELD_Y"
    reject(norms, mutation)
    mutation = copy.deepcopy(replay)
    target = next(row for row in mutation["rows"] if row.get("y_rows"))
    target["y_rows"][0]["status"] = "TARGET_GUARD_BOUNDARY"
    reject(norms, mutation)
    mutation = copy.deepcopy(replay)
    mutation["cut_zero_points"].append({"fake": True})
    reject(norms, mutation)
    print("PASS repeated-BC cell3 BC- colored exclusion hostile audit: 5/5")


if __name__ == "__main__":
    main()
