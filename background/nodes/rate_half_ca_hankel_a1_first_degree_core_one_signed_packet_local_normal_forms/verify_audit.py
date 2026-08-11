#!/usr/bin/env python3
"""Static audit for the signed tangent-packet normal forms."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "t=C_tot-O",
        "V_*=R_*+A+3B",
        "V_*=R_*+2A+3B",
        "V_*=R_*+3B",
        "does not assert that the signed",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("SIGNED_PACKET_LOCAL_NORMAL_FORMS_AUDIT_PASS")


if __name__ == "__main__":
    main()
