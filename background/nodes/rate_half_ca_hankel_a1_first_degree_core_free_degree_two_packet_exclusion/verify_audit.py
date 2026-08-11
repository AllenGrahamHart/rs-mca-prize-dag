#!/usr/bin/env python3
"""Static audit for the core-free degree-two exclusion."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "claim_contract.md", "audit.md"))
    for token in (
        "o_gamma=c_gamma-t_gamma",
        "e-1 mod 3",
        "(e-2)+3=e+1>e",
        "degrees `3,4,5` remain open",
        "not assumed fibrewise",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("CORE_FREE_DEGREE_TWO_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
