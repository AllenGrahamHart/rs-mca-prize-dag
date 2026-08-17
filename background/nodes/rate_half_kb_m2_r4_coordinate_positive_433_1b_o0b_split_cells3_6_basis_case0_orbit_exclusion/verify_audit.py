#!/usr/bin/env python3
"""Hostile audit of the first basis-fed outside orbit exclusion."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load():
    spec = importlib.util.spec_from_file_location("case0_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load()


def expect_rejected(call, label):
    try:
        call()
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(MODULE.RESULT.read_text())
    mutation = deepcopy(payload)
    mutation["row"]["unit"] = False
    expect_rejected(lambda: MODULE.verify(mutation), "nonunit row")
    mutation = deepcopy(payload)
    mutation["row"]["stdout"] = mutation["row"]["stdout"].replace(
        "SAT=5,DIM=-1,SIZE=1", "SAT=5,DIM=3,SIZE=82"
    )
    expect_rejected(lambda: MODULE.verify(mutation), "changed unit guard")
    orbit = set(MODULE.EXPECTED_ORBIT)
    orbit.pop()
    expect_rejected(lambda: MODULE.verify(payload, orbit), "truncated orbit")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_CASE0_AUDIT_PASS "
          "mutations=3/3")


if __name__ == "__main__":
    main()
