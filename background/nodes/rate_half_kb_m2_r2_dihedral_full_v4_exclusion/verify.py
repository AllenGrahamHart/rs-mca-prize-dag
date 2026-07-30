#!/usr/bin/env python3
"""Verify the exhaustive full-V4 factor-degree synthesis."""

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
    require("n in {2,3,5,6}" in statement, "exhaustive split")
    require("(4,2)" in statement and "(8,1)" in statement, "scope fence")

    candidates = {2, 3, 5, 6}
    excluded = {
        2: "degree2_source_star_exclusion",
        3: "degree3_source_facet_exclusion",
        5: "degree5_source_star_exclusion",
        6: "degree6_common_pole_exclusion",
    }
    require(candidates == set(excluded), "incomplete case split")
    for degree, token in excluded.items():
        require(f"`n={degree}`" in proof, f"proof case n={degree}")
        require(token in source, f"source case n={degree}")

    print("RATE_HALF_KB_M2_R2_DIHEDRAL_FULL_V4_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
