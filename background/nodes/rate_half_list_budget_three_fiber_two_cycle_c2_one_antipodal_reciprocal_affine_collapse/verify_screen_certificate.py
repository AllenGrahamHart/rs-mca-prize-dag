"""Fail-closed registration wrapper for the reciprocal-affine no-hit screen.

The existing 2026-07-21 maintainer ruling accepts remote no-hit screens as
PROVED evidence when their launcher and banked result are hash-pinned and a
local deterministic coverage checker passes. Original Modal app:
ap-Ifv7cgmA0WCon3SfgP1aSo.
"""

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "experiments/prize_resolution"

PINS = {
    "rate_half_list_c2_reciprocal_affine_torsion_modal.py":
        "4d28013ab06a85505b3bff2da137c12158bb08f6e49ef68e4a5bdbd5528457dd",
    "rate_half_list_c2_reciprocal_affine_torsion_result.json":
        "c4e4757c179e812d28f38e1efe1ce9a05326836083221f29e404b7c0787c6e91",
    "rate_half_list_c2_reciprocal_affine_torsion_check.py":
        "ac66817b4d5c185144a5fbc4f18ea26183424988148d43033c4f9185f3660a55",
}


def main() -> None:
    for name, want in PINS.items():
        got = hashlib.sha256((PACKET / name).read_bytes()).hexdigest()
        assert got == want, f"hash drift: {name} {got[:16]} != {want[:16]}"
    checker = PACKET / "rate_half_list_c2_reciprocal_affine_torsion_check.py"
    proc = subprocess.run(
        [sys.executable, str(checker)],
        capture_output=True,
        text=True,
        timeout=55,
        cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    tail = proc.stdout.strip().splitlines()[-1]
    assert "_PASS" in tail, tail
    print(f"C2_RECIPROCAL_AFFINE_SCREEN_CERTIFICATE_PASS pinned=3 checker={tail}")


if __name__ == "__main__":
    main()
