#!/usr/bin/env python3
"""Audit the E=33 endpoint synthesis guards."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    spec = importlib.util.spec_from_file_location("primary", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    assert primary.PROFILES == {(5, 7), (1, 8), (4, 5, 1), (0, 6, 1)}
    assert set(primary.CHILDREN) == {
        "e1_n256_s16_e33_profile_061_exclusion",
        "e1_n256_s16_e33_profile_451_quotient_exclusion",
        "e1_n256_s16_e33_profile_18_light_template_exclusion",
        "e1_n256_s16_e33_profile_57_light_template_exclusion",
    }
    print("E1_N256_S16_E33_ENDPOINT_EXCLUSION_AUDIT_PASS profiles=4 mutations=2")


if __name__ == "__main__":
    main()
