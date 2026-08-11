#!/usr/bin/env python3
"""Static audit for the core-free cubic root router."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "u+v=e+1",
        "t_x<=c_x+epsilon_x",
        "(3-r)e<=3u+2I_0<=5u",
        "5u<e",
        "one double and one simple root",
        "does not exclude",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    print("CORE_FREE_CUBIC_ROOT_ROUTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
