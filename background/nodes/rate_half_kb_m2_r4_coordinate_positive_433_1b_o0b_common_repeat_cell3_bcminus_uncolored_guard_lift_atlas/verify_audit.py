#!/usr/bin/env python3
"""Hostile controls for the cell-3 BC- guard-lift atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("lift_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(function, *args):
    try:
        function(*args)
    except RuntimeError:
        return
    raise RuntimeError("mutation survived")


def main():
    generic = json.loads((VERIFY.EXPERIMENTS / VERIFY.GENERIC).read_text())
    roots = json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES["roots_result"][0]).read_text())
    lifts = json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES["lifts_result"][0]).read_text())
    VERIFY.validate_roots(roots, generic)
    VERIFY.validate_lifts(lifts, roots)
    mutation = copy.deepcopy(roots); mutation["rows"][0]["roots"].append(1); reject(VERIFY.validate_roots, mutation, generic)
    mutation = copy.deepcopy(roots); mutation["status_counts"] = {}; reject(VERIFY.validate_roots, mutation, generic)
    mutation = copy.deepcopy(lifts); mutation["rows"][0]["status"] = "LIFTED"; reject(VERIFY.validate_lifts, mutation, roots)
    mutation = copy.deepcopy(lifts); mutation["source_tower_sha256"] = "0"*64; reject(VERIFY.validate_lifts, mutation, roots)
    mutation = copy.deepcopy(lifts); mutation["guarded_point_count"] -= 1; reject(VERIFY.validate_lifts, mutation, roots)
    print("PASS repeated-BC cell3 BC- guard-lift hostile audit: 5/5")


if __name__ == "__main__":
    main()
