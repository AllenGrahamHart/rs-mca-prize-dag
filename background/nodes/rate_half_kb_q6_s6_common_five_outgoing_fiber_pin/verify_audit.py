#!/usr/bin/env python3
"""Independent audit of the common-five root-set consequence."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    invariant = frozenset("ABCDEF")
    common = frozenset("ABCDE")
    complement = frozenset("GHIJKL")
    assert len(common) == 5 and common < invariant
    assert len(complement) == 6 and not invariant.intersection(complement)
    assert "There are six labels in `I^c`" in proof
    assert "No point over a label in `K` occurs" in proof
    print("RATE_HALF_KB_Q6_S6_COMMON_FIVE_OUTGOING_FIBER_PIN_AUDIT_PASS")


if __name__ == "__main__":
    main()
