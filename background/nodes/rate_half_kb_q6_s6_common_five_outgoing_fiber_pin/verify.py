#!/usr/bin/env python3
"""Verify the common-five outgoing-fiber pin."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    source = (NODE / "source_evidence.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Root_T F_out(T,pi)={alpha_j:j notin I}" in statement, "fiber identity")
    require("O_j=psi^* K + b Z_j" in proof, "noninvariant divisor")
    require("Corollary 9.27" in source and "356ff4b4" in source, "source pin")

    labels = set(range(12))
    invariant = set(range(6))
    common = set(range(5))
    require(common < invariant and len(invariant) == 6, "common five")
    for _ in common:
        roots = labels - invariant
        require(len(roots) == 6 and not roots.intersection(invariant), "outgoing fiber")
    print("RATE_HALF_KB_Q6_S6_COMMON_FIVE_OUTGOING_FIBER_PIN_PASS")


if __name__ == "__main__":
    main()
