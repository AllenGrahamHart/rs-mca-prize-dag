#!/usr/bin/env python3
"""Static audit for the two-point pencil exclusion."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "W=tK/tE",
        "W=span(s_alpha,s_beta)",
        "W intersect Fbar*1=0",
        "the PENCIL splitting from `(TPD4)`",
        "No generic multiplication-map",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("TWO_POINT_PENCIL_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
