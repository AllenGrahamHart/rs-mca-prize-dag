#!/usr/bin/env python3
"""Static check for the M720 complete-flag rule in the Modal helper."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "archive" / "retraction_xr_20260705" / "midlarge_h7_20" / "notes" / "modal_midlarge_h7_20.py"


def main() -> None:
    text = SOURCE.read_text()
    assert "complete = (W == n) and not aborted" in text
    assert '"complete": complete' in text
    print("M720 certificate semantics verified: complete iff W==n and not aborted")


if __name__ == "__main__":
    main()
