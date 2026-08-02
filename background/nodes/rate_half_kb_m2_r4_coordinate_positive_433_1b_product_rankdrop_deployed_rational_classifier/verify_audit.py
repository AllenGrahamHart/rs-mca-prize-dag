#!/usr/bin/env python3
"""Mutation audit for the positive 433-1b rational classifier."""

import copy
import importlib.util
import json


SPEC = importlib.util.spec_from_file_location(
    "rational_verify", __file__.replace("verify_audit.py", "verify.py")
)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payload, label):
    try:
        VERIFY.verify_payload(payload)
    except (AssertionError, KeyError, RuntimeError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(VERIFY.RESULT.read_text())
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    must_fail(mutation, "lost finite row")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["factors"][0]["degree"] = 1
    must_fail(mutation, "invented linear factor")

    mutation = copy.deepcopy(payload)
    survivor = next(row for row in mutation["rows"] if row["rational_points"])
    survivor["rational_points"][0]["b"] += 1
    must_fail(mutation, "moved rational point")

    mutation = copy.deepcopy(payload)
    survivor = next(row for row in mutation["rows"] if row["rational_points"])
    survivor["rational_points"][0]["guard_nonzero"] = False
    must_fail(mutation, "lost guard")

    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_RATIONAL_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()
