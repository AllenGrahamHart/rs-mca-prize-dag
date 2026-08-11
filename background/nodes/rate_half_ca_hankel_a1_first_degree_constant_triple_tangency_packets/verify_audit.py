#!/usr/bin/env python3
"""Static claim-boundary audit for the tangency packet leaf."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = (ROOT / "statement.md").read_text()
    proof = (ROOT / "proof.md").read_text()
    audit = (ROOT / "audit.md").read_text()
    joined = statement + proof + audit
    for token in (
        "2 I_0+I_E<=sum_gamma c_gamma<=Delta",
        "length O_C/(s_F^3)",
        "{(0,2,0,2)",
        "does not exclude",
        "need not be regular",
    ):
        if token not in joined:
            raise AssertionError(f"missing audit token: {token}")
    if "pole divisor equals" in joined:
        raise AssertionError("forbidden pole-divisor identification")
    print("CONSTANT_TRIPLE_PACKETS_AUDIT_PASS")


if __name__ == "__main__":
    main()
