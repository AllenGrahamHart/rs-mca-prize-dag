#!/usr/bin/env python3
"""Hostile controls for the cell-11 target-curve projection atlas."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_curve_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(function, payload, label):
    try:
        function(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    source = VERIFY.load("input_result")
    projection = VERIFY.load("projection_result")
    geometry = VERIFY.load("geometry_result")
    VERIFY.validate_input(source); VERIFY.validate_projection(projection); VERIFY.validate_geometry(geometry)
    mutation = copy.deepcopy(source); mutation["common_rows"].pop()
    reject(VERIFY.validate_input, mutation, "lost input row")
    mutation = copy.deepcopy(projection); mutation["rows"][0]["full_dimension"] = 0
    reject(VERIFY.validate_projection, mutation, "dimension")
    mutation = copy.deepcopy(projection); mutation["rows"][0]["elimination_output"] = "1"
    reject(VERIFY.validate_projection, mutation, "plane equation")
    mutation = copy.deepcopy(projection); mutation["source_sha256"] = "0" * 64
    reject(VERIFY.validate_projection, mutation, "source custody")
    mutation = copy.deepcopy(geometry); mutation["rows"][0]["symmetric_xy"] = "1"
    reject(VERIFY.validate_geometry, mutation, "symmetric reduction")
    mutation = copy.deepcopy(geometry); mutation["rows"][1]["basis_sizes"]["source_r"] += 1
    reject(VERIFY.validate_geometry, mutation, "basis census")
    print("PASS repeated-BC cell11 curve projection hostile audit: 6/6")


if __name__ == "__main__":
    main()
