#!/usr/bin/env python3
"""Hostile controls for the cell-11 symmetric tower certificate."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_tower_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(function, payload, label):
    try:
        function(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    symmetric = VERIFY.load("symmetric_result")
    two = VERIFY.load("two_result")
    chart = VERIFY.load("chart_result")
    VERIFY.validate_symmetric(symmetric); VERIFY.validate_two(two); VERIFY.validate_chart(chart)
    mutation = copy.deepcopy(symmetric); mutation["rows"].pop()
    reject(VERIFY.validate_symmetric, mutation, "coverage")
    mutation = copy.deepcopy(symmetric); mutation["rows"][0]["full_dimension"] = 0
    reject(VERIFY.validate_symmetric, mutation, "dimension")
    mutation = copy.deepcopy(symmetric); mutation["rows"][0]["ordered_lift_output"] += "b2"
    reject(VERIFY.validate_symmetric, mutation, "lift")
    mutation = copy.deepcopy(two); mutation["rows"][0]["full_generators_mod_two_relation"][2] = "x"
    reject(VERIFY.validate_two, mutation, "containment")
    mutation = copy.deepcopy(two); mutation["rows"][1]["generic_extension_degree"] = 6
    reject(VERIFY.validate_two, mutation, "degree")
    mutation = copy.deepcopy(chart); mutation["rows"][0]["status"] = "ERROR"
    reject(VERIFY.validate_chart, mutation, "chart unit")
    print("PASS repeated-BC cell11 symmetric tower hostile audit: 6/6")


if __name__ == "__main__":
    main()
