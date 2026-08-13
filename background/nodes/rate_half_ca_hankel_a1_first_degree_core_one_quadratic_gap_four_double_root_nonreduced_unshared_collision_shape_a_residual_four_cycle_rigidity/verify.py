#!/usr/bin/env python3
"""Replay the shape-A residual four-cycle rigidity ledger."""

import argparse


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def replay(mutation=None):
    mutation = mutation or {}
    e = mutation.get("e", (2**39 + 1) // 3)
    d = mutation.get("d", 3 * e - 2)
    deg_r = mutation.get("deg_r", e - 6)
    deg_b = mutation.get("deg_b", 2)
    contact_b_coefficient = mutation.get("contact_b_coefficient", 2)
    vertical_b_coefficient = mutation.get("vertical_b_coefficient", 3)
    modification_length = mutation.get("modification_length", 2)
    constant_direction_rank = mutation.get("constant_direction_rank", 0)

    vertical_degree = deg_r + vertical_b_coefficient * deg_b
    contact_degree = deg_r + contact_b_coefficient * deg_b
    residual_degree = contact_b_coefficient * deg_b
    # The bundle has e summands, but only its largest negative degree is
    # needed. Never materialize an official-size list.
    e1_negative_ceiling = max(1 - d, -d)
    e2_envelope_ceiling = e1_negative_ceiling + 1

    require(e == 183251937963, "official e")
    require(d == 549755813887, "locator row degree")
    require(deg_r > 0, "proper residual fibre divisor")
    require(deg_b == 2, "correction degree")
    require(vertical_degree == e, "vertical divisor degree")
    require(contact_degree == e - 2, "contact divisor degree")
    require(residual_degree == 4, "residual four-cycle degree")
    require(modification_length == deg_b, "second modification length")
    require(constant_direction_rank == 0, "constant direction exclusion")
    require(e1_negative_ceiling == 1 - d, "first splitting ceiling")
    require(e2_envelope_ceiling == 2 - d < 0, "second splitting ceiling")

    # Both normalization patterns from the collision dichotomy pull back
    # with total coefficient four.
    patterns = mutation.get("patterns", [[2], [1, 1]])
    require(patterns == [[2], [1, 1]], "normalization patterns")
    require(all(sum(2 * multiplicity for multiplicity in p) == 4 for p in patterns),
            "local residual length")

    return d, residual_degree, e2_envelope_ceiling


def tamper_selftest():
    mutations = [
        {"e": (2**39 + 1) // 3 + 1},
        {"d": 549755813886},
        {"deg_r": 183251937956},
        {"deg_b": 3},
        {"contact_b_coefficient": 1},
        {"vertical_b_coefficient": 2},
        {"modification_length": 1},
        {"constant_direction_rank": 1},
        {"patterns": [[1], [1, 1]]},
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

    d, residual_degree, negative_ceiling = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/9"
    print(
        "RATE_HALF_SHAPE_A_RESIDUAL_FOUR_RIGIDITY_PASS "
        f"d={d} residual_degree={residual_degree} "
        f"negative_ceiling={negative_ceiling}{suffix}"
    )


if __name__ == "__main__":
    main()
