#!/usr/bin/env python3
"""Independent packet audit for the E32 profile-(4,7) exact norms."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
MAXIMUM_NORM = 119477984433218714943829098200259691143739376720677525742811917286342611458


def main() -> None:
    production = json.loads((NOTES / "e32_profile47_exact_norm_census_result.json").read_text())
    audit = json.loads((NOTES / "e32_profile47_exact_norm_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 148
    for left, right in zip(first, second):
        assert int(left["template"]) == int(right["template"])
        assert left["light"] == right["light"]
        assert int(left["full_conductor_profile_47"]) == int(right["full_conductor_profile_47"])
        assert int(left["norm_at_or_above_2_250"]) == int(right["norm_at_or_above_2_250"]) == 0
        assert int(left["maximum_norm"]) == int(right["maximum_norm"])
        assert left["maximum_witness"] == right["maximum_witness"]
    assert sum(int(row["full_conductor_profile_47"]) for row in first) == 60_148
    assert max(int(row["maximum_norm"]) for row in first) == MAXIMUM_NORM
    assert 15 * MAXIMUM_NORM < 2**250

    production_source = (NOTES / "e32_profile47_exact_norm_census.cpp").read_text()
    audit_source = (NOTES / "e32_profile47_exact_norm_audit.cpp").read_text()
    production_launcher = (NOTES / "e32_profile47_exact_norm_census_modal.py").read_text()
    audit_launcher = (NOTES / "e32_profile47_exact_norm_audit_modal.py").read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "python-flint" in production_launcher and "polresultant" not in production_launcher
    assert "pari-gp" in audit_launcher and "polresultant" in audit_launcher

    print(
        "E1_N256_S16_E32_PROFILE_47_EXACT_NORM_EXCLUSION_AUDIT_PASS "
        "engines=2 templates=148 full=60148 max_bits=247 above=0"
    )


if __name__ == "__main__":
    main()
