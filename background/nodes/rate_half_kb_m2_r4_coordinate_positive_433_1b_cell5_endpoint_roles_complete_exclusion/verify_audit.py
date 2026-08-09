#!/usr/bin/env python3
"""Hostile mutations for the cell-5 endpoint rootlessness certificate."""

import copy
import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("cell5_endpoint_verify", VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(verifier, pilot, replay, root, kernel):
    try:
        verifier.validate(pilot, replay, root, kernel)
    except RuntimeError:
        return True
    return False


def main():
    verifier = load_verifier()
    pilot = verifier.load("pilot")
    replay = verifier.load("replay")
    root = verifier.load("root")
    kernel = json.loads(verifier.KERNEL.read_text())
    verifier.validate(pilot, replay, root, kernel)

    dropped = copy.deepcopy(root)
    dropped["rows"].pop()
    if not rejected(verifier, pilot, replay, dropped, kernel):
        raise RuntimeError("dropped eliminant accepted")

    rooted = copy.deepcopy(root)
    rooted["rows"][0]["root_gcd"] = [1, 1]
    rooted["rows"][0]["root_count"] = 1
    if not rejected(verifier, pilot, replay, rooted, kernel):
        raise RuntimeError("nontrivial root gcd accepted")

    lifted = copy.deepcopy(replay)
    lifted["rows"][0]["r_root_count"] = 1
    lifted["rows"][0]["r_roots"] = [0]
    if not rejected(verifier, pilot, lifted, root, kernel):
        raise RuntimeError("replay root accepted")

    divergent = copy.deepcopy(kernel)
    divergent["rows"][0]["kernel"][0]["sha256"] = "0" * 64
    if not rejected(verifier, pilot, replay, root, divergent):
        raise RuntimeError("sign-dependent kernel accepted")

    print("PASS cell-5 endpoint hostile audit: 4/4 mutations rejected")


if __name__ == "__main__":
    main()
