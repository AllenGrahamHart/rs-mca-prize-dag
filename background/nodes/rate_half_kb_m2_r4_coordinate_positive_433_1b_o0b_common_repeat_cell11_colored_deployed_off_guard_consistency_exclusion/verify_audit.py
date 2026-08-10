#!/usr/bin/env python3
"""Hostile controls for the colored cell-11 consistency verifier."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("colored_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)
RESULT = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_colored_consistency_result.json"
)
TOWER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)


def reject(mutation, label):
    payload = copy.deepcopy(VERIFY.load(RESULT))
    tower = VERIFY.load(TOWER)
    mutation(payload)
    try:
        VERIFY.validate_payload(payload, tower)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    reject(lambda value: value.__setitem__("source_tower_count", 7),
           "tower census")
    reject(lambda value: value["rows"][0].__setitem__("tower_valid", False),
           "tower validity")
    reject(lambda value: value["rows"][0]["rows"][1].__setitem__(
        "missing_record", "BE"), "record cover")
    reject(lambda value: value["rows"][0]["rows"][0].__setitem__(
        "determinant_zero", True), "zero determinant")
    reject(lambda value: value["rows"][0]["rows"][0][
        "base_field_roots"
    ][0].__setitem__("construction_guards_nonzero", True), "guard root")
    reject(lambda value: value.__setitem__("non_guard_root_occurrences", 1),
           "non-guard root census")
    reject(lambda value: value["rows"][0]["rows"][0].__setitem__(
        "status", "DEPLOYED_POINTWISE_BOUNDARY"), "status")
    print("PASS cell11 colored consistency hostile audit: 7/7")


if __name__ == "__main__":
    main()

