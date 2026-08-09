#!/usr/bin/env python3
"""Hostile status mutations for the cells 5-8 complete composition."""

import importlib.util
from pathlib import Path

NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("cells5_8_complete_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    verifier = load_verifier()
    statuses = {identifier: "PROVED" for identifier in verifier.PARENTS}
    verifier.validate(statuses)
    for identifier in verifier.PARENTS:
        mutated = dict(statuses)
        mutated[identifier] = "SUPPORTED"
        try:
            verifier.validate(mutated)
        except RuntimeError:
            continue
        raise RuntimeError(f"demoted parent accepted: {identifier}")
    print("PASS cells 5-8 complete hostile audit: 3/3 demotions rejected")


if __name__ == "__main__":
    main()
