#!/usr/bin/env python3
"""Hostile mutation controls for the positive 433-1b/O0b atlas."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("atlas_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(atlas, atlases, lanes, defects, label):
    try:
        atlas.validate(atlases, lanes, defects)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    atlas = VERIFY.load_atlas()
    atlases, lanes, defects = atlas.verify()

    mutation = copy.deepcopy(atlases)
    mutation.pop("SDF")
    must_fail(atlas, mutation, lanes, defects, "lost stratum")

    mutation = copy.deepcopy(lanes)
    mutation.pop(next(iter(mutation)))
    must_fail(atlas, atlases, mutation, defects, "lost lane")

    mutation = copy.deepcopy(lanes)
    key = next(iter(mutation))
    mutation[key] = mutation[key][:-1]
    must_fail(atlas, atlases, mutation, defects, "lost target record")

    mutation = copy.deepcopy(defects)
    mutation["SBC"]["total"] = 1
    must_fail(atlas, atlases, lanes, mutation, "defect total")
    print("PASS positive 433-1b/O0b signed-edge atlas hostile audit: 4/4")


if __name__ == "__main__":
    main()
