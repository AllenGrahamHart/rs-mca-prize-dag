"""Fail-closed registration wrapper for the ANTIINVARIANT Modal no-hit screen.

Maintainer ruling 2026-07-21 (w17-C1): remote no-hit screens carrying a local
coverage/hash certificate are accepted as PROVED evidence, and the screen's
launcher, checker, and banked result are hash-pinned here so the manifest's
fail-open scan covers them (closes the w17-C4 tracking gap). Modal app
ap-6KQ2mJjoE3Qkq7VaKqnxlZ. Re-execution path: verify_screen_remote.py (registered as a
remote launcher; subject to the sub-5-minute wall-time self-auth rule).
"""
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "experiments/prize_resolution"

PINS = {
    "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_check.py": "d2eafae074ba68e2bc4e6b36d81d34c97b72ee95b37a203de94a36df854add9c",
    "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_modal.py": "f3d2d6ef3c3af2f39289a8a18b174b84ef6dc3d5b23616acdb72abd38559dfff",
    "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_result.json": "901a60f0bdd583d96e0d397dc7a1c0a4de97253f2ee1dddfa222e30e4fd66bc3",
}


def main() -> None:
    for name, want in PINS.items():
        got = hashlib.sha256((PACKET / name).read_bytes()).hexdigest()
        assert got == want, f"hash drift: {name} {got[:16]} != {want[:16]}"
    proc = subprocess.run(
        [sys.executable, str(PACKET / "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_check.py")],
        capture_output=True, text=True, timeout=55, cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    tail = proc.stdout.strip().splitlines()[-1]
    assert "_PASS" in tail, tail
    print(f"ANTIINVARIANT_SCREEN_CERTIFICATE_PASS pinned=3 checker={tail}")


if __name__ == "__main__":
    main()
