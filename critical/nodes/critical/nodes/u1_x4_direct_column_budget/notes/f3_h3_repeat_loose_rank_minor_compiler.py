#!/usr/bin/env python3
"""Rank-minor degree compiler for loose Stepanov nonvanishing gates."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_repeat_loose_stepanov_compiler import LooseTarget, compile_row, sample_targets


@dataclass(frozen=True)
class MinorDegreeRow:
    target: LooseTarget
    rank_target: int
    entry_parameter_degree: int
    minor_total_degree: int
    rank_capacity_slack: int


def entry_parameter_degree(target: LooseTarget) -> int:
    return (
        target.parameter_blocks * (target.param_degree - 1)
        + target.subgroup_order
        * (target.subgroup_degree - 1)
        * target.parameter_sum_total
    )


def minor_degree_row(target: LooseTarget) -> MinorDegreeRow:
    compiled = compile_row(target)
    rank_target = compiled.conditions + 1
    entry_degree = entry_parameter_degree(target)
    if compiled.rank_capacity_slack <= 0:
        raise AssertionError((target, compiled.rank_capacity_slack, "rank target exceeds X-capacity"))
    return MinorDegreeRow(
        target=target,
        rank_target=rank_target,
        entry_parameter_degree=entry_degree,
        minor_total_degree=rank_target * entry_degree,
        rank_capacity_slack=compiled.rank_capacity_slack,
    )


def main() -> None:
    print("h=3 repeat loose rank-minor degree compiler")
    print("rank >= r is a nonzero r-minor condition in the cleared substitution matrix")
    print("entry parameter degree: m(P-1)+n(B-1)S_total")
    print("r-minor total parameter degree <= r * entry_degree")
    print(" target     r_target  entry_degree   minor_degree  capacity_slack")
    for target in sample_targets():
        row = minor_degree_row(target)
        print(
            f"{target.name:9s} {row.rank_target:9d}"
            f" {row.entry_parameter_degree:13d}"
            f" {row.minor_total_degree:14d}"
            f" {row.rank_capacity_slack:15d}"
        )
    print("missing theorem: exhibit rank-good minors nonzero on repaired loose parameter images")
    print("H3_REPEAT_LOOSE_RANK_MINOR_COMPILER_PASS")


if __name__ == "__main__":
    main()
