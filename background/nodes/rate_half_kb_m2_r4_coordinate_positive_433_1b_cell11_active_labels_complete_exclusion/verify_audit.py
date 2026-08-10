#!/usr/bin/env python3
"""Hostile mutations for the cell-11 active-label aggregate."""

import importlib.util
from pathlib import Path

NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("cell11_active_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(verifier, owners, statuses):
    try:
        verifier.validate(owners, statuses)
    except RuntimeError:
        return True
    return False


def main():
    verifier = load_verifier()
    owners = dict(verifier.OWNERS)
    statuses = verifier.load_statuses()
    verifier.validate(owners, statuses)

    identifier = next(iter(owners))
    dropped = dict(owners)
    dropped[identifier] = dropped[identifier][1:]
    if not rejected(verifier, dropped, statuses):
        raise RuntimeError("dropped representative accepted")

    duplicate = dict(owners)
    duplicate[identifier] = duplicate[identifier] + (duplicate[identifier][0],)
    if not rejected(verifier, duplicate, statuses):
        raise RuntimeError("duplicate representative accepted")

    demoted = dict(statuses)
    demoted[identifier] = "SUPPORTED"
    if not rejected(verifier, owners, demoted):
        raise RuntimeError("demoted dependency accepted")

    print("PASS cell-11 active-label hostile audit: 3/3 mutations rejected")


if __name__ == "__main__":
    main()
