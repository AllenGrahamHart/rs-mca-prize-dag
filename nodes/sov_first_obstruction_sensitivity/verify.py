#!/usr/bin/env python3
"""Replay the forced-root verifier, which includes the O_{h-1} sensitivity gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "nodes" / "sov_forced_root_recursion_algebra" / "verify.py"


def main() -> None:
    subprocess.run([sys.executable, str(TARGET)], check=True)
    print("SOV first-obstruction sensitivity covered by recursion verifier")


if __name__ == "__main__":
    main()
