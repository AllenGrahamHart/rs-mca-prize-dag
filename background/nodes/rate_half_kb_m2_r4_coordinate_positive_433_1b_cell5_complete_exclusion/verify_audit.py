#!/usr/bin/env python3
"""Hostile mutations for the cell-5 complete-label composition."""

import importlib.util
from pathlib import Path

NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("cell5_complete_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(verifier, statuses, active, endpoint):
    try:
        verifier.validate(statuses, active, endpoint)
    except RuntimeError:
        return True
    return False


def main():
    verifier = load_verifier()
    statuses = verifier.load_statuses()
    active = {(xi, pairing) for xi in range(5) for pairing in range(15)}
    endpoint = {(xi, pairing) for xi in (5, 6) for pairing in range(15)}
    verifier.validate(statuses, active, endpoint)

    demoted = dict(statuses)
    demoted[verifier.ENDPOINT] = "SUPPORTED"
    if not rejected(verifier, demoted, active, endpoint):
        raise RuntimeError("demoted child accepted")

    dropped = set(endpoint)
    dropped.remove((6, 14))
    if not rejected(verifier, statuses, active, dropped):
        raise RuntimeError("missing endpoint label accepted")

    overlap = set(endpoint)
    overlap.remove((6, 14))
    overlap.add((4, 14))
    if not rejected(verifier, statuses, active, overlap):
        raise RuntimeError("overlapping child cover accepted")

    print("PASS cell-5 complete hostile audit: 3/3 mutations rejected")


if __name__ == "__main__":
    main()
