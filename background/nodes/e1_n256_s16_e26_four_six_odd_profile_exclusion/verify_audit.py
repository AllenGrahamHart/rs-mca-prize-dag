#!/usr/bin/env python3
"""Independent structural audit of the E26 four-profile exclusion packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXP = ROOT / "experiments/prize_resolution"
MAXIMUM_NORM = 1139098407599461804511111865916270680930143333943822578584573946997885235216


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def flatten(rows: list[dict[str, object]]) -> list[int]:
    return [int(value) for row in sorted(rows, key=lambda item: int(item["batch"])) for value in row["norms"]]


def main() -> None:
    census = json.loads((EXP / "e26_four_six_odd_profile_census_result.json").read_text())
    production = sorted(census["production"], key=lambda row: int(row["template"]))
    audit = sorted(census["audit"], key=lambda row: int(row["template"]))
    assert len(production) == len(audit) == 1_234
    assert [strip_runtime(row) for row in production] == [strip_runtime(row) for row in audit]
    assert sum(int(row["vectors"]) for row in production) == 24_492_353_024
    assert sum(sum(int(value) for value in row["profile_counts"]) for row in production) == 78_848
    assert sum(sum(int(value) for value in row["above_cutoff"]) for row in production) == 74_614
    assert sum(sum(int(value) for value in row["full_above_cutoff"]) for row in production) == 45_408
    assert 74_614 - 45_408 == 29_206

    norms = json.loads((EXP / "e26_four_six_odd_profile_norm_result.json").read_text())
    flint_norms = flatten(norms["flint"])
    pari_norms = flatten(norms["pari"])
    assert flint_norms == pari_norms and len(flint_norms) == 45_408
    assert max(flint_norms) == MAXIMUM_NORM
    assert all(value < 2**250 for value in flint_norms)
    assert MAXIMUM_NORM < 2**250 < 2 * MAXIMUM_NORM

    production_source = (EXP / "e26_four_six_odd_profile_census.cpp").read_text()
    audit_source = (EXP / "e26_four_six_odd_profile_census_audit.cpp").read_text()
    norm_driver = (EXP / "e26_four_six_odd_profile_norm_modal.py").read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    print("E1_N256_S16_E26_FOUR_SIX_ODD_PROFILE_EXCLUSION_AUDIT_PASS templates=1234 vectors=24492353024 exceptions=74614 full=45408 max_bits=250 engines=4")


if __name__ == "__main__":
    main()
