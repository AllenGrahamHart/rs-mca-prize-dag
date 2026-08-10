#!/usr/bin/env python3
"""Hostile controls for repeated-BC common saturation classification."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("saturation_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def rejected(payload, compiler, label):
    try:
        VERIFY.validate(payload, compiler)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(
        (VERIFY.EXPERIMENTS / VERIFY.FILES["result"][0]).read_text()
    )
    compiler = json.loads(
        (VERIFY.EXPERIMENTS / VERIFY.FILES["compiler_result"][0]).read_text()
    )
    VERIFY.validate(payload, compiler)

    mutation = copy.deepcopy(payload)
    mutation["rows"].pop()
    rejected(mutation, compiler, "lost case")

    mutation = copy.deepcopy(payload)
    mutation["rows"][0]["full_unit"] = not mutation["rows"][0]["full_unit"]
    rejected(mutation, compiler, "unit flip")

    survivor = next(index for index, row in enumerate(payload["rows"])
                    if not row["full_unit"])
    mutation = copy.deepcopy(payload)
    mutation["rows"][survivor]["stdout"] = mutation["rows"][survivor]["stdout"].replace(
        "DIM=1", "DIM=0").replace("DIM=2", "DIM=0")
    rejected(mutation, compiler, "dimension")

    mutation = copy.deepcopy(compiler)
    paired = next(row for row in mutation["rows"]
                  if row["mode"] == "stripped" and row["cell"] == 2)
    paired["minor_summaries"][0]["sha256"] = "0" * 64
    rejected(payload, mutation, "duplicate-role digest")

    mutation = copy.deepcopy(payload)
    mutation["representative_cells"].pop()
    rejected(mutation, compiler, "representative census")
    print("PASS repeated-BC saturation hostile audit: 5/5")


if __name__ == "__main__":
    main()
