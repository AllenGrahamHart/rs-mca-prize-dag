#!/usr/bin/env python3
"""Hostile controls for the uncolored guard-root atlas."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("roots_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(source, payload, label):
    try:
        VERIFY.validate(source, payload)
    except (RuntimeError, KeyError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    source = json.loads(VERIFY.SOURCE.read_text())
    payload = json.loads(VERIFY.RESULT.read_text())
    VERIFY.validate(source, payload)
    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    reject(source, mutation, "lost guard")
    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["roots"] = [1]
    mutation["rows"][0]["field_part_degree"] = 1
    mutation["rows"][0]["field_part_coefficients"] = [VERIFY.PRIME-1, 1]
    reject(source, mutation, "invented root")
    mutation = copy.deepcopy(payload)
    mutation["root_union"].pop()
    reject(source, mutation, "root union")
    mutation = copy.deepcopy(payload)
    key = next(iter(mutation["root_incidence"]))
    mutation["root_incidence"][key].pop()
    reject(source, mutation, "incidence")
    print("PASS uncolored guard-root hostile audit: 4/4")


if __name__ == "__main__":
    main()
