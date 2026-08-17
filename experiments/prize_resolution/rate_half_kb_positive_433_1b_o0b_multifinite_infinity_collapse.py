#!/usr/bin/env python3
"""Verify the FFI/FIF infinity-pair leading-coefficient collapses."""

import hashlib
import importlib.util
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_compiler():
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    spec = importlib.util.spec_from_file_location("cached_outside_core", COMPILER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_pair_ledger():
    compiler = load_compiler()
    targets = ("b", "c", "d", "e", "f")
    records = tuple(
        compiler.edge(targets[left], targets[right], -1 if sign == 0 else sign)[0]
        for left, right, sign in compiler.EDGE_SPECS["S0"]
    )
    require(records == ("b*e", "c*f", "d*e", "-d*e", "d*f", "-d*f", "-e*f"),
            "S0 record ledger")
    residual = tuple(index for index in range(7) if index != 2)
    matching = tuple(compiler.pairings(range(6)))[0]
    record_pairs = tuple((residual[left], residual[right]) for left, right in matching)
    require(record_pairs == ((0, 1), (3, 4), (5, 6)),
            "xi2 pairing0 ledger")
    return records, record_pairs


def verify_collapses():
    d, e, f, z2, z5 = sp.symbols("d e f z2 z5")
    ffi_left = z5 + d * f * z2
    ffi_right = z5 + e * f * z2
    require(sp.expand(ffi_left - ffi_right - f * (d - e) * z2) == 0,
            "FFI q6 subtraction")
    fif_left = z5 + d * e * z2
    fif_right = z5 - d * f * z2
    require(sp.expand(fif_left - fif_right - d * (e + f) * z2) == 0,
            "FIF q5 subtraction")
    return {
        "FFI": ("f", "d-e"),
        "FIF": ("d", "e+f"),
    }


def verify_guards():
    compiler = load_compiler()
    packet = {
        "variables": ["t", "r", "c", "b"],
        "common_equations": ["t", "r", "c"],
        "kernel": ["1", "t", "r", "c", "b", "t+r", "t+c", "r+b"],
        "route_guards": [f"t+{index}" for index in range(16)],
        "rank_cofactors": [f"r+{index}" for index in range(6)],
    }
    compiled = compiler.compile_case((3, "S0", -1, -1, -1, 2, 0), packet)
    compact = {"".join(value.split()) for value in compiled["guards"]}
    require({"d", "f", "(d)^2-(e)^2", "(e)^2-(f)^2"} <= compact,
            "nonzero and square-distinct guards")
    return 4


def main():
    verify_pair_ledger()
    collapses = verify_collapses()
    guards = verify_guards()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_MULTIFINITE_INFINITY_COLLAPSE_PASS "
          f"masks={len(collapses)} guards={guards}")


if __name__ == "__main__":
    main()
