#!/usr/bin/env python3
"""Hostile controls for the uncolored DF exclusion."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("df_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(values, label):
    try:
        VERIFY.validate(*values)
    except (RuntimeError, KeyError, ValueError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    baseline = VERIFY.load_payloads()
    VERIFY.validate(*baseline)
    mutation = list(copy.deepcopy(baseline))
    mutation[0]["rows"].pop()
    reject(mutation, "lost case")
    mutation = list(copy.deepcopy(baseline))
    mutation[0]["rows"][0]["q_values"].pop()
    reject(mutation, "q cover")
    mutation = list(copy.deepcopy(baseline))
    mutation[0]["rows"][0]["fibers"][0]["status"] = "EMPTY_ENDPOINT_FIBERS"
    reject(mutation, "fiber status")
    mutation = list(copy.deepcopy(baseline))
    endpoint = next(item for row in mutation[0]["rows"]
                    for fiber in row["fibers"]
                    for item in fiber.get("endpoint_rows", []))
    endpoint["gcd_degree"] = 1
    reject(mutation, "residual gcd")
    print("PASS uncolored DF hostile audit: 4/4")


if __name__ == "__main__":
    main()
