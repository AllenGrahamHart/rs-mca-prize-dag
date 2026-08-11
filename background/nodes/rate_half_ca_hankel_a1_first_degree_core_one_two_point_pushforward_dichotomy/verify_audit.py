#!/usr/bin/env python3
"""Static boundary audit for the two-point pushforward dichotomy."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    text = "\n".join((ROOT / name).read_text() for name in
                     ("statement.md", "proof.md", "audit.md"))
    for token in (
        "k_(x_*)^2",
        "O(1-d)^2",
        "Smith exponents",
        "does not exclude either splitting",
        "not excluded",
    ):
        if token not in text:
            raise AssertionError(f"missing audit token: {token}")
    if "O(2) direct_sum" in text:
        raise AssertionError("forbidden exponent-two splitting")
    print("TWO_POINT_PUSHFORWARD_AUDIT_PASS")


if __name__ == "__main__":
    main()
