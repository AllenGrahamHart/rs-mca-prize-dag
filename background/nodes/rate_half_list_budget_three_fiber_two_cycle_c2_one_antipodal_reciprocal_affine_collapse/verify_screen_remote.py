"""Remote launcher registration for the reciprocal-affine no-hit screen.

Classified as a remote launcher by the manifest and never replayed in the
local verifier battery. Re-running it spends Modal credit and requires the
banked packet hashes to be refreshed. Original run:
ap-Ifv7cgmA0WCon3SfgP1aSo, 4,495,442 moduli, zero hits.
"""

import subprocess
from pathlib import Path

import modal


ROOT = Path(__file__).resolve().parents[3]
LAUNCHER = (
    ROOT
    / "experiments/prize_resolution"
    / "rate_half_list_c2_reciprocal_affine_torsion_modal.py"
)


def main() -> None:
    del modal
    modal_bin = Path.home() / ".venvs/modal/bin/modal"
    raise SystemExit(
        subprocess.call([str(modal_bin), "run", str(LAUNCHER)], cwd=ROOT)
    )


if __name__ == "__main__":
    main()
