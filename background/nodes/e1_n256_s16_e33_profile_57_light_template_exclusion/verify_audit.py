#!/usr/bin/env python3
"""Audit the independent E=33 profile-(5,7) census packets."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    spec = importlib.util.spec_from_file_location("primary", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    pin = json.loads((HERE / "source_pin.json").read_text())
    census_source = primary.ROOT / pin["census_file"]
    audit_source = primary.ROOT / pin["audit_file"]
    assert hashlib.sha256(census_source.read_bytes()).hexdigest() != hashlib.sha256(
        audit_source.read_bytes()
    ).hexdigest()
    assert audit_source.name not in census_source.read_text()
    assert census_source.name not in audit_source.read_text()
    census_packet = json.loads((primary.ROOT / pin["census_result_file"]).read_text())
    audit_packet = json.loads((primary.ROOT / pin["audit_result_file"]).read_text())
    census_rows, audit_rows = primary.check_packets(census_packet, audit_packet)
    assert all(
        int(left["profile_57"]) == int(right["profile_57"])
        for left, right in zip(census_rows, audit_rows)
    )
    print(
        "E1_N256_S16_E33_PROFILE_57_LIGHT_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "engines=2 templates=100 vectors=1984793600 m3=1758/1416"
    )


if __name__ == "__main__":
    main()
