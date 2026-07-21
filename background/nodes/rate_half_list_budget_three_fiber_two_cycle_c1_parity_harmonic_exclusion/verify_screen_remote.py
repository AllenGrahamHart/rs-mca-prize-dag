"""Remote launcher registration for the HARMONIC Modal screen (w17-C1 ruling).

Classified as a remote launcher by the manifest (hash-pinned, never replayed
in the local battery). Running it RE-LAUNCHES the full screen on Modal and
regenerates the banked result packet; the sub-5-minute wall-time self-auth
rule (maintainer ruling 2026-07-21) applies, and verify_screen_certificate.py
must be re-pinned afterwards. Original run: Modal app ap-Js6Im9DeoBlc0di05YG2WE, 0 hits.
"""
import subprocess
import sys
from pathlib import Path

import modal

ROOT = Path(__file__).resolve().parents[3]
LAUNCHER = ROOT / "experiments/prize_resolution" / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py"


def main() -> None:
    del modal  # imported for classification and to fail fast when unavailable
    raise SystemExit(subprocess.call([sys.executable, str(LAUNCHER)], cwd=ROOT))


if __name__ == "__main__":
    main()
