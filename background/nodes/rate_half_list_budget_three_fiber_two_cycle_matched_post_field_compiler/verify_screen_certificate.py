"""Fail-closed registration wrapper for the HARMONIC_TOP Modal no-hit screen.

Maintainer ruling 2026-07-21 (w17-C1): remote no-hit screens carrying a local
coverage/hash certificate are accepted as PROVED evidence, and the screen's
launcher, checker, and banked result are hash-pinned here so the manifest's
fail-open scan covers them (closes the w17-C4 tracking gap). Modal app
ap-PVTrzkKlh4j1B6qDmGU1Wf. Re-execution path: verify_screen_remote.py (registered as a
remote launcher; subject to the sub-5-minute wall-time self-auth rule).
"""
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "experiments/prize_resolution"

PINS = {
    "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_check.py": "20d31d4eaae9fe6a17aaaf4d394cacd3681ddbdd59068fef7044ce40aa88d0a2",
    "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_modal.py": "a3d73e4135acb558dbfac26c24ca27bfcff543f07f2ada49605e481d15dcab64",
    "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_result.json": "eb4abfed366940680403906877553802c894eb0c51c8fa60c46ff0e5a0c322cc",
}


def main() -> None:
    for name, want in PINS.items():
        got = hashlib.sha256((PACKET / name).read_bytes()).hexdigest()
        assert got == want, f"hash drift: {name} {got[:16]} != {want[:16]}"
    proc = subprocess.run(
        [sys.executable, str(PACKET / "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_check.py")],
        capture_output=True, text=True, timeout=55, cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    tail = proc.stdout.strip().splitlines()[-1]
    assert "_PASS" in tail, tail
    print(f"HARMONIC_TOP_SCREEN_CERTIFICATE_PASS pinned=3 checker={tail}")


if __name__ == "__main__":
    main()
