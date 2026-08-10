#!/usr/bin/env python3
"""Hostile controls for the cell-3 BC- generic-rank atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("generic_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload, label):
    try:
        VERIFY.validate(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads((VERIFY.EXPERIMENTS / VERIFY.RESULT).read_text())
    VERIFY.validate(payload)
    mutation = copy.deepcopy(payload); mutation["rows"].pop(); reject(mutation, "row")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["selected"]["rank"] = 15; reject(mutation, "rank")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["selected"]["equations"] = [0, 2]; reject(mutation, "pair")
    mutation = copy.deepcopy(payload); mutation["rows"][0]["guard_hashes"] = ["0"*64]; reject(mutation, "guard")
    mutation = copy.deepcopy(payload); mutation["complete_atlas"] = False; reject(mutation, "completion")
    print("PASS repeated-BC cell3 BC- generic hostile audit: 5/5")


if __name__ == "__main__":
    main()
