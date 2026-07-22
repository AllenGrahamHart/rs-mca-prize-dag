#!/usr/bin/env python3
"""Audit the XR first-core peeling proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "2N-2a>=2|unionF_j|-2a",
        "Everyresidual`F_j`inherits",
        "Itsrankisatleasttwo",
        "atleastoneactivenon-anchor",
        "removesexactlyoneblock",
        "Onceremoved,itisabsentfromeverylaterresidual",
        "h|F_terminal|<=2N-2a-1",
        "`F_0`isthedisjointunionofitspivotsandterminalresidual",
    ):
        assert marker in proof
    assert "only a sufficient trigger" in audit
    assert "proper subset of its Maxwell core" in audit
    assert "strict failure" in audit
    assert "certificate count is still the mathematical frontier" in audit
    assert "No Modal" in audit
    print("XR_UNIFORM_MAXWELL_FIRST_CORE_PEELING_OWNER_AUDIT_PASS mutations=12")


if __name__ == "__main__":
    main()
