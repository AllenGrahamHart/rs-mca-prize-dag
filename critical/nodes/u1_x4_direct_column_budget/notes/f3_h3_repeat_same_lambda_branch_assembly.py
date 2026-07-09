#!/usr/bin/env python3
"""Branch assembly for the h=3 same-lambda value gate."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_repeat_lambda_one_scale_h2_cap import (
    combined_scale_pair_bound,
    scale_h2_cap_summary,
)


@dataclass(frozen=True)
class SameLambdaBranch:
    name: str
    description: str
    membership_total: int
    extra_domain_degree: int


STRICT_BRANCHES = (
    SameLambdaBranch(
        name="H3-VALUE-GEN-INJECTIVE",
        description="lambda != 1: no two admissible generic S3 ratio orbits",
        membership_total=14,
        extra_domain_degree=10,
    ),
    SameLambdaBranch(
        name="H3-VALUE-SCALE-INJECTIVE",
        description="lambda = 1: no two admissible primitive-cube scale orbits",
        membership_total=6,
        extra_domain_degree=3,
    ),
)


def strict_value_closure(known: frozenset[str]) -> frozenset[str]:
    result = set(known)
    if {branch.name for branch in STRICT_BRANCHES} <= result:
        result.add("H3-VALUE-INJECTIVE")
    return frozenset(result)


def main() -> None:
    print("h=3 repeat same-lambda branch assembly")
    for branch in STRICT_BRANCHES:
        print(
            f"{branch.name}: {branch.description}; "
            f"membership_S_total={branch.membership_total}; "
            f"extra_domain_degree={branch.extra_domain_degree}"
        )
    closed = strict_value_closure(frozenset(branch.name for branch in STRICT_BRANCHES))
    if "H3-VALUE-INJECTIVE" not in closed:
        raise AssertionError(closed)
    print("H3-VALUE-GEN-INJECTIVE + H3-VALUE-SCALE-INJECTIVE => H3-VALUE-INJECTIVE")
    first_official = 2**13
    scale_bound = combined_scale_pair_bound(first_official)
    if scale_bound >= first_official * first_official:
        raise AssertionError((first_official, scale_bound))
    scale_refined = scale_h2_cap_summary()
    print(
        "count route: H3-VALUE-GEN-INJECTIVE plus scale-count leaves the "
        "combined trivial/h2 affine scale collision payment"
    )
    print(f"first_official_scale_pair_bound={scale_bound}")
    print(f"h2_scale_cap_first_better=2^{scale_refined['first_h2_better_s']}")
    print("H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY_PASS")


if __name__ == "__main__":
    main()
