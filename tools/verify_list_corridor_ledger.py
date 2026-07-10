#!/usr/bin/env python3
"""Verify the list_corridor_ledger packet.

The ledger comparison is intentionally small:

  required gain = W_list - 1
  available gain = the exact scale-free floor gain from cap_envelope_parameter_sweep

The verifier also runs the underlying cap-envelope sweep verifier, because that
packet owns the exact big-int proof that the quoted gains are valid.
"""

from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "critical" / "nodes" / "list_corridor_ledger" / "list_corridor_ledger_table.json"
WIDTHS = ROOT / "critical" / "nodes" / "list_corridor_widths" / "list_corridor_widths_table.json"
SWEEP = ROOT / "critical" / "nodes" / "cap_envelope_parameter_sweep" / "notes" / "verify_sweep.py"
TOL = 5e-12


EXPECTED_GAINS = {
    "1/4": Fraction(81, 128),
    "1/8": Fraction(203, 2048),
    "1/16": Fraction(3, 8),
}


def close(a: float, b: float) -> bool:
    return abs(a - b) <= TOL


def run_sweep() -> None:
    proc = subprocess.run(
        [sys.executable, str(SWEEP)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        raise SystemExit("underlying cap-envelope sweep verifier failed")


def main() -> None:
    errors: list[str] = []
    ledger = json.loads(LEDGER.read_text())
    widths = json.loads(WIDTHS.read_text())

    if ledger.get("node") != "list_corridor_ledger":
        errors.append("ledger node mismatch")
    if ledger.get("units") != widths.get("units"):
        errors.append("ledger and width units differ")

    width_by_rate = {row["rate"]: row for row in widths["rows"]}
    for row in ledger.get("rows", []):
        rate = row["rate"]
        if rate not in width_by_rate:
            errors.append(f"{rate}: no matching width row")
            continue
        w_list = float(width_by_rate[rate]["W_list"])
        required = w_list - 1.0
        gain = float(EXPECTED_GAINS[rate])
        margin = gain - required

        if not close(float(row["W_list"]), w_list):
            errors.append(f"{rate}: W_list mismatch")
        if not close(float(row["required_gain_W_list_minus_1"]), required):
            errors.append(f"{rate}: required gain mismatch")
        if row.get("sweep_gain_fraction") != f"{EXPECTED_GAINS[rate].numerator}/{EXPECTED_GAINS[rate].denominator}":
            errors.append(f"{rate}: sweep fraction mismatch")
        if not close(float(row["sweep_gain"]), gain):
            errors.append(f"{rate}: sweep gain mismatch")
        if not close(float(row["margin"]), margin):
            errors.append(f"{rate}: margin mismatch")
        if margin <= 0:
            errors.append(f"{rate}: non-positive margin")
        if row.get("verdict") != "PASS":
            errors.append(f"{rate}: verdict should be PASS")

    if errors:
        print("FAIL list_corridor_ledger")
        for err in errors:
            print(" -", err)
        raise SystemExit(1)

    run_sweep()
    print("PASS list_corridor_ledger")
    for row in ledger["rows"]:
        print(
            f"{row['rate']}: required={row['required_gain_W_list_minus_1']:.12f} "
            f"gain={row['sweep_gain']:.12f} margin={row['margin']:.12f}"
        )


if __name__ == "__main__":
    main()
