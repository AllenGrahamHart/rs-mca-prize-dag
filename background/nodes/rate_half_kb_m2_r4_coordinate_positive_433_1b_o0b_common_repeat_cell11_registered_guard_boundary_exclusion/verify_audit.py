#!/usr/bin/env python3
"""Hostile controls for the cell-11 registered-guard boundary certificate."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_guard_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(boundary, replay, label):
    try:
        VERIFY.validate(boundary, replay, check_dag=False)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    boundary, replay = VERIFY.load_payloads()
    VERIFY.validate(boundary, replay, check_dag=False)
    mutation = copy.deepcopy(replay)
    mutation["source_point_count"] = 159
    reject(boundary, mutation, "point census")
    mutation = copy.deepcopy(replay)
    mutation["rows"][0]["point_rows"].pop()
    reject(boundary, mutation, "point coverage")
    mutation = copy.deepcopy(replay)
    mutation["rows"][0]["point_rows"][0]["missing_product"] += 1
    reject(boundary, mutation, "common reconstruction")
    mutation = copy.deepcopy(replay)
    mutation["rows"][0]["point_rows"][0]["endpoint_roots"] = [
        {"value": 0, "multiplicity": 1}
    ]
    reject(boundary, mutation, "endpoint completeness")
    mutation = copy.deepcopy(replay)
    mutation["colored_candidate_count"] = 1
    reject(boundary, mutation, "candidate count")
    mutation = copy.deepcopy(boundary)
    source_point = next(
        point
        for root_row in mutation["rows"][0]["root_rows"]
        for point in root_row["source_points"]
        if point.get("guarded")
    )
    source_point["guarded"] = False
    reject(mutation, replay, "guarded source custody")
    print("PASS repeated-BC cell11 registered-guard hostile audit: 6/6")


if __name__ == "__main__":
    main()
