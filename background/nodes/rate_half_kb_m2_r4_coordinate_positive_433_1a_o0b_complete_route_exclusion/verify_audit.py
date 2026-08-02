#!/usr/bin/env python3
"""Mutation controls for the positive-route coverage verifier."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("positive_route_verify",
                                              NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(coverage, label):
    try:
        VERIFY.verify_coverage(coverage)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    coverage = VERIFY.COVERAGE
    VERIFY.verify_coverage(coverage)

    must_fail(coverage[:-1], "missing orbit")

    mutation = list(coverage)
    node_id, orbit, _, reps = mutation[0]
    mutation[0] = (node_id, orbit, 8, reps)
    must_fail(tuple(mutation), "raw-row total")

    mutation = list(coverage)
    node_id, orbit, rows, _ = mutation[1]
    mutation[1] = (node_id, orbit, rows, 1)
    must_fail(tuple(mutation), "representative total")

    mutation = list(coverage)
    node_id, _, rows, reps = mutation[8]
    mutation[8] = (node_id, (13,), rows, reps)
    must_fail(tuple(mutation), "duplicate cell")
    print("positive 433-1a route coverage audit verified")


if __name__ == "__main__":
    main()
