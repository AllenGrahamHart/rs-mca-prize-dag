#!/usr/bin/env python3
"""Hostile controls for cells 3/6 full-system transport."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("transport_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def rejected(call, label):
    try:
        call()
    except (RuntimeError, KeyError, IndexError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    transport = VERIFY.load_transport(); VERIFY.validate(transport)
    original = transport.COMMON_ROLE_SWAP
    transport.COMMON_ROLE_SWAP = (0, 1, 2, 3, 4)
    rejected(lambda: VERIFY.validate(transport), "cell map")
    transport.COMMON_ROLE_SWAP = original

    original = transport.OUTSIDE_RECORD_SWAP
    transport.OUTSIDE_RECORD_SWAP = (0, 1, 2, 3, 4, 5, 6)
    rejected(lambda: VERIFY.validate(transport), "record map")
    transport.OUTSIDE_RECORD_SWAP = original

    original = transport.OUTSIDE_MATCHINGS
    transport.OUTSIDE_MATCHINGS = original[:-1]
    rejected(lambda: VERIFY.validate(transport), "label cover")
    transport.OUTSIDE_MATCHINGS = original
    print("PASS repeated-BC cells3/6 transport hostile audit: 3/3")


if __name__ == "__main__":
    main()
