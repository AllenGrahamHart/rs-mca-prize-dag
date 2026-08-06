#!/usr/bin/env python3
"""Branch assembly for the h=3 slope-ratio hit gate."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Branch:
    name: str
    description: str
    membership_total: int
    hit_product_total: int


BRANCHES = {
    "generic-generic": Branch(
        name="H3-SLOPE-GG-HIT",
        description="both lambda-distinct edges have lambda != 1",
        membership_total=14,
        hit_product_total=41,
    ),
    "mixed": Branch(
        name="H3-SLOPE-MIXED-HIT",
        description="exactly one edge has lambda=1; orient the generic edge as source",
        membership_total=10,
        hit_product_total=27,
    ),
}


def classify_lambda_distinct_pair(first_is_scale: bool, second_is_scale: bool) -> str | None:
    if first_is_scale and second_is_scale:
        return None
    if first_is_scale or second_is_scale:
        return "mixed"
    return "generic-generic"


def verify_branch_partition() -> dict[str, int]:
    counts = {"generic-generic": 0, "mixed": 0, "scale-scale": 0}
    for first_is_scale in (False, True):
        for second_is_scale in (False, True):
            branch = classify_lambda_distinct_pair(first_is_scale, second_is_scale)
            if branch is None:
                counts["scale-scale"] += 1
            else:
                counts[branch] += 1
    if counts != {"generic-generic": 1, "mixed": 2, "scale-scale": 1}:
        raise AssertionError(counts)
    return counts


def slope_ratio_hit_closure(known: frozenset[str]) -> frozenset[str]:
    result = set(known)
    if {"H3-SLOPE-GG-HIT", "H3-SLOPE-MIXED-HIT"} <= result:
        result.add("H3-SLOPE-RATIO-HIT")
    return frozenset(result)


def main() -> None:
    print("h=3 repeat slope branch assembly")
    counts = verify_branch_partition()
    print(
        f"branch_partition: generic_generic={counts['generic-generic']} "
        f"mixed_orientations={counts['mixed']} "
        f"scale_scale_non_lambda_distinct={counts['scale-scale']}"
    )
    for key in ("generic-generic", "mixed"):
        branch = BRANCHES[key]
        print(
            f"{branch.name}: {branch.description}; "
            f"membership_S_total={branch.membership_total}; "
            f"hit_product_total_bound={branch.hit_product_total}"
        )
    closed = slope_ratio_hit_closure(frozenset(branch.name for branch in BRANCHES.values()))
    if "H3-SLOPE-RATIO-HIT" not in closed:
        raise AssertionError(closed)
    print("H3-SLOPE-GG-HIT + H3-SLOPE-MIXED-HIT => H3-SLOPE-RATIO-HIT")
    print("H3_REPEAT_SLOPE_BRANCH_ASSEMBLY_PASS")


if __name__ == "__main__":
    main()
