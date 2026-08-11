#!/usr/bin/env python3
"""Static audit for the core-free bounded-divisor normal form."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "D_reg=P_1P_2 L_0^(2I_0) E_(1-I_0)",
        "`C_1,C_2` are not both zero",
        "O_C(Z_1+Z_2-R_0-E_1)",
        "does not assert",
        "signed and is not declared effective",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("CORE_FREE_BOUNDED_DIVISOR_AUDIT_PASS")


if __name__ == "__main__":
    main()
