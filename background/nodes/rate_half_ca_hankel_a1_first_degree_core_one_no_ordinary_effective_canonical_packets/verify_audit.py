#!/usr/bin/env python3
"""Static audit for the no-ordinary effective canonical packets."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "H_2:=Z_c-E_u",
        "O_C(H_2)",
        "(2n-m)/3>=0",
        "proper subdivisor",
        "does not exclude",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("NO_ORDINARY_CANONICAL_PACKETS_AUDIT_PASS")


if __name__ == "__main__":
    main()
