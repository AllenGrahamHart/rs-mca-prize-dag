#!/usr/bin/env python3
"""Hostile controls for the repeated-BC colored-missing atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("colored_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(cut, roots, label):
    try:
        VERIFY.validate(cut, roots)
    except (RuntimeError, KeyError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    cut = json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES["cut_result"][0]).read_text())
    roots = json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES["root_result"][0]).read_text())
    VERIFY.validate(cut, roots)
    mutation = copy.deepcopy(cut); mutation["rows"].pop(); reject(mutation, roots, "lost cut")
    mutation = copy.deepcopy(cut); mutation["rows"][0]["dimension"] = 1; reject(mutation, roots, "dimension")
    mutation = copy.deepcopy(roots); mutation["rows"][0]["point_count"] = 1; reject(cut, mutation, "BE live")
    mutation = copy.deepcopy(roots)
    root = next(root for u_row in mutation["rows"][0]["u_rows"]
                for root in u_row.get("root_rows", []))
    root["status"] = "LIFTED"
    reject(cut, mutation, "guard")
    mutation = copy.deepcopy(roots)
    cf = next(row for row in mutation["rows"] if row["missing_record"] == "CF")
    cf["points"][0]["source_squared_sum"] ^= 1
    reject(cut, mutation, "CF sum")
    print("PASS repeated-BC BC+ colored-missing hostile audit: 5/5")


if __name__ == "__main__":
    main()
