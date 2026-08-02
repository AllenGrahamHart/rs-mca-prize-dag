#!/usr/bin/env python3
"""Mutation controls for the positive 433-1b/O0a signed atlas."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("signed_atlas_verify",
                                              NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(atlas, orbits, lanes, defect, label):
    try:
        atlas.validate(orbits, lanes, defect)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    atlas = VERIFY.load_atlas()
    orbits, lanes, defect = atlas.verify()

    must_fail(atlas, orbits[:-1], lanes, defect, "lost orbit")

    mutation = copy.deepcopy(lanes)
    mutation.pop((-1, -1))
    must_fail(atlas, orbits, mutation, defect, "lost lane")

    mutation = copy.deepcopy(lanes)
    mutation[(1, 1)] = mutation[(1, 1)][:-1]
    must_fail(atlas, orbits, mutation, defect, "lost record")

    mutation = dict(defect)
    mutation["total"] = 2
    must_fail(atlas, orbits, lanes, mutation, "defect")
    print("positive 433-1b/O0a signed-edge atlas audit verified")


if __name__ == "__main__":
    main()
