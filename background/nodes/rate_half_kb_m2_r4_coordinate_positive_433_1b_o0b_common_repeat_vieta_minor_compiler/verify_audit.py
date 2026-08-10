#!/usr/bin/env python3
"""Hostile controls for the repeated-BC common compiler."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("repeat_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payload, label):
    try:
        VERIFY.verify_payload(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(
        (VERIFY.EXPERIMENTS / VERIFY.FILES["result"][0]).read_text()
    )
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    must_fail(mutation, "lost case")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["minor_summaries"].pop()
    must_fail(mutation, "lost minor")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["matching"][0][0] = "LA"
    must_fail(mutation, "role partition")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["cell_orbits"][0] = [0, 1]
    must_fail(mutation, "cell orbit")

    mutation = copy.deepcopy(payload)
    mutation["summaries"]["stripped"]["-1"]["maximum_terms"] = 67
    must_fail(mutation, "aggregate summary")
    print("PASS repeated-BC common compiler hostile audit: 5/5")


if __name__ == "__main__":
    main()
