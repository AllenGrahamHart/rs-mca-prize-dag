#!/usr/bin/env python3
"""Independent ordered-negacyclic audit of the profile-(1,8) census."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    spec = importlib.util.spec_from_file_location("primary", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    pin = json.loads((HERE / "source_pin.json").read_text())
    source = primary.ROOT / pin["audit_census_file"]
    with tempfile.TemporaryDirectory() as temporary:
        binary = primary.compile_binary(source, Path(temporary))
        rows = []
        for template in range(11):
            completed = subprocess.run(
                [str(binary), str(template)],
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            rows.append(json.loads(completed.stdout))
    assert primary.summarize(rows) == primary.EXPECTED
    assert sum(int(row["supports"]) for row in rows) == 3_411_364
    assert sum(int(row["vectors"]) for row in rows) == 218_327_296
    assert sum(int(row["profile_18"]) for row in rows) == 17_144
    assert max(int(row["maximum_m3"]) for row in rows) == 1_356
    print(
        "E1_N256_S16_E33_PROFILE_18_LIGHT_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "ordered_negacyclic vectors=218327296 profile=17144 m3=1356"
    )


if __name__ == "__main__":
    main()
