#!/usr/bin/env python3
"""Replay the AQB finite-deficit verifier used by the threshold accounting."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "nodes" / "aqb_averaged_quotient_box" / "verify.py"


def main() -> None:
    subprocess.run([sys.executable, str(VERIFY)], check=True)
    print("AQB amortization threshold accounting verified")


if __name__ == "__main__":
    main()
