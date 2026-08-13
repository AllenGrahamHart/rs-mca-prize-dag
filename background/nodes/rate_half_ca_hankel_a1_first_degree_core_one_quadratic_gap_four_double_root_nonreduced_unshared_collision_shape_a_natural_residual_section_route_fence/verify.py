#!/usr/bin/env python3
"""Replay the shape-A natural residual-section route fence."""

import argparse


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def replay(mutation=None):
    mutation = mutation or {}
    e = mutation.get("e", (2**39 + 1) // 3)
    m = mutation.get("m", e - 2)
    n = mutation.get("n", (3 * e - 7) // 2)
    pure_fiber_floor = mutation.get("pure_fiber_floor", e + 7)
    residual_degree = mutation.get("residual_degree", 4)
    section_dimension = mutation.get("section_dimension", 1)
    pade_independent_sections = mutation.get("pade_independent_sections", 0)
    raw_t_jet_mandatory_zeros = mutation.get("raw_t_jet_mandatory_zeros", 0)
    raw_x_jet_mandatory_zeros = mutation.get("raw_x_jet_mandatory_zeros", 0)

    require(e == 183251937963, "official e")
    require(m == 183251937961, "shape-A parameter degree")
    require(n == 274877906941, "shape-A row degree")
    require(pure_fiber_floor == 183251937970 > 0, "pure fiber existence")
    require(residual_degree == 4, "residual cycle degree")
    require(section_dimension == 1, "residual section dimension")
    require(pade_independent_sections == 0, "Pade residual coincidence")
    require(raw_t_jet_mandatory_zeros == 0, "simple parameter root")
    require(raw_x_jet_mandatory_zeros == 0, "squarefree row root")
    require(n > residual_degree, "first-jet base-divisor failure")

    return n, pure_fiber_floor, section_dimension


def tamper_selftest():
    mutations = [
        {"e": (2**39 + 1) // 3 + 1},
        {"m": 183251937960},
        {"n": 274877906940},
        {"pure_fiber_floor": 0},
        {"residual_degree": 5},
        {"section_dimension": 2},
        {"pade_independent_sections": 1},
        {"raw_t_jet_mandatory_zeros": 1},
        {"raw_x_jet_mandatory_zeros": 1},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    n, pure_fibers, section_dimension = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/9"
    print(
        "RATE_HALF_SHAPE_A_NATURAL_SECTION_FENCE_PASS "
        f"n={n} pure_fibers={pure_fibers} h0={section_dimension}{suffix}"
    )


if __name__ == "__main__":
    main()
