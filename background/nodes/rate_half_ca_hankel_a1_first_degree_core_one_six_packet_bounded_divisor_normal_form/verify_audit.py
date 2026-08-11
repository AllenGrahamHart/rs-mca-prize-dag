#!/usr/bin/env python3
"""Static audit for the six-packet bounded-divisor leaf."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "D=P_* E_(c-2)",
        "N_F(U,V;x_*)=P_* C_(c+1)",
        "O_C(Z_c-R_0-E_u)",
        "does not assert",
        "signed in five packets",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("SIX_PACKET_BOUNDED_DIVISOR_AUDIT_PASS")


if __name__ == "__main__":
    main()
