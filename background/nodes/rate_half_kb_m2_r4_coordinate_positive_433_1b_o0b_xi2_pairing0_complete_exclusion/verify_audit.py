#!/usr/bin/env python3
"""Hostile parent-status audit for complete xi2/pairing0 exclusion."""

import importlib.util
from pathlib import Path


VERIFY = Path(__file__).resolve().parent / "verify.py"


def main():
    spec = importlib.util.spec_from_file_location("complete_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    statuses = {identifier: "PROVED" for identifier in verifier.PARENTS}
    verifier.validate(statuses)
    for identifier in verifier.PARENTS:
        mutation = dict(statuses)
        mutation[identifier] = "TARGET"
        try:
            verifier.validate(mutation)
        except RuntimeError:
            continue
        raise RuntimeError(f"demoted parent accepted: {identifier}")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_"
          "COMPLETE_AUDIT_PASS mutations=8/8")


if __name__ == "__main__":
    main()
