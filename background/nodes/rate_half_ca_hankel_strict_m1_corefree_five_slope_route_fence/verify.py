#!/usr/bin/env python3
"""Hash-pin and replay the exact strict-m=1 locator/Hankel census."""

from hashlib import sha256
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_strict_m1_locator_lines.py"
EXPECTED = "b0f03a9b167857810aaab64cbfccec052dafa8b51ae0e34d117e247793faec02"


def main() -> None:
    assert sha256(SCRIPT.read_bytes()).hexdigest() == EXPECTED
    namespace = runpy.run_path(str(SCRIPT), run_name="rate_half_strict_m1_census")
    namespace["main"]()
    print("RATE_HALF_CA_HANKEL_STRICT_M1_COREFREE_FIVE_SLOPE_ROUTE_FENCE_PASS")


if __name__ == "__main__":
    main()
