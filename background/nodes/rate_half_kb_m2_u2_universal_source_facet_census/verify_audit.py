#!/usr/bin/env python3
"""Independent partition audit of the universal K-fiber profiles."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def partitions(total: int, maximum: int = 4) -> list[tuple[int, ...]]:
    out = []

    def visit(remaining: int, cap: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for part in range(min(cap, remaining), 0, -1):
            visit(remaining - part, part, prefix + (part,))

    visit(total, maximum, ())
    return out


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "partitions of four" in proof
    assert "not paired" in audit

    deficit_partitions = partitions(4)
    assert deficit_partitions == [(4,), (3, 1), (2, 2), (2, 1, 1),
                                  (1, 1, 1, 1)]
    degree_profiles = []
    for partition in deficit_partitions:
        deficits = partition + (0,) * (6 - len(partition))
        degree_profiles.append(tuple(sorted(4 - value for value in deficits)))
    assert len(set(degree_profiles)) == 5
    assert all(sum(profile) == 20 and profile.count(0) <= 1
               for profile in degree_profiles)
    print("RATE_HALF_KB_M2_U2_UNIVERSAL_SOURCE_FACET_CENSUS_AUDIT_PASS")


if __name__ == "__main__":
    main()
