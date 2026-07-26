#!/usr/bin/env python3
"""Primary replay for the WCL (4,9) inversion-symmetric exclusion."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / "experiments/prize_resolution/check_wcl49_inversion_symmetric_divisibility.py"
RESULT = ROOT / "experiments/prize_resolution/wcl49_inversion_symmetric_divisibility_result.json"

saved_argv = sys.argv
try:
    sys.argv = [str(CHECKER), str(RESULT)]
    runpy.run_path(str(CHECKER), run_name="__main__")
finally:
    sys.argv = saved_argv

print("DLI_WCL_ELL4_WEIGHT9_INVERSION_SYMMETRIC_EXCLUSION_VERIFY_PASS")
