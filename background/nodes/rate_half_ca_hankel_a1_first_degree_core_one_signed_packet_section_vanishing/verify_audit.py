#!/usr/bin/env python3
"""Static audit for signed-packet section vanishing."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "P_3<V_*",
        "W intersect Fbar*1=0",
        "O(1-d)^3",
        "`P_3` and `R_0` are disjoint",
        "does not exclude",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("SIGNED_PACKET_SECTION_VANISHING_AUDIT_PASS")


if __name__ == "__main__":
    main()
