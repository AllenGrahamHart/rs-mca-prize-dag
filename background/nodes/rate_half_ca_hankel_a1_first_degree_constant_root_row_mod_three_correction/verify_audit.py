#!/usr/bin/env python3
"""Static audit for the scalar root-row correction law."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "c_x+epsilon_x-t_x=0 mod 3",
        "z e=0 mod 3",
        "unsupported point",
        "I_E+2I_0",
        "necessary, not sufficient",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("ROOT_ROW_MOD_THREE_CORRECTION_AUDIT_PASS")


if __name__ == "__main__":
    main()
