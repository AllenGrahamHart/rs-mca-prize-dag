#!/usr/bin/env python3
"""Cross-audit the cell-9 105-label composition."""

import copy
import importlib.util
from pathlib import Path

NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell9_complete", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def rejected(callback, message):
    try:
        callback()
    except RuntimeError:
        return
    raise RuntimeError(message)


def main():
    statuses = VERIFY.load_statuses()
    result = VERIFY.validate(VERIFY.OWNERS, statuses)
    hostile_owners = copy.deepcopy(VERIFY.OWNERS)
    key = next(iter(hostile_owners))
    hostile_owners[key] = hostile_owners[key][1:]
    rejected(
        lambda: VERIFY.validate(hostile_owners, statuses),
        "missing representative mutation survived",
    )
    hostile_statuses = dict(statuses)
    hostile_statuses[VERIFY.ENDPOINT] = "TARGET"
    rejected(
        lambda: VERIFY.validate(VERIFY.OWNERS, hostile_statuses),
        "dependency-status mutation survived",
    )
    print(
        "PASS cell-9 complete exclusion cross-audit: "
        f"owners={result['owners']} orbits={result['orbits']} "
        "mutations=2/2"
    )


if __name__ == "__main__":
    main()
