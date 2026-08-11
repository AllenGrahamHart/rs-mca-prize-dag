#!/usr/bin/env python3
"""Static audit for the core-one two-point normal form."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "q_*=P_ord L_alpha^2 L_beta^2",
        "D C_3",
        "O_C(rho+2,-e-1)=O_C(P_alpha+P_beta)",
        "does not prove",
        "does not assume every supported root",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("CORE_ONE_TWO_POINT_NORMAL_FORM_AUDIT_PASS")


if __name__ == "__main__":
    main()
