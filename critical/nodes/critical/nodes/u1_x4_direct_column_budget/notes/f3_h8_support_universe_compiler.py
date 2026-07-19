#!/usr/bin/env python3
"""Compile exact h=8 n=64 support-universe bookkeeping.

This is a combinatorial audit for the remaining h=8 residual.  It does not
enumerate supports or run an x83 search; it verifies the exact sizes of the
anchored universe, the antipodal subfamily, and the paid-branch local shell
workloads already used by the x83 certificates.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"

N = 64
SUPPORT_SIZE = 16
PAID_X83_SUPPORTS = 7

EXPECTED = {
    "anchored_supports": 122131734269895,
    "anchored_antipodal_supports": 2629575,
    "anchored_nonantipodal_supports": 122131731640320,
    "blind_left_records": 553270671,
    "blind_right_records": 3872894697,
    "shell_workloads": {
        0: 7,
        1: 5376,
        2: 947520,
        3: 67800320,
        4: 2478949200,
    },
    "shell_le_3_workload": 68753223,
}


def shell_workload(radius: int) -> int:
    """Multiplicity workload around the seven paid h=8 square-lift supports."""
    return PAID_X83_SUPPORTS * math.comb(SUPPORT_SIZE, radius) * math.comb(
        N - SUPPORT_SIZE, radius
    )


def require_radius3_certificate(name: str) -> None:
    cert = json.loads((NOTES / name).read_text())
    expected_processed = shell_workload(3)
    expected = {
        "radius": 3,
        "processed": expected_processed,
        "full_zero": 0,
        "complete": True,
        "errors": [],
    }
    for key, value in expected.items():
        if cert.get(key) != value:
            raise AssertionError((name, key, cert.get(key), value))
    if cert.get("jobs_completed") != cert.get("jobs_expected"):
        raise AssertionError(
            (name, "jobs", cert.get("jobs_completed"), cert.get("jobs_expected"))
        )


def main() -> None:
    anchored_supports = math.comb(N - 1, SUPPORT_SIZE - 1)
    anchored_antipodal = math.comb(N // 2 - 1, SUPPORT_SIZE // 2 - 1)
    anchored_nonantipodal = anchored_supports - anchored_antipodal
    blind_left = math.comb(N - 1, SUPPORT_SIZE // 2 - 1)
    blind_right = math.comb(N - 1, SUPPORT_SIZE // 2)
    shell_rows = {radius: shell_workload(radius) for radius in range(5)}
    shell_le_3 = sum(shell_rows[radius] for radius in range(4))

    actual = {
        "anchored_supports": anchored_supports,
        "anchored_antipodal_supports": anchored_antipodal,
        "anchored_nonantipodal_supports": anchored_nonantipodal,
        "blind_left_records": blind_left,
        "blind_right_records": blind_right,
        "shell_workloads": shell_rows,
        "shell_le_3_workload": shell_le_3,
    }
    if actual != EXPECTED:
        raise AssertionError((actual, EXPECTED))

    require_radius3_certificate("f3_h8_n64_x83_radius3_shell_certificate_p4289.json")
    require_radius3_certificate("f3_h8_n64_x83_radius3_shell_certificate.json")

    radius3_fraction = Fraction(shell_rows[3], anchored_nonantipodal)
    shell_le_3_fraction = Fraction(shell_le_3, anchored_nonantipodal)
    blind_left_gib = blind_left * 32 / (1024**3)

    print("h=8 n=64 support universe compiler")
    print(f"anchored 16-supports with 0: {anchored_supports}")
    print(f"anchored antipodal supports: {anchored_antipodal}")
    print(f"anchored non-antipodal supports: {anchored_nonantipodal}")
    print(f"blind left records: {blind_left} (~{blind_left_gib:.2f} GiB at 32 bytes)")
    print(f"blind right records: {blind_right}")
    for radius in range(5):
        print(f"paid-branch radius {radius} workload: {shell_rows[radius]}")
    print(
        "paid-branch radius <=3 workload: "
        f"{shell_le_3} "
        f"({float(shell_le_3_fraction * 1_000_000):.6f} ppm of non-antipodal universe)"
    )
    print(
        "paid-branch radius 3 workload: "
        f"{shell_rows[3]} "
        f"({float(radius3_fraction * 1_000_000):.6f} ppm of non-antipodal universe)"
    )
    print("H8_SUPPORT_UNIVERSE_COMPILER_PASS")


if __name__ == "__main__":
    main()
