#!/usr/bin/env python3
"""Mutation audit for the positive 433-1b rank-drop classifier."""

import copy
import importlib.util
import json


SPEC = importlib.util.spec_from_file_location(
    "rankdrop_verify", __file__.replace("verify_audit.py", "verify.py")
)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payload, label):
    try:
        VERIFY.verify_payload(payload)
    except (KeyError, RuntimeError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(
        (VERIFY.EXPERIMENTS / VERIFY.FILES["common_result"][0]).read_text()
    )
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    must_fail(mutation, "lost root-sign row")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["minor_count"] = 44
    must_fail(mutation, "lost full minor")

    mutation = copy.deepcopy(payload)
    survivor = next(row for row in mutation["rows"] if row["cell"] == 14)
    survivor["dimension"] = 1
    must_fail(mutation, "positive-dimensional survivor")

    mutation = copy.deepcopy(payload)
    unit = next(row for row in mutation["rows"] if row["cell"] == 0)
    unit["unit"] = False
    must_fail(mutation, "lost unit certificate")

    assert len(tuple(__import__("itertools").combinations(range(10), 8))) == 45
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_COMMON_AUDIT_PASS "
        "mutations=4 determinant_count=45"
    )


if __name__ == "__main__":
    main()
