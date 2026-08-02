#!/usr/bin/env python3
"""Mutation and algebra audit for the 433-1b rank-drop exclusion."""

import copy
import importlib.util
import json

import sympy as sp


SPEC = importlib.util.spec_from_file_location(
    "rankdrop_complete_verify", __file__.replace("verify_audit.py", "verify.py")
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
    payload = json.loads(VERIFY.RESULT.read_text())
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["lanes"].pop()
    must_fail(mutation, "lost sign lane")

    mutation = copy.deepcopy(payload)
    mutation["lanes"][0]["rows"].pop()
    must_fail(mutation, "lost matching ledger")

    mutation = copy.deepcopy(payload)
    mutation["lanes"][0]["rows"][0]["unit"] = False
    must_fail(mutation, "lost unit ideal")

    mutation = copy.deepcopy(payload)
    mutation["status_counts"]["COMPLETE"] = 6719
    must_fail(mutation, "aggregate mismatch")

    d0, d1, d2, e0, e1, e2, y, z, w = sp.symbols(
        "d0 d1 d2 e0 e1 e2 y z w"
    )
    a2 = d0 + d1*w + d2*w**2
    a0 = e0 + e1*w + e2*w**2
    left = sp.resultant(a0-y*a2, a0.subs(w, -w)-z*a2.subs(w, -w), w)
    right = sp.resultant(a0-z*a2, a0.subs(w, -w)-y*a2.subs(w, -w), w)
    assert sp.expand(left-right) == 0
    assert len(tuple(VERIFY.pairings(range(6)))) == 15
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_COMPLETE_AUDIT_PASS "
        "mutations=4 resultant_symmetric=1 matchings=15"
    )


if __name__ == "__main__":
    main()
