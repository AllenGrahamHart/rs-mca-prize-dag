"""Fail-closed registration wrapper for the HARMONIC Modal no-hit screen.

Maintainer ruling 2026-07-21 (w17-C1): remote no-hit screens carrying a local
coverage/hash certificate are accepted as PROVED evidence, and the screen's
launcher, checker, and banked result are hash-pinned here so the manifest's
fail-open scan covers them (closes the w17-C4 tracking gap). Modal app
ap-Js6Im9DeoBlc0di05YG2WE. Re-execution path: verify_screen_remote.py (registered as a
remote launcher; subject to the sub-5-minute wall-time self-auth rule).
"""
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "experiments/prize_resolution"

PINS = {
    "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_check.py": "f1e21d25aab834ee669b389fcfd83d935e1a3793eb6020035bbbaa5e2d326782",
    "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py": "7cd0b561634c83ccd4e5941748e63ecbaeeb1a7ff22c6053c9c0b61d90960cdb",
    "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.json": "4ddf28e4d69d1683bd52c14d946d730252ac996b3006721f4b6d39e966b51928",
}


def main() -> None:
    for name, want in PINS.items():
        got = hashlib.sha256((PACKET / name).read_bytes()).hexdigest()
        assert got == want, f"hash drift: {name} {got[:16]} != {want[:16]}"
    proc = subprocess.run(
        [sys.executable, str(PACKET / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_check.py")],
        capture_output=True, text=True, timeout=55, cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    tail = proc.stdout.strip().splitlines()[-1]
    assert "_PASS" in tail, tail
    print(f"HARMONIC_SCREEN_CERTIFICATE_PASS pinned=3 checker={tail}")


if __name__ == "__main__":
    main()
