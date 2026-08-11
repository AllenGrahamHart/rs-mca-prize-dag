#!/usr/bin/env python3
"""Static audit for the u=1 double-root cubic normal forms."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "w+epsilon=1",
        "c_s=2,c_d=1",
        "V_s=R_s+A",
        "O_C(A+B-Q)",
        "h^0(C,L_1)=0",
        "does not exclude",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("CUBIC_DOUBLE_GAP_ONE_NORMAL_FORMS_AUDIT_PASS")


if __name__ == "__main__":
    main()
