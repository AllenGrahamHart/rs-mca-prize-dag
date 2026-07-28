#!/usr/bin/env python3
"""Replay the independent E27 profile and light-router audit."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_DIR = Path(__file__).resolve().parent


def main() -> None:
    pin = json.loads((NODE_DIR / "source_pin.json").read_text())
    checker = ROOT / pin["independent_check_file"]
    assert hashlib.sha256(checker.read_bytes()).hexdigest() == pin["independent_check_file_sha256"]
    spec = importlib.util.spec_from_file_location("e27_profile_parity_probe_check", checker)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()

    statement = (NODE_DIR / "statement.md").read_text()
    audit = (NODE_DIR / "audit.md").read_text()
    assert "M_3=443" in statement and "exactly eight affine" in statement
    assert "Gaussian" in audit and "elimination" in audit and "15,624 supports" in audit
    print("E1_N256_S16_E27_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS independent=1")


if __name__ == "__main__":
    main()
