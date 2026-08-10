#!/usr/bin/env python3
"""Hostile coverage audit for the positive 433-1b raw workboard."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("raw_workboard_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(call, label):
    try:
        call()
    except RuntimeError:
        return
    raise RuntimeError(f"hostile mutation accepted: {label}")


def main():
    verifier = load_verifier()
    statuses = {identifier: "PROVED" for identifier in verifier.PARENTS}
    groups = {identifier: set(cells)
              for identifier, cells in verifier.ROLE_GROUPS.items()}
    verifier.validate(statuses, groups)

    for identifier in verifier.PARENTS:
        mutated = dict(statuses)
        mutated[identifier] = "SUPPORTED"
        rejected(lambda m=mutated: verifier.validate(m, groups),
                 f"demoted {identifier}")

    owner0 = next(identifier for identifier, cells in groups.items()
                  if cells == {0})
    owner14 = next(identifier for identifier, cells in groups.items()
                   if cells == {14})

    missing = {identifier: set(cells) for identifier, cells in groups.items()}
    missing[owner14] = set()
    rejected(lambda: verifier.validate(statuses, missing), "missing cell 14")

    duplicate = {identifier: set(cells) for identifier, cells in groups.items()}
    duplicate[owner14] = {0}
    rejected(lambda: verifier.validate(statuses, duplicate), "duplicate cell 0")

    extra = {identifier: set(cells) for identifier, cells in groups.items()}
    extra[owner0] = {0, 15}
    rejected(lambda: verifier.validate(statuses, extra), "extra cell 15")

    omitted_owner = {identifier: set(cells) for identifier, cells in groups.items()
                     if identifier != owner14}
    rejected(lambda: verifier.validate(statuses, omitted_owner), "missing owner")
    print("PASS raw workboard hostile audit: parent and coverage mutations rejected")


if __name__ == "__main__":
    main()
