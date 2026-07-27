#!/usr/bin/env python3
"""Repartitioning audit for the E33 profile-(4,5,1) quotient census."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    spec = importlib.util.spec_from_file_location("primary", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    pin = json.loads((HERE / "source_pin.json").read_text())
    with tempfile.TemporaryDirectory() as temporary:
        binary = primary.compile_binary(Path(temporary), pin)
        rows = primary.run_census(binary, 7)
    primary.check_rows(rows, 7)
    assert sum(int(row["tested"]) for row in rows if row["order"] == 128) == 5_421_301
    assert sum(int(row["tested"]) for row in rows if row["order"] == 64) == 3_086_861
    assert max(int(row["best"]) for row in rows if row["order"] == 128) == 1732
    assert max(int(row["best"]) for row in rows if row["order"] == 64) == 1670
    print(
        "E1_N256_S16_E33_PROFILE_451_QUOTIENT_EXCLUSION_AUDIT_PASS "
        "repartition=7 order128=5421301/1732 order64=3086861/1670"
    )


if __name__ == "__main__":
    main()
